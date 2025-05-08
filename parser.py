import ply.yacc as yacc
from lexer import tokens  # import tokens from lexer.py

# AST node structure
class BinOp:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class Num:
    def __init__(self, value):
        self.value = value

class Neg:
    def __init__(self, expr):
        self.expr = expr

# Precedence rules
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MUL', 'DIV'),
    ('right', 'UMINUS'),
)

# Grammar rules
def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression MUL expression
                  | expression DIV expression'''
    p[0] = BinOp(p[1], p[2], p[3])

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = Num(p[1])

def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_expression_uminus(p):
    'expression : MINUS expression %prec UMINUS'
    p[0] = Neg(p[2])

def p_error(p):
    if p:
        print(f"[Syntax Error] Unexpected token '{p.value}' at position {p.lexpos}")
    else:
        print("[Syntax Error] Unexpected end of input")


# Build the parser
parser = yacc.yacc()

# Optional test runner
if __name__ == "__main__":
    while True:
        try:
            expr = input("Enter expression > ")
        except EOFError:
            break
        if not expr:
            continue
        result = parser.parse(expr)
        print(result)
