dataTypeTokens = [
    'WORD',
    'FLOAT',
    'INT',
    'DELIMITER',
    'BOOL'
]

#regular expressions

t_WORD = r'[a-zA-Z_][a-zA-Z_0-9]*'
t_FLOAT = r'[0-9]+\.[0-9]*|[0-9]*\.[0-9]+'
t_INT = r'[0-9]+'
t_BOOL = r'true!false'
t_DELIMITER = r';'