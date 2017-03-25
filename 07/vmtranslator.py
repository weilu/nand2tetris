#!/usr/bin/env python3

import sys

ASM_END_BLOCK = '\n'.join((
    '(END)',
    '  @END',
    '  0;JMP'))

boolean_label_counter = 0
filename = ''

def strip_comments(line):
    try:
        return line[0:line.index('//')].strip()
    except ValueError:
        return line.strip()

def parse(line):
    line = strip_comments(line)
    if not line:
        return ''

    words = [w.strip() for w in line.split(' ')]
    op = words[0]

    if len(words) == 1:
        if op not in OP_TRANSLATE_FUNCTIONS:
            raise ValueError('Illegal operator: {}'.format(op))
        return OP_TRANSLATE_FUNCTIONS[op]()
    else:
        if op == 'push':
            return translate_push(words[1], words[2])
        elif op == 'pop':
            return translate_pop(words[1], words[2])
        elif op == 'label':
            return translate_label(words[1])
        elif op == 'if-goto':
            return translate_goto(words[1], conditional=True)
        elif op == 'goto':
            return translate_goto(words[1])
        elif op == 'function':
            return translate_function(words[1], words[2])
        else:
            raise ValueError('Illegal operator: {}'.format(op))

def translate_function(function_name, arg_count):
    return '\n'.join((
        '// === function {name} ===',
        '({name})',
        '@{count}',
        'D=A-1',
        '({name}$INIT_LOCALS)',
        '  @LCL',
        '  A=M+D',
        '  M=0',
        '  D=D-1',
        '  @SP',
        '  M=M+1 // forward SP to skip local pointer addresses',
        '  @{name}$INIT_LOCALS',
        '  D;JGE',
        '\n')).format(name=function_name, count=arg_count)

def translate_label(label_name):
    return '\n'.join((
        '// === label {name} ===',
        '(global${name})',
        '\n')).format(name=label_name)

def translate_goto(label_name, conditional=False):
    return '\n'.join((
        '// === if-goto {name} ===',
        pop_assign_addr_to_a(),
        'D=M',
        '@global${name}',
        'D;JNE' if conditional else '0;JMP',
        '\n')).format(name=label_name)

SEGMENT_START_MAP = {
        'local': 'LCL',
        'argument': 'ARG',
        'this': 'THIS',
        'that': 'THAT',
        'temp': 'R5',
        }

def get_pointer_addr(i):
    if i =='0':
        return 'THIS'
    elif i == '1':
        return 'THAT'
    else:
        raise ValueError('Illegal value for i={} in `push pointer i`'.format(i))

def translate_push(segment, i):
    if segment == 'constant':
        return '\n'.join((
            '// === push constant {i} ===',
            '@{i} // D=i',
            'D=A',
            '@SP  // *SP=D',
            'A=M',
            'M=D',
            advance_stack_pointer())).format(i=i)
    elif segment in set(('local', 'argument', 'this', 'that')):
        return push_read_start_from('M', segment, i)
    elif segment in set(('temp',)):
        return push_read_start_from('A', segment, i)
    elif segment == 'pointer':
        addr = get_pointer_addr(i)
        return '\n'.join((
            '// === push pointer {i} ===',
            '@{addr} // D={addr}',
            'D=M',
            '@SP  // *SP=D',
            'A=M',
            'M=D',
            advance_stack_pointer())).format(i=i, addr=addr)
    elif segment == 'static':
        return '\n'.join((
            '// === push static {i} ===',
            '@{program}.{i} // D=*{program}.{i}',
            'D=M',
            '@SP  // *SP=D',
            'A=M',
            'M=D',
            advance_stack_pointer())).format(i=i, program=filename)
    else:
        raise ValueError('pushing segment {} is not supported'.format(segment))

def push_read_start_from(register, segment, i):
    return '\n'.join((
        '// === push {segment} {i} ===',
        '@{start} // *{start}=D',
        'D={register}',
        '@{i} // D={start}+i',
        'A=D+A',
        'D=M',
        '@SP  // *SP=D',
        'A=M',
        'M=D',
        advance_stack_pointer())).format(register=register, segment=segment, i=i,
                start=SEGMENT_START_MAP[segment])

def translate_pop(segment, i):
    if segment == 'constant':
        raise ValueError('Cannot pop constant. Illegal vm command')
    elif segment in set(('local', 'argument', 'this', 'that')):
        return pop_read_from('M', segment, i)
    elif segment in set(('temp',)):
        return pop_read_from('A', segment, i)
    elif segment =='pointer':
        addr = get_pointer_addr(i)
        d_assignment_block = '\n'.join((
            '@{addr} // D={addr}',
            'D=A')).format(addr=addr)
        return pop_write_to_address_d(segment, i, d_assignment_block)
    elif segment =='static':
        d_assignment_block = '\n'.join((
            '@{program}.{i} // D={program}.{i}',
            'D=A')).format(i=i, program=filename)
        return pop_write_to_address_d(segment, i, d_assignment_block)
    else:
        raise ValueError('popping segment {} is not supported'.format(segment))

def pop_write_to_address_d(segment, i, d_assignment_block):
        return '\n'.join((
            '// === pop {segment} {i} ===',
            d_assignment_block,
            '@tmp // tmp=D',
            'M=D',
            pop_assign_addr_to_a(),
            'D=M // D=*SP',
            '@tmp // *tmp=D',
            'A=M',
            'M=D',
            '\n')).format(segment=segment, i=i)

def pop_read_from(register, segment, i):
        d_assignment_block = '\n'.join((
            '@{start} // D={start}',
            'D={register}',
            '@{i} // D={start}+i',
            'D=D+A',
            )).format(register=register, i=i, start=SEGMENT_START_MAP[segment])
        return pop_write_to_address_d(segment, i, d_assignment_block)

def translate_add():
    return '\n'.join((
        '// === add ===',
        pop_two_assign_first_to_d_second_addr_to_a(),
        'M=D+M // *SP=D+*SP',
        advance_stack_pointer()))

def translate_sub():
    return '\n'.join((
        '// === sub ===',
        pop_two_assign_first_to_d_second_addr_to_a(),
        'M=M-D // *SP=*SP-D',
        advance_stack_pointer()))

def translate_neg():
    return '\n'.join((
        '// === neg ===',
        pop_assign_addr_to_a(),
        'M=-M // *SP=-*SP',
        advance_stack_pointer()))

def translate_eq():
    return '\n'.join((
        '// === eq ===',
        pop_two_assign_first_to_d_second_addr_to_a(),
        set_stack_boolean_if('JEQ'),
        advance_stack_pointer()))

def translate_lt():
    return '\n'.join((
        '// === lt ===',
        pop_two_assign_first_to_d_second_addr_to_a(),
        set_stack_boolean_if('JLT'),
        advance_stack_pointer()))

def translate_gt():
    return '\n'.join((
        '// === gt ===',
        pop_two_assign_first_to_d_second_addr_to_a(),
        set_stack_boolean_if('JGT'),
        advance_stack_pointer()))

def translate_not():
    return '\n'.join((
        '// === not ===',
        pop_assign_addr_to_a(),
        'M=!M // *SP=!*SP',
        advance_stack_pointer()))

def set_stack_boolean_if(jump_condition):
    global boolean_label_counter
    boolean_label_counter += 1
    return '\n'.join((
        'D=M-D',
        '@{condition}_SET_TRUE_{counter}',
        'D;{condition}',
        '@SP',
        'A=M',
        'M=0',
        '@{condition}_RESUME_{counter}',
        '0;JMP',
        '({condition}_SET_TRUE_{counter})',
        '  @SP',
        '  A=M',
        '  M=-1',
        '({condition}_RESUME_{counter})')) \
    .format(condition=jump_condition, counter=boolean_label_counter)

def translate_and():
    return '\n'.join((
        '// === and ===',
        pop_two_assign_first_to_d_second_addr_to_a(),
        'M=D&M // *SP=D&*SP',
        advance_stack_pointer()))

def translate_or():
    return '\n'.join((
        '// === or ===',
        pop_two_assign_first_to_d_second_addr_to_a(),
        'M=D|M // *SP=D|*SP',
        advance_stack_pointer()))

def translate_return():
    return '\n'.join((
        '// === return ===',
        '@SP',
        'A=M-1',
        'D=M // read return value',
        '@return_value',
        'M=D // save return value in var return_value',

        '@LCL',
        'D=M',
        '@SP',
        'M=D-1 // SP points to LCL-1',
        'A=M',
        'D=M // read prev THAT value',
        '@THAT',
        'M=D // restore THAT',
        '@SP',
        'M=M-1 // pop',
        'A=M',
        'D=M // read prev THIS value',
        '@THIS',
        'M=D // restore THIS',
        '@SP',
        'M=M-1 // pop',
        'A=M',
        'D=M // read prev ARG value',
        '@ARG',
        'M=D // restore ARG',
        '@SP',
        'M=M-1 // pop',
        'A=M',
        'D=M // read prev LCL value',
        '@LCL',
        'M=D // restore LCL',
        '@SP',
        'M=M-1 // pop',
        'A=M',
        'D=M',
        '@return_addr',
        'M=D // save return address in var return_addr',

        '@return_value',
        'D=M // hold return value in D',
        '@SP',
        'M=M-1 // pop to restore SP value',
        'A=M-1',
        'M=D // push return value to top of the stack',

        '@return_addr',
        'A=M // read return address value',
        '0;JMP',
        '\n'))

def pop_assign_addr_to_a():
    return '\n'.join((
        '@SP',
        'M=M-1 // pop',
        'A=M'))

def pop_two_assign_first_to_d_second_addr_to_a():
    return '\n'.join((
        pop_assign_addr_to_a(),
        'D=M // D=*SP',
        pop_assign_addr_to_a()))

def advance_stack_pointer():
    return '\n'.join((
        '@SP // SP++',
        'M=M+1',
        '\n'))

OP_TRANSLATE_FUNCTIONS = {
    'add': translate_add,
    'sub': translate_sub,
    'neg': translate_neg,
    'eq': translate_eq,
    'lt': translate_lt,
    'gt': translate_gt,
    'and': translate_and,
    'or': translate_or,
    'not': translate_not,
    'return': translate_return }

def main():
    if len(sys.argv) != 2 or not sys.argv[1].endswith('.vm'):
        print('Usage: ./vmtranslator.py input.vm')
        return

    infile = sys.argv[1]
    global filename
    filename = infile.split('/')[-1].replace('.vm', '')
    outfile = infile.replace('vm', 'asm')
    with open(outfile, 'w') as output_file:
        with open(infile) as input_file:
            for line in input_file:
                asm_block = parse(line)
                output_file.write(asm_block)
            output_file.write(ASM_END_BLOCK)

if __name__ == "__main__":
    main()
