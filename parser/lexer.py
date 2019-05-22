import ply.lex as lex
import dill
from tokens.definitions import *
from tokens.data_types import *
from tokens.manipulations import *
from tokens.sql import *
tokens =  list(set().union(

            modelTokens,
            dataTypeTokens,
            trainTokens,
            trainProfileTokens,
            basicSQL
            ))

#regular expressions

t_ALPHA_NUMERIC = r'[a-zA-Z_][a-zA-Z_0-9]*'
 
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

with open("parser/lexer.dill", "wb") as f:
    dill.dump(lexer, f)