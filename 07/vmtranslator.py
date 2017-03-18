#!/usr/bin/env python3

import sys

ARITHMETIC_OPS = set(('add', 'sub', 'neg', 'eq', 'lt', 'gt', ))
BOOLEAN_OPS = set(('not', 'and', 'or'))
STACK_OPS = set(('push', 'pop'))

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
        validate_arithmetic_or_boolean(op)
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
            raise ValueError('op {} is not supported yet'.format(op))
    else:
        validate_stack(op)
        if op == 'push':
            return translate_push(words[1], words[2])
        else:
            return translate_pop(words[1], words[2])

def translate_push(segment, i):
    if segment == 'constant':
        return '\n'.join((
            '// === push constant {i} ===',
            '@{i} // D=i',
            'D=A',
            '@SP  // *SP=D',
            'A=M',
            'M=D',
            '@SP  // SP++',
            'M=M+1',
            '\n')).format(i=i)
    else:
        raise ValueError('pushing segment {} is not supported'.format(segment))

def translate_pop(segment, i):
    if segment == 'constant':
        return '\n'.join((
            '// === pop constant {i} === TODO',
            '\n')).format(i=i)
    else:
        raise ValueError('popping segment {} is not supported'.format(segment))

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
        'M=M-D// *SP=*SP-D',
        advance_stack_pointer()))

def translate_neg():
    return '\n'.join((
        '// === neg ===',
        '@SP',
        'M=M-1 // pop',
        'A=M',
        'M=-M  // *SP=-*SP',
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
        '@SP',
        'M=M-1 // pop',
        'A=M',
        'M=!M  // *SP=!*SP',
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

def pop_two_assign_first_to_d_second_addr_to_a():
    return '\n'.join((
        '@SP',
        'M=M-1 // pop',
        'A=M',
        'D=M   // D=*SP',
        '@SP',
        'M=M-1 // pop',
        'A=M'))

def advance_stack_pointer():
    return '\n'.join((
        '@SP   // SP++',
        'M=M+1',
        '\n'))

def validate_arithmetic_or_boolean(op):
    if op not in ARITHMETIC_OPS and op not in BOOLEAN_OPS:
        raise ValueError('Illegal arithmetic/boolean operator: {}'.format(op))

def validate_stack(op):
    if op not in STACK_OPS:
        raise ValueError('Illegal stack operator: {}'.format(op))

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
