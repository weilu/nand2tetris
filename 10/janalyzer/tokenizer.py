import re

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

def tokenize(line):
    if not line:
        return []

    tokens = []
    token_start = 0
    string_start = False
    for m in re.finditer(' |\(|\)|\[|\]|\.|"|;|,|~|-|$', line):
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
                parsed = parse(line[token_start:token_end])
                if parsed:
                    tokens.append(parsed)
                token_start = m.end()
            else:
                next # skip until the end of the string

        # handle non-space and non-quote delimiter
        if delimiter not in (' ', '"', '$'):
            parsed = parse(delimiter)
            if parsed:
                tokens.append(parsed)

    return tokens


def parse(word):
    if word == '':
        return ''

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


def format_token(token_value, token_type):
    return '<{}> {} </{}>'.format(token_type, token_value, token_type)
