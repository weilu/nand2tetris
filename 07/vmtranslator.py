#!/usr/bin/env python3

import sys
from os import path, sep
from glob import glob

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
            return translate_if_goto(words[1])
        elif op == 'goto':
            return translate_goto(words[1])
        elif op == 'function':
            return translate_function(words[1], words[2])
        elif op == 'call':
            return translate_call_function(words[1], words[2])
        else:
            raise ValueError('Illegal operator: {}'.format(op))

def push_caller_frame_to_stack(segment_name):
    return '\n'.join((
        '@{name}',
        'D=M',
        '@SP',
        'A=M',
        'M=D',
        advance_stack_pointer())).format(name=segment_name)

def translate_call_function(function_name, arg_count):
    return '\n'.join((
        '// === call function {name} {count} ===',
        '@{name}$return_addr',
        'D=A',
        '@SP',
        'A=M',
        'M=D',
        advance_stack_pointer(),
        push_caller_frame_to_stack('LCL'),
        push_caller_frame_to_stack('ARG'),
        push_caller_frame_to_stack('THIS'),
        push_caller_frame_to_stack('THAT'),
        '@{count}',
        'D=A',
        '@5',
        'D=D+A // save arg offset in D',
        '@SP',
        'D=M-D',
        '@ARG',
        'M=D // ARG=SP-n-5',
        '@SP',
        'D=M',
        '@LCL',
        'M=D // LCL=SP',
        '@{name}',
        '0;JMP // goto f',
        '({name}$return_addr)',
        '\n')).format(name=function_name, count=arg_count)

def translate_function(function_name, arg_count):
    return '\n'.join((
        '// === function {name} {count} ===',
        '({name})',
        '@{count}',
        'D=A-1',
        '@{name}$END_INIT_LOCALS',
        'D;JLT',
        '({name}$INIT_LOCALS)',
        '  @LCL',
        '  A=M+D',
        '  M=0',
        '  D=D-1',
        '  @SP',
        '  M=M+1 // forward SP to skip local pointer addresses',
        '  @{name}$INIT_LOCALS',
        '  D;JGE',
        '({name}$END_INIT_LOCALS)',
        '\n')).format(name=function_name, count=arg_count)

def translate_label(label_name):
    return '\n'.join((
        '// === label {name} ===',
        '(global${name})',
        '\n')).format(name=label_name)

def translate_goto(label_name):
    return '\n'.join((
        '// === goto {name} ===',
        '@global${name}',
        '0;JMP',
        '\n')).format(name=label_name)

def translate_if_goto(label_name):
    return '\n'.join((
        '// === if-goto {name} ===',
        pop_assign_addr_to_a(),
        'D=M',
        '@global${name}',
        'D;JNE',
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
        '@ARG',
        'A=M',
        'D=A',
        '@SP',
        'M=D // point SP to return value but do not write return value yet',

        '@LCL',
        'D=M',
        '@tmpsp',
        'M=D-1 // tmpsp points to LCL-1',
        'A=M',
        'D=M // read prev THAT value',
        '@THAT',
        'M=D // restore THAT',
        '@tmpsp',
        'M=M-1 // pop',
        'A=M',
        'D=M // read prev THIS value',
        '@THIS',
        'M=D // restore THIS',
        '@tmpsp',
        'M=M-1 // pop',
        'A=M',
        'D=M // read prev ARG value',
        '@ARG',
        'M=D // restore ARG',
        '@tmpsp',
        'M=M-1 // pop',
        'A=M',
        'D=M // read prev LCL value',
        '@LCL',
        'M=D // restore LCL',
        '@tmpsp',
        'M=M-1 // pop',
        'A=M',
        'D=M // read return address value',
        '@return_addr',
        'M=D // save return address in var return_addr',

        '@return_value',
        'D=M',
        '@SP',
        'A=M',
        'M=D // write return value to SP',
        advance_stack_pointer(),

        '@return_addr',
        'A=M',
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
    if len(sys.argv) != 2:
        print('Usage: ./vmtranslator.py input.vm')
        return

    infile = sys.argv[1]
    if not infile.endswith('.vm') and not path.isdir(infile):
        print('Usage: ./vmtranslator.py input.vm')
        return

    global filename
    filename = infile.split('/')[-1].replace('.vm', '')
    outfile = infile.replace('vm', 'asm')

    infiles = [infile]
    if path.isdir(infile):
        infile = path.abspath(infile)
        infiles = glob(path.join(infile, '*.vm'))
        filename = infile.split('/')[-1]
        outfile = path.join(infile, '{}.asm'.format(filename))

    with open(outfile, 'w') as output_file:
        for infile in infiles:
            with open(infile) as input_file:
                for line in input_file:
                    asm_block = parse(line)
                    output_file.write(asm_block)
                output_file.write(ASM_END_BLOCK)

if __name__ == "__main__":
    main()
