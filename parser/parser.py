import ply.yacc as yacc
import dill
from lexer import tokens

MODEL, TRAIN, TRAINING_PROFILE = range(3)
states = ['MODEL', 'TRAIN', 'TRAINING_PROFILE' ]
currentState = None
def p_create_model(p):
    '''expression : CREATE MODEL WORD TYPE WORD REGULARIZER WORD DELIMITER'''
    global currentState
    currentState = MODEL
    p[0] = "A create model"
    print( f" p[0] = {p[0]}" )

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
# CREATE MODEL modName
# CREATE MODEL modName
# REGULARIZER r1
# TYPE LR;
# CREATE MODEL modName TYPE LR REGULARIZER r1;
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