import ply.lex as lex
import dill
tokens = [
    'ALPHA_NUMERIC',
    'CREATE',
    'MODEL',
    'REGULARIZER',
    'TYPE'
]

#regular expressions

t_ALPHA_NUMERIC = r'[a-zA-Z_][a-zA-Z_0-9]*'
def t_CREATE(t):
    r'CREATE'
    return t
def t_MODEL(t):
    r'MODEL'
    return t
def t_REGULARIZER(t):
    r'REGULARIZER'
    return t
def t_TYPE(t):
    r'TYPE'
    return t
    
 
# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

with open("parser/testLexer.dill", "wb") as f:
    dill.dump(lexer, f)