import ply.lex as lex
import dill
tokens = (
    'CREATE',
    'MODEL','STRING',
    'TYPE', 
    'REGULARIZER'
)

#regular expressions

t_CREATE = r'CREATE'
t_MODEL = r'MODEL'
t_REGULARIZER = r'REGULARIZER'

def t_STRING(t):
    r'\w+'
    t.value = t
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