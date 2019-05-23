import ply.lex as lex
from ply.lex import TOKEN
import dill
from tokens.manipulations import *
from tokens.sql import *
from tokens.definitions import *
from tokens.data_types import *


keywords = list(set().union(
            modelTokens,
            trainTokens,
            trainProfileTokens
            ))
tokens =  list(set().union(

            dataTypeTokens,
            basicSQL

            )) + keywords

print(tokens)

def t_SQL(t):
    r'\[\s*[SELECT,UPDATE]+[^\]]*\]'
    t.value = t.value[1:len(t.value)].strip()
    return t

# keywords rule
reKyewords = "(" + "|".join(keywords) + ")+[ \n\t]{1}"
@TOKEN(reKyewords)
def t_KEYWORD(t):
    print("I am in t_KEYWORD")
    t.value = t.value.strip()
    t.type = t.value
    return t
 
# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_TRAINING_PROFILE(t):
    r'TRAINING[_ \t\n]+PROFILE'
    t.type = 'TRAINING_PROFILE'
    print("I am in t_TRAINING_PROFILE")
    return t
# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

with open("parser/lexer.dill", "wb") as f:
    dill.dump(lexer, f)