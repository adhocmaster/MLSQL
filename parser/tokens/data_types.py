dataTypeTokens = [
    'ALPHA_NUMERIC',
    'FLOAT',
    'INTEGER'
]

#regular expressions

t_ALPHA_NUMERIC = r'[a-zA-Z_][a-zA-Z_0-9]*'
t_FLOAT = r'[0-9]+\.[0-9]*|[0-9]*\.[0-9]+'
t_INTEGER = r'[0-9]+'