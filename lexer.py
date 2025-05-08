import ply.lex as lex

# List of token names
tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'MUL',
    'DIV',
    'LPAREN',
    'RPAREN',
)

# Regular expression rules for simple tokens
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_MUL     = r'\*'
t_DIV     = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'

# A rule for numbers (integers and decimals)
def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t

# Ignoring spaces and tabs
t_ignore = ' \t'

# Error handling rule
def t_error(t):
    print(f"[Lexer Error] Illegal character '{t.value[0]}' at position {t.lexpos}")
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()

# Optional test function
if __name__ == "__main__":
    while True:
        try:
            expression = input("Enter expression > ")
        except EOFError:
            break
        lexer.input(expression)
        for tok in lexer:
            print(tok)
