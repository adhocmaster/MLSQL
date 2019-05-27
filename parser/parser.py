import ply.yacc as yacc
import dill
from lexer import tokens

MODEL, TRAIN, TRAINING_PROFILE = range(3)
states = ['MODEL', 'TRAIN', 'TRAINING_PROFILE' ]
currentState = None
def p_create_model(p):
    'expression : CREATE MODEL ALPHA_NUMERIC'
    global currentState
    currentState = MODEL
    p[0] = "I can be anything"
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
# '''

# parser.parse(data)

if __name__ == "__main__":

    userInput  = ''

    while userInput != 'exit':
        userInput = input().strip()
        p = parser.parse(userInput)
        print(p)

    pass