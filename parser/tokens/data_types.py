dataTypeTokens = [
    'ALPHA_NUMERIC',
    'FLOAT',
    'INTEGER'
]

#regular expressions

t_ALPHA_NUMERIC = r'[a-zA-Z_][a-zA-Z_0-9]*'
t_FLOAT = r'[0-9]+\.[0-9]*|[0-9]*\.[0-9]+'
t_INTEGER = r'[0-9]+'
def t_TRAINING_PROFILE(t):
    r'(TRAINING PROFILE)'
    t.type = 'TRAINING_PROFILE'
    print("I am in t_TRAINING_PROFILE")
    return t