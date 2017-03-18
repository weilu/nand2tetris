#!/usr/bin/env python3

import sys

ARITHMETIC_OPS = set(('add', 'sub', 'neg', 'eq', 'lt', 'gt', ))
BOOLEAN_OPS = set(('not', 'and', 'or'))
STACK_OPS = set(('push', 'pop'))

ASM_END_BLOCK = '\n'.join((
    '(END)',
    '  @END',
    '  0;JMP'))

def strip_comments(line):
    try:
        return line[0:line.index('//')].strip()
    except ValueError:
        return line.strip()

def parse(line):
    line = strip_comments(line)
    if not line:
        return ''

    print('[DEBUG]: parsing {}'.format(line))
    words = [w.strip() for w in line.split(' ')]
    op = words[0]

    if len(words) == 1:
        validate_arithmetic_or_boolean(op)
        if op == 'add':
            return translate_add()
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
            '@SP //*SP=D',
            'A=M',
            'M=D',
            '@SP //SP++',
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
        '@SP // pop',
        'M=M-1',
        '@SP // D=*SP',
        'A=M',
        'D=M',
        '@SP // pop',
        'M=M-1',
        '@SP //*SP=D+*SP',
        'A=M',
        'M=D+M',
        '@SP //SP++',
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
