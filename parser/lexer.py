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
    r'\[\s*[SELECT,UPDATE]+[^\];]*\]'
    t.value = t.value[1:len(t.value)-1].strip()
    return t

# keywords rule
reKyewords = "(" + "|".join(keywords) + ")+[ \n\t]{1}"
@TOKEN(reKyewords)
def t_KEYWORD(t):
    print(f"found keyword: {t.value}")
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
    t.value = 'TRAINING_PROFILE'
    print("I am in t_TRAINING_PROFILE")
    return t


def t_LEARNING_RATE(t):
    r'LEARNING[_ \t\n]+RATE'
    t.type = 'LEARNING_RATE'
    t.value = 'LEARNING_RATE'
    print("I am in t_LEARNING_RATE")
    return t

def t_VALIDATION_SPLIT(t):
    r'VALIDATION[_ \t\n]+SPLIT'
    t.type = 'VALIDATION_SPLIT'
    t.value = 'VALIDATION_SPLIT'
    print("I am in t_VALIDATION_SPLIT")
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