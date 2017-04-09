class Parser():

    def __init__(self, tokens):
        self.tokens = tokens
        self.i = 0

    def token(self):
        return self.tokens[self.i]

    def look_ahead_token(self):
        return self.tokens[self.i+1]

    def compile_class_var(self):
        out = ['<classVarDec>']
        out.append(self.token()) # var
        self.i += 1
        while self.i < len(self.tokens):
            if is_class_var_start(self.token()):
                out.append('</classVarDec>')
                out.append(self.compile_class_var())
                return '\n'.join(out)
            elif is_subroutine_start(self.token()):
                out.append('</classVarDec>')
                out.append(self.compile_subroutine())
                return '\n'.join(out)
            else:
                out.append(self.token())
                self.i += 1
        out.append('</classVarDec>')
        return '\n'.join(out)


    def compile_subroutine(self):
        out = ['<subroutineDec>']
        out.append(self.token())
        self.i += 1
        while self.i < len(self.tokens):
            if is_class_var_start(self.token()):
                out.append('</subroutineDec>')
                out.append(self.compile_class_var())
                return '\n'.join(out)
            elif is_subroutine_start(self.token()):
                out.append('</subroutineDec>')
                out.append(self.compile_subroutine())
                return '\n'.join(out)
            else:
                token = self.token()
                out.append(token)
                self.i += 1
                if is_open_bracket(token):
                    out.append(self.compile_parameter_list())
                    out.append(self.token()) # append )
                    if not is_open_brace(self.look_ahead_token()):
                        raise ValueError('expect { following parameters')
                    self.i += 1
                    out.append(self.compile_subroutine_body())
                    break
        out.append('</subroutineDec>')
        return '\n'.join(out)

    def compile_parameter_list(self):
        out = ['<parameterList>']
        while self.i < len(self.tokens):
            if is_close_bracket(self.token()):
                break
            else:
                out.append(self.token())
                self.i += 1
        out.append('</parameterList>')
        return '\n'.join(out)


    def compile_subroutine_body(self):
        out = ['<subroutineBody>']

        out.append(self.token()) # TODO: validate {
        self.i += 1
        if is_var_start(self.token()):
            out.append(self.compile_var())
        elif is_statement_start(self.token()):
            out.append(self.compile_statements())
        else:
            raise ValueError('subroutine can only contain variable declarations or statements')

        # validate & append closing }
        if not is_close_brace(self.token()):
            raise ValueError('missing closing } for subroutine')
        out.append(self.token())
        self.i += 1

        out.append('</subroutineBody>')
        return '\n'.join(out)

    def compile_var(self):
        out = ['<varDec>']
        out.append(self.token()) # var
        self.i += 1
        while self.i < len(self.tokens):
            if is_var_start(self.token()):
                out.append('</varDec>')
                out.append(self.compile_var())
                return '\n'.join(out)
            elif is_statement_start(self.token()):
                out.append('</varDec>')
                out.append(self.compile_statements())
                return '\n'.join(out)
            else:
                out.append(self.token())
                self.i += 1
        out.append('</varDec>')
        return '\n'.join(out)

    def compile_statements(self):
        out = ['<statements>' ]
        while self.i < len(self.tokens):
            if is_return_statement_start(self.token()):
                out.append(self.compile_return())
                break
            if is_let_statement_start(self.token()):
                out.append(self.compile_let())
            elif is_if_statement_start(self.token()):
                out.append(self.compile_if())
            elif is_while_statement_start(self.token()):
                out.append(self.compile_while())
            elif is_do_statement_start(self.token()):
                out.append(self.compile_do())
            else:
                break
        out.append('</statements>')
        return '\n'.join(out)


    def compile_do(self):
        out = ['<doStatement>']
        out.append(self.token()) # do
        self.i += 1
        out.append(self.compile_subroutine_call())
        out.append(self.token()) # ;
        self.i += 1
        out.append('</doStatement>')
        return '\n'.join(out)


    def compile_while(self):
        out = ['<whileStatement>']
        out.append(self.token()) # TODO: validate while
        self.i += 1
        out.append(self.token()) # TODO: validate (
        self.i += 1

        out.append(self.compile_expression())
        if not is_close_bracket(self.token()):
            raise ValueError('missing closing ) for expression')
        out.append(self.token())
        self.i += 1

        out.append(self.token()) # TODO: validate {
        self.i += 1
        out.append(self.compile_statements())

        # validate & append closing }
        if not is_close_brace(self.token()):
            raise ValueError('missing closing } for while block')
        out.append(self.token())
        self.i += 1

        out.append('</whileStatement>')
        return '\n'.join(out)


    def compile_if(self):
        out = ['<ifStatement>']
        out.append(self.token()) # TODO: validate if
        self.i += 1
        out.append(self.token()) # TODO: validate (
        self.i += 1

        out.append(self.compile_expression())
        if not is_close_bracket(self.token()):
            raise ValueError('missing closing ) for expression')
        out.append(self.token())
        self.i += 1

        out.append(self.token()) # TODO: validate {
        self.i += 1
        out.append(self.compile_statements())

        # validate & append closing }
        if not is_close_brace(self.token()):
            raise ValueError('missing closing } for if block')
        out.append(self.token())
        self.i += 1

        # optional else statement
        if is_else_start(self.token()):
            out.append(self.token())
            self.i += 1
            out.append(self.token()) # TODO: validate {
            self.i += 1
            out.append(self.compile_statements())

            # validate & append closing }
            if not is_close_brace(self.token()):
                raise ValueError('missing closing } for else block')
            out.append(self.token())
            self.i += 1

        out.append('</ifStatement>')
        return '\n'.join(out)


    def compile_let(self):
        out = ['<letStatement>' ]
        out.append(self.token()) # let
        self.i += 1
        out.append(self.token()) # varName
        self.i += 1
        if is_open_square_bracket(self.token()):
            out.append(self.token()) # [
            self.i += 1
            out.append(self.compile_expression())
            out.append(self.token()) # ]
            self.i += 1
        out.append(self.token()) # =
        self.i += 1
        out.append(self.compile_expression())
        out.append(self.token()) # ;
        self.i += 1
        out.append('</letStatement>')
        return '\n'.join(out)


    def compile_return(self):
        out = ['<returnStatement>' ]
        out.append(self.token())  # return

        self.i += 1
        compiled = self.compile_expression()
        if compiled:
            out.append(compiled)
        out.append(self.token())
        self.i += 1

        out.append('</returnStatement>')
        return '\n'.join(out)


    def compile_expression(self):
        out = ['<expression>' ]
        compiled = self.compile_term()
        if not compiled:
            return None
        out.append(compiled)

        if is_op(self.token()):
            out.append(self.token())
            self.i += 1
            out.append(self.compile_term())

        out.append('</expression>')
        return '\n'.join(out)


    def compile_term(self):
        out = ['<term>']
        if (is_contant(self.token())):
            out.append(self.token())
            self.i += 1
        elif (is_unary_op(self.token())):
            out.append(self.token())
            self.i += 1
            out.append(self.compile_term())
        elif (is_open_bracket(self.token())):
            out.append(self.token())
            self.i += 1
            out.append(self.compile_expression())
            if not is_close_bracket(self.token()):
                raise ValueError('missing closing ) for expression')
            out.append(self.token())
            self.i += 1
        elif (is_identifier(self.token())):
            look_ahead = self.look_ahead_token()
            if is_open_square_bracket(look_ahead):
                out.append(self.token()) # varName
                self.i += 1
                out.append(self.token()) # [
                self.i += 1
                out.append(self.compile_expression())
                if not is_close_square_bracket(self.token()):
                    raise ValueError('missing closing ] for expression')
                out.append(self.token()) # ]
                self.i += 1
            elif is_open_bracket(look_ahead) or is_dot(look_ahead):
                out.append(self.compile_subroutine_call())
            else:
                out.append(self.token()) # varName
                self.i += 1
        else:
            return None
        out.append('</term>')
        return '\n'.join(out)


    def compile_subroutine_call(self):
        out = [self.token()] # identifier
        self.i += 1
        if is_dot(self.token()):
            out.append(self.token()) # .
            self.i += 1
            out.append(self.token()) # identifier
            self.i += 1
        elif is_open_bracket(self.token()):
            pass
        else:
            raise ValueError('Invalid subroutine call syntax')

        out.append(self.token()) # (
        self.i += 1
        out.append(self.compile_expression_list())
        if not is_close_bracket(self.token()):
            raise ValueError('missing closing ) for expression list')
        out.append(self.token()) # )
        self.i += 1

        return '\n'.join(out)

    def compile_expression_list(self):
        out = ['<expressionList>']
        compiled = self.compile_expression()
        if compiled:
            out.append(compiled)

        while is_comma(self.token()):
            out.append(self.token()) # ,
            self.i += 1
            out.append(self.compile_expression())

        out.append('</expressionList>')
        return '\n'.join(out)


    def compile_class(self):
        out = ['<class>',
                self.tokens[0],
                self.tokens[1], # TODO: validate identifier
                self.tokens[2], # TODO: validate {
                ]

        self.i = 3
        while self.i < len(self.tokens):
            if(is_class_var_start(self.token())):
                out.append(self.compile_class_var())
            elif(is_subroutine_start(self.token())):
                out.append(self.compile_subroutine())
            elif is_close_brace(self.token()):
                break
            else:
                raise ValueError('Only class variable or subroutine declaration is allowed in a class')

        # validate & append closing }
        if not is_close_brace(self.token()):
            raise ValueError('missing closing } for class')
        out.append(self.token())
        self.i += 1

        out.append('</class>\n')
        return '\n'.join(out)


    def compile(self):
        if len(self.tokens) < 1 or self.tokens[0] != '<keyword> class </keyword>':
            raise ValueError('Program must start with a class declaration')
        return self.compile_class()


def is_class_var_start(token):
    return token in ('<keyword> field </keyword>', '<keyword> static </keyword>')

def is_subroutine_start(token):
    return token in ('<keyword> constructor </keyword>',
            '<keyword> function </keyword>', '<keyword> method </keyword>')

def is_open_bracket(token):
    return token in ('<symbol> ( </symbol>')

def is_close_bracket(token):
    return token in('<symbol> ) </symbol>')

def is_open_square_bracket(token):
    return token in ('<symbol> [ </symbol>')

def is_close_square_bracket(token):
    return token in ('<symbol> ] </symbol>')

def is_open_brace(token):
    return token in('<symbol> { </symbol>')

def is_close_brace(token):
    return token in('<symbol> } </symbol>')

def is_comma(token):
    return token == '<symbol> , </symbol>'

def is_dot(token):
    return token in ('<symbol> . </symbol>')

def is_unary_op(token):
    return token in { '<symbol> - </symbol>', '<symbol> ~ </symbol>' }

def is_op(token):
    return token in { '<symbol> + </symbol>',
            '<symbol> - </symbol>',
            '<symbol> * </symbol>',
            '<symbol> / </symbol>',
            '<symbol> &amp; </symbol>',
            '<symbol> | </symbol>',
            '<symbol> &lt; </symbol>',
            '<symbol> &gt; </symbol>',
            '<symbol> = </symbol>', }

def is_var_start(token):
    return token in ('<keyword> var </keyword>', )

def is_statement_start(token):
    return token in { '<keyword> let </keyword>',
            '<keyword> if </keyword>',
            '<keyword> else </keyword>',
            '<keyword> while </keyword>',
            '<keyword> do </keyword>',
            '<keyword> return </keyword>', }

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

