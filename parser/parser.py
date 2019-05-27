import ply.yacc as yacc
import dill
from lexer import tokens

ESTIMATOR, TRAIN, TRAINING_PROFILE = range(3)
states = ['ESTIMATOR', 'TRAIN', 'TRAINING_PROFILE' ]
currentState = None
def p_create_model(p):
    '''expression : CREATE ESTIMATOR WORD TYPE WORD DELIMITER
                  | CREATE ESTIMATOR WORD TYPE WORD LOSS WORD DELIMITER
                  | CREATE ESTIMATOR WORD TYPE WORD LOSS WORD LEARNING_RATE FLOAT DELIMITER
                  | CREATE ESTIMATOR WORD TYPE WORD LOSS WORD LEARNING_RATE FLOAT OPTIMIZER WORD REGULARIZER WORD DELIMITER'''
    global currentState
    currentState = ESTIMATOR
    p[0] = "A create ESTIMATOR"
    print( f" p[0] = {p[0]}" )

    length = len(p)

    name = p[3]
    estimatorType = p[5]
    loss = 'MSE'
    lr = 0.001
    optimizer = None
    regularizer = None

    if length > 7:
        loss = p[7]
    if length > 9:
        lr = p[9]
    if length >= 11:
        optimizer = p[11]
        regularizer = p[13]

    




def p_SQL(p):
    'expression : SQL DELIMITER'
    p[0] = p[1]
    print( f" p[0] = {p[0]}" )

def p_training_profile(p):
    '''expression : CREATE TRAINING_PROFILE WORD BATCH_SIZE INT EPOCH INT SHUFFLE BOOL'''
    p[0] = "A training profile"
    print( f" p[0] = {p[0]}" )

def p_error(t):
    print('Syntax error at "%s"' % t.value if t else 'NULL')
    global current_state
    current_state = None

parser = yacc.yacc()

# with open("parser/parser.dill", "wb") as f:
#     dill.dump(parser, f)


# data = '''
# CREATE ESTIMATOR modName
# CREATE ESTIMATOR modName
# REGULARIZER r1
# TYPE LR;
# CREATE ESTIMATOR modName TYPE LR REGULARIZER r1;
# [SELECT * FROM EMP];
# '''

# parser.parse(data)

if __name__ == "__main__":

    userInput  = ''
    prevInput = ''
    while True:
        userInput = input().strip()

        if userInput == 'exit':
            break
        
        if userInput[-1] != ';':
            prevInput += ' ' + userInput
            continue
        
        data = prevInput + userInput
        print(f"parsing {data}")
        p = parser.parse(data)
        print(p)

        prevInput = ''

    pass