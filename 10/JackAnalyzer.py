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
    return '<{}> {} </{}>'.format(token_type, token_value, token_type)


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


def tokenize(line):
    if not line:
        return []

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

def is_class_var_start(token):
    return token in('<keyword> field </keyword>', '<keyword> static </keyword>')

def is_subroutine_start(token):
    return token in('<keyword> constructor </keyword>',
            '<keyword> function </keyword>',
            '<keyword> method </keyword>')

def is_open_bracket(token):
    return token in ('<symbol> ( </symbol>')

def is_close_bracket(token):
    return token in('<symbol> ) </symbol>')

def is_open_square_bracket(token):
    return token in ('<symbol> [ </symbol>')

def is_close_square_bracket(token):
    return token in ('<symbol> ] </symbol>')

def is_close_brace(token):
    return token in('<symbol> } </symbol>')

def is_comma(token):
    return token == '<symbol> , </symbol>'

def is_dot(token):
    return token in ('<symbol> . </symbol>')

def is_unary_op(token):
    return token in { '<symbol> - </symbol>', '<symbol> ~ </symbol>' }

def is_op(token):
    return token in {
            '<symbol> + </symbol>',
            '<symbol> - </symbol>',
            '<symbol> * </symbol>',
            '<symbol> / </symbol>',
            '<symbol> &amp; </symbol>',
            '<symbol> | </symbol>',
            '<symbol> &lt; </symbol>',
            '<symbol> &gt; </symbol>',
            '<symbol> = </symbol>', }

def is_var_start(token):
    return token in('<keyword> var </keyword>', )

def is_statement_start(token):
    return token in('<keyword> let </keyword>',
            '<keyword> if </keyword>',
            '<keyword> else </keyword>',
            '<keyword> while </keyword>',
            '<keyword> do </keyword>',
            '<keyword> return </keyword>',
            )

def is_return_statement_start(token):
    return (token == '<keyword> return </keyword>')

def is_let_statement_start(token):
    return (token == '<keyword> let </keyword>')

def is_if_statement_start(token):
    return (token == '<keyword> if </keyword>')

def is_else_start(token):
    return (token == '<keyword> else </keyword>')

def is_while_statement_start(token):
    return (token == '<keyword> while </keyword>')

def is_do_statement_start(token):
    return (token == '<keyword> do </keyword>')

def is_keyword_constant(token):
    return token in {
            '<keyword> true </keyword>',
            '<keyword> false </keyword>',
            '<keyword> null </keyword>',
            '<keyword> this </keyword>' }

def is_contant(token):
    return (token.startswith('<integerConstant>') or
            token.startswith('<stringConstant>') or is_keyword_constant(token))

def is_identifier(token):
    return token.startswith('<identifier>')

def compile_class_var(tokens, i):
    out = ['<classVarDec>',
            tokens[i]]
    i += 1
    while i < len(tokens):
        if is_class_var_start(tokens[i]):
            out.append('</classVarDec>')
            compiled, i = compile_class_var(tokens, i)
            out.append(compiled)
            return ('\n'.join(out), i)
        elif is_subroutine_start(tokens[i]):
            out.append('</classVarDec>')
            compiled, i = compile_subroutine(tokens, i)
            out.append(compiled)
            return ('\n'.join(out), i)
        else:
            out.append(tokens[i])
            i += 1
    out.append('</classVarDec>')
    return ('\n'.join(out), i)


def compile_subroutine(tokens, i):
    out = ['<subroutineDec>',
            tokens[i]]
    i += 1
    while i < len(tokens):
        if is_class_var_start(tokens[i]):
            out.append('</subroutineDec>')
            compiled, i = compile_class_var(tokens, i)
            out.append(compiled)
            return ('\n'.join(out), i)
        elif is_subroutine_start(tokens[i]):
            out.append('</subroutineDec>')
            compiled, i = compile_subroutine(tokens, i)
            out.append(compiled)
            return ('\n'.join(out), i)
        else:
            token = tokens[i]
            out.append(token)
            i += 1
            if token == '<symbol> ( </symbol>':
                compiled, i = compile_parameter_list(tokens, i)
                out.append(compiled)
                out.append(tokens[i]) # append )
                if tokens[i+1] != '<symbol> { </symbol>':
                    raise ValueError('expect { following parameters')
                compiled, i = compile_subroutine_body(tokens, i+1)
                out.append(compiled)
                break
    out.append('</subroutineDec>')
    return ('\n'.join(out), i)


def compile_parameter_list(tokens, i):
    out = ['<parameterList>']
    while i < len(tokens):
        if tokens[i] == '<symbol> ) </symbol>':
            break
        else:
            out.append(tokens[i])
            i += 1
    out.append('</parameterList>')
    return ('\n'.join(out), i)


def compile_subroutine_body(tokens, i):
    out = ['<subroutineBody>',
            tokens[i]] # TODO: validate {

    i += 1
    if is_var_start(tokens[i]):
        compiled, i = compile_var(tokens, i)
        out.append(compiled)
    elif is_statement_start(tokens[i]):
        compiled, i = compile_statements(tokens, i)
        out.append(compiled)
    else:
        raise ValueError('subroutine can only contain variable declarations or statements')

    # validate & append closing }
    if not is_close_brace(tokens[i]):
        raise ValueError('missing closing } for subroutine')
    out.append(tokens[i])
    i += 1

    out.append('</subroutineBody>')
    return ('\n'.join(out), i)


def compile_var(tokens, i):
    out = ['<varDec>',
            tokens[i]]
    i += 1
    while i < len(tokens):
        if is_var_start(tokens[i]):
            out.append('</varDec>')
            compiled, i = compile_var(tokens, i)
            out.append(compiled)
            return ('\n'.join(out), i)
        elif is_statement_start(tokens[i]):
            out.append('</varDec>')
            compiled, i = compile_statements(tokens, i)
            out.append(compiled)
            return ('\n'.join(out), i)
        else:
            out.append(tokens[i])
            i += 1
    out.append('</varDec>')
    return ('\n'.join(out), i)


def compile_statements(tokens, i):
    out = ['<statements>' ]
    while i < len(tokens):
        if is_return_statement_start(tokens[i]):
            compiled, i = compile_return(tokens, i)
            out.append(compiled)
            break
        if is_let_statement_start(tokens[i]):
            compiled, i = compile_let(tokens, i)
            out.append(compiled)
        elif is_if_statement_start(tokens[i]):
            compiled, i = compile_if(tokens, i)
            out.append(compiled)
        elif is_while_statement_start(tokens[i]):
            compiled, i = compile_while(tokens, i)
            out.append(compiled)
        elif is_do_statement_start(tokens[i]):
            compiled, i = compile_do(tokens, i)
            out.append(compiled)
        else:
            break
    out.append('</statements>')
    return ('\n'.join(out), i)


def compile_do(tokens, i):
    out = ['<doStatement>']
    out.append(tokens[i]) # do
    i += 1
    compiled, i = compile_subroutine_call(tokens, i)
    out.append(compiled)
    out.append(tokens[i]) # ;
    i += 1
    out.append('</doStatement>')
    return ('\n'.join(out), i)


def compile_while(tokens, i):
    out = ['<whileStatement>',
            tokens[i], # TODO: validate if
            tokens[i+1], # TODO: validate (
            ]
    i = i+2

    compiled, i = compile_expression(tokens, i)
    out.append(compiled)
    if not is_close_bracket(tokens[i]):
        raise ValueError('missing closing ) for expression')
    out.append(tokens[i])
    i += 1

    out.append(tokens[i]) # TODO: validate {
    i += 1
    compiled, i = compile_statements(tokens, i)
    out.append(compiled)

    # validate & append closing }
    if not is_close_brace(tokens[i]):
        raise ValueError('missing closing } for while block')
    out.append(tokens[i])
    i += 1

    out.append('</whileStatement>')
    return ('\n'.join(out), i)


def compile_if(tokens, i):
    out = ['<ifStatement>',
            tokens[i], # TODO: validate if
            tokens[i+1], # TODO: validate (
            ]
    i = i+2

    compiled, i = compile_expression(tokens, i)
    out.append(compiled)
    if not is_close_bracket(tokens[i]):
        raise ValueError('missing closing ) for expression')
    out.append(tokens[i])
    i += 1

    out.append(tokens[i]) # TODO: validate {
    i += 1
    compiled, i = compile_statements(tokens, i)
    out.append(compiled)

    # validate & append closing }
    if not is_close_brace(tokens[i]):
        raise ValueError('missing closing } for if block')
    out.append(tokens[i])
    i += 1

    # optional else statement
    if is_else_start(tokens[i]):
        out.append(tokens[i])
        i += 1
        out.append(tokens[i]) # TODO: validate {
        i += 1
        compiled, i = compile_statements(tokens, i)
        out.append(compiled)

        # validate & append closing }
        if not is_close_brace(tokens[i]):
            raise ValueError('missing closing } for else block')
        out.append(tokens[i])
        i += 1

    out.append('</ifStatement>')
    return ('\n'.join(out), i)


def compile_let(tokens, i):
    out = ['<letStatement>' ]
    out.append(tokens[i]) # let
    i += 1
    out.append(tokens[i]) # varName
    i += 1
    if is_open_square_bracket(tokens[i]):
        out.append(tokens[i]) # [
        i += 1
        compiled, i = compile_expression(tokens, i)
        out.append(compiled)
        out.append(tokens[i]) # ]
        i += 1
    out.append(tokens[i]) # =
    i += 1
    compiled, i = compile_expression(tokens, i)
    out.append(compiled)
    out.append(tokens[i]) # ;
    i += 1
    out.append('</letStatement>')
    return ('\n'.join(out), i)


def compile_return(tokens, i):
    out = ['<returnStatement>',
            tokens[i] ] # return
    i += 1
    compiled, i = compile_expression(tokens, i)
    if compiled:
        out.append(compiled)
    out.append(tokens[i])
    i += 1

    out.append('</returnStatement>')
    return ('\n'.join(out), i)


def compile_expression(tokens, i):
    out = ['<expression>' ]
    compiled, i = compile_term(tokens, i)
    if not compiled:
        return (None, i)
    out.append(compiled)

    if is_op(tokens[i]):
        out.append(tokens[i])
        i += 1
        compiled, i = compile_term(tokens, i)
        out.append(compiled)

    out.append('</expression>')
    return ('\n'.join(out), i)


def compile_term(tokens, i):
    out = ['<term>']
    if (is_contant(tokens[i])):
        out.append(tokens[i])
        i += 1
    elif (is_unary_op(tokens[i])):
        out.append(tokens[i])
        i += 1
        compiled, i = compile_term(tokens, i)
        out.append(compiled)
    elif (is_open_bracket(tokens[i])):
        out.append(tokens[i])
        i += 1
        compiled, i = compile_expression(tokens, i)
        out.append(compiled)
        if not is_close_bracket(tokens[i]):
            raise ValueError('missing closing ) for expression')
        out.append(tokens[i])
        i += 1
    elif (is_identifier(tokens[i])):
        look_ahead = tokens[i+1]
        if is_open_square_bracket(look_ahead):
            out.append(tokens[i]) # varName
            i += 1
            out.append(tokens[i]) # [
            i += 1
            compiled, i = compile_expression(tokens, i)
            out.append(compiled)
            if not is_close_square_bracket(tokens[i]):
                raise ValueError('missing closing ] for expression')
            out.append(tokens[i]) # ]
            i += 1
        elif is_open_bracket(look_ahead) or is_dot(look_ahead):
            compiled, i = compile_subroutine_call(tokens, i)
            out.append(compiled)
        else:
            out.append(tokens[i]) # varName
            i += 1
    else:
        return (None, i)
    out.append('</term>')
    return ('\n'.join(out), i)


def compile_subroutine_call(tokens, i):
    out = [tokens[i]] # identifier
    i += 1
    if is_dot(tokens[i]):
        out.append(tokens[i]) # .
        i += 1
        out.append(tokens[i]) # identifier
        i += 1
    elif is_open_bracket(tokens[i]):
        pass
    else:
        raise ValueError('Invalid subroutine call syntax')

    out.append(tokens[i]) # (
    i += 1
    compiled, i = compile_expression_list(tokens, i)
    out.append(compiled)
    if not is_close_bracket(tokens[i]):
        raise ValueError('missing closing ) for expression list')
    out.append(tokens[i]) # )
    i += 1

    return ('\n'.join(out), i)

def compile_expression_list(tokens, i):
    out = ['<expressionList>']
    compiled, i = compile_expression(tokens, i)
    if compiled:
        out.append(compiled)

    while is_comma(tokens[i]):
        out.append(tokens[i]) # ,
        i += 1
        compiled, i = compile_expression(tokens, i)
        out.append(compiled)

    out.append('</expressionList>')
    return ('\n'.join(out), i)


def compile_class(tokens):
    out = ['<class>',
            tokens[0],
            tokens[1], # TODO: validate identifier
            tokens[2], # TODO: validate {
            ]

    i = 3
    while i < len(tokens):
        if(is_class_var_start(tokens[i])):
            compiled, i = compile_class_var(tokens, i)
            out.append(compiled)
        elif(is_subroutine_start(tokens[i])):
            compiled, i = compile_subroutine(tokens, i)
            out.append(compiled)
        elif is_close_brace(tokens[i]):
            break
        else:
            raise ValueError('Only class variable or subroutine declaration is allowed in a class')

    # validate & append closing }
    if not is_close_brace(tokens[i]):
        raise ValueError('missing closing } for class')
    out.append(tokens[i])
    i += 1

    out.append('</class>\n')
    return '\n'.join(out)


def compile(tokens):
    if len(tokens) < 1 or tokens[0] != '<keyword> class </keyword>':
        raise ValueError('Program must start with a class declaration')
    return compile_class(tokens)


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
            tokens = []
            with open(infile) as input_file:
                source = strip_comments(input_file.read())
                source = source.split('\n')
                for line in source:
                    tokens = tokens + tokenize(line.strip())
            output_file.write(compile(tokens))

if __name__ == "__main__":
    main()
