import sys
import re
from os import path

KEY_WORDS = { 'class', 'constructor', 'function', 'method', 'field', 'static',
        'var', 'int', 'char', 'boolean', 'void', 'true', 'false', 'null',
        'this', 'let', 'do', 'if', 'else', 'while', 'return' }

SYMBOLS = { '{', '}', '(', ')', '[', ']', '.', ',', ';', '+', '-', '*', '/',
        '|', '=', '~' }

ESCAPED_SYMBOLS = {
        '&': '&amp;',
        '"': '&quot;',
        '<': '&lt;',
        '>': '&gt;'
        }

def format_token(token_value, token_type):
    return '<{}> {} </{}>\n'.format(token_type, token_value, token_type)


def parse(word):
    if word == '':
        return ''
    print(word)

    if word in KEY_WORDS:
        return format_token(word, 'keyword')
    elif word in SYMBOLS:
        return format_token(word, 'symbol')
    elif word in ESCAPED_SYMBOLS.keys():
        return format_token(ESCAPED_SYMBOLS[word], 'symbol')
    else:
        try:
            int_value = int(word)
            if int_value > 32767:
                raise ValueError('Invalid int value {}'.format(word))
            return format_token(word, 'integerConstant')
        except ValueError:
            if re.match('\w+', word) and not re.match('^\d', word):
                return format_token(word, 'identifier')
            else:
                raise ValueError('Invalid identifier {}'.format(word))


def tokenize(line):
    if not line:
        return ''
    tokens = []
    token_start = 0
    string_start = False
    for m in re.finditer(' |\(|\)|\[|\]|\.|"|;|,|~|$', line):
        delimiter = m.group()
        if delimiter == '"':
            if not string_start: # open quote
                string_start = True
                token_start += 1
            else: # close quote
                token_end = m.start()
                tokens.append(format_token(line[token_start:token_end],
                    'stringConstant'))
                token_start = m.end()
                string_start = False
        else:
            if not string_start:
                # parse token up to the delimiter & forward token pointer
                token_end = m.start()
                tokens.append(parse(line[token_start:token_end]))
                token_start = m.end()
            else:
                next # skip until the end of the string

        # handle non-space and non-quote delimiter
        if delimiter not in (' ', '"', '$'):
            tokens.append(parse(delimiter))

    return ''.join(tokens)


def strip_comments(source):
    source = re.sub(re.compile("/\*.*?\*/", re.DOTALL), "", source) # /* */
    source = re.sub(re.compile("//.*$", re.MULTILINE), "", source) # //
    source = re.sub(re.compile("^\s*$\n", re.MULTILINE), "", source) # blank line
    return source


def main():
    if len(sys.argv) != 2:
        print('Usage: ./JackAnalyzer.py input.jack')
        return

    infile = sys.argv[1]
    if not infile.endswith('.jack') and not path.isdir(infile):
        print('Usage: ./JackAnalyzer.py input.jack')
        return


    infiles = [infile]
    if path.isdir(infile):
        infile = path.abspath(infile)
        infiles = glob(path.join(infile, '*.jack'))


    for infile in infiles:
        # TODO: drop "Out" prefix before submission
        outfile = infile.replace('.jack', 'Out.xml')
        with open(outfile, 'w') as output_file:
            output_file.write('<tokens>\n')
            with open(infile) as input_file:
                source = strip_comments(input_file.read())
                source = source.split('\n')
                for line in source:
                    output_file.write(tokenize(line.strip()))
            output_file.write('</tokens>\n')

if __name__ == "__main__":
    main()
