modelTokens = [
    'CREATE',
    'MODEL',
    'ESTIMATOR',
    'REGULARIZER',
    'TYPE',
    'FORMULA',
    'FORMULA_OPERATOR'
]

trainProfileTokens = [
    'CREATE',
    'AND'
    'TRAINING_PROFILE',
    'BATCH_SIZE',
    'EPOCH',
    'SUFFLE',
    'WITH'
]

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