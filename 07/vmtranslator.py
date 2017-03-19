#!/usr/bin/env python3

import sys

ASM_END_BLOCK = '\n'.join((
    '(END)',
    '  @END',
    '  0;JMP'))

counter = 0

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
        if op == 'add':
            return translate_add()
        elif op == 'sub':
            return translate_sub()
        elif op == 'neg':
            return translate_neg()
        elif op == 'eq':
            return translate_eq()
        elif op == 'lt':
            return translate_lt()
        elif op == 'gt':
            return translate_gt()
        elif op == 'and':
            return translate_and()
        elif op == 'or':
            return translate_or()
        elif op == 'not':
            return translate_not()
        else:
            raise ValueError('Illegal arithmetic/boolean operator: {}'.format(op))
    else:
        if op == 'push':
            return translate_push(words[1], words[2])
        elif op == 'pop':
            return translate_pop(words[1], words[2])
        else:
            raise ValueError('Illegal stack operator: {}'.format(op))

SEGMENT_START_MAP = {
        'local': 'LCL',
        'argument': 'ARG',
        'this': 'THIS',
        'that': 'THAT',
        'temp': 'R5',
        }

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
    else:
        raise ValueError('popping segment {} is not supported'.format(segment))

def pop_read_from(register, segment, i):
        return '\n'.join((
            '// === pop {segment} {i} ===',
            '@{start} // D={start}',
            'D={register}',
            '@{i} // D={start}+i',
            'D=D+A',
            '@{segment}_{i} // {segment}_{i}=D',
            'M=D',
            pop_assign_addr_to_a(),
            'D=M // D=*SP',
            '@{segment}_{i} // *{segment}_{i}=D',
            'A=M',
            'M=D')).format(register=register, segment=segment, i=i,
                    start=SEGMENT_START_MAP[segment])

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
    global counter
    counter += 1
    return '\n'.join((
        'D=M-D',
        '@{condition}_SET_TRUE_{counter}',
        'D;{condition}',
        '({condition}_SET_FALSE_{counter})',
        '  @SP',
        '  A=M',
        '  M=0',
        '  @{condition}_RESUME_{counter}',
        '  0;JMP',
        '({condition}_SET_TRUE_{counter})',
        '  @SP',
        '  A=M',
        '  M=-1',
        '({condition}_RESUME_{counter})')) \
    .format(condition=jump_condition, counter=counter)

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

def main():
    if len(sys.argv) != 2 or not sys.argv[1].endswith('.vm'):
        print('Usage: ./vmtranslator.py input.vm')
        return

    infile = sys.argv[1]
    outfile = infile.replace('vm', 'asm')
    with open(outfile, 'w') as output_file:
        with open(infile) as input_file:
            for line in input_file:
                asm_block = parse(line)
                output_file.write(asm_block)
            output_file.write(ASM_END_BLOCK)

if __name__ == "__main__":
    main()
