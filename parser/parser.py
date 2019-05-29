projectFolder = 'F:/myProjects/tfKeras/UCSC/CMPS203/MLSQL/'
import logging, sys, math,os

# currentFolder = os.path.abspath('')
# try:
#     sys.path.remove(str(currentFolder))
# except ValueError: # Already removed
#     pass

sys.path.append(str(projectFolder))

# logging.basicConfig(
#     level = logging.DEBUG,
#     filename = "parselog.txt",
#     filemode = "w",
#     format = "%(filename)10s:%(lineno)4d:%(message)s"
# )
# log = logging.getLogger()

import ply.yacc as yacc
import dill
from lexer import tokens
from engine.ASTProcessor import ASTProcessor
from data import Estimator
from data.TrainingProfile import TrainingProfile

ASTProcessor = ASTProcessor()
ESTIMATOR, TRAIN, TRAINING_PROFILE, USE = range(4)
states = ['ESTIMATOR', 'TRAIN', 'TRAINING_PROFILE', 'USE' ]
currentState = None
currentDb = None #database connector instance, not url.


def p_create_model(p):
    '''exp : CREATE ESTIMATOR WORD TYPE WORD FORMULA FORMULA_EXP DELIMITER
            | CREATE ESTIMATOR WORD TYPE WORD FORMULA FORMULA_EXP LOSS WORD DELIMITER
            | CREATE ESTIMATOR WORD TYPE WORD FORMULA FORMULA_EXP LOSS WORD LEARNING_RATE FLOAT DELIMITER
            | CREATE ESTIMATOR WORD TYPE WORD FORMULA FORMULA_EXP LOSS WORD LEARNING_RATE FLOAT OPTIMIZER WORD REGULARIZER WORD DELIMITER'''
    global currentState
    currentState = ESTIMATOR

    length = len(p)

    name = p[3]
    estimatorType = p[5]
    loss = None
    lr = 0.001
    optimizer = None
    regularizer = None

    lastPos = 5
    if length > 7:
        lastPos += 2
        formula = p[lastPos]

    if length > lastPos + 2:
        lastPos += 2
        loss = p[lastPos]

    if length > lastPos + 2:
        lastPos += 2
        lr = p[lastPos]

    if length > lastPos + 2:
        lastPos += 2
        optimizer = p[lastPos]
        lastPos += 2
        regularizer = p[lastPos]

    try:
        estimator = ASTProcessor.createEstimator(name=name, 
                                                estimatorType=estimatorType, 
                                                formula=formula, 
                                                loss=loss, 
                                                lr=lr, 
                                                optimizer=optimizer, 
                                                regularizer=regularizer)
        print(f"Created estimator with name {name}")
    except Exception as e:
        printError(e)
    
    pass

def p_training_profile(p):
    '''exp : CREATE TRAINING_PROFILE WORD WITH SQL DELIMITER
                | CREATE TRAINING_PROFILE WORD WITH SQL AND VALIDATION_SPLIT FLOAT DELIMITER
                | CREATE TRAINING_PROFILE WORD WITH SQL AND VALIDATION_SPLIT FLOAT BATCH_SIZE INT EPOCH INT DELIMITER
                | CREATE TRAINING_PROFILE WORD WITH SQL AND VALIDATION_SPLIT FLOAT BATCH_SIZE INT EPOCH INT SHUFFLE BOOL DELIMITER'''
    global currentState
    currentState = TRAINING_PROFILE
    length = len(p)

    name = p[3]
    sql = p[5]
    validationSplit = 0
    batchSize = 0
    epoch = 0
    shuffle = False

    if length > 7:
        validationSplit = p[8]
    if length > 10:
        batchSize = p[10]
        epoch = p[12]
    if length > 14:
        shuffle = p[14]
    
    try:
        profile = ASTProcessor.createTrainingProfile(name=name, sql=sql, validationSplit=validationSplit, batchSize=batchSize, epoch=epoch, shuffle=shuffle)
        print(f"Created training profile with name {name}")
    except Exception as e:
        printError(e)
    pass


def p_train(p):
    '''exp : TRAIN WORD WITH TRAINING_PROFILE WORD'''
    global currentState
    currentState = TRAIN

    estimatorName = p[2]
    trainingProfileName = p[5]



def p_use_database(p):
    'exp : USE WORD DELIMITER'
    global currentDb
    currentDbURL = p[2]

    if ASTProcessor.hasDB(currentDbURL):
        print(f"selected {currentDbURL}")
        currentDb = ASTProcessor.getDB(currentDbURL)
    else:
        printError(f'{currentDbURL} does not exist in the database engine.')
        currentDb = None
    
    pass

def p_SQL(p):
    'exp : SQL DELIMITER'
    p[0] = p[1]
    print( f" p[0] = {p[0]}" )

    pass


def p_error(t):
    printError('Syntax error at "%s"' % t.value if t else 'NULL')
    global current_state
    current_state = None
    pass

def printError(e):
    print("Operation failed due to:")
    print(e)

# parser = yacc.yacc(debug=True, errorlog=log)
parser = yacc.yacc(debug=True)

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

        if len(userInput) == 0:
            continue

        
        if userInput[-1] != ';':
            prevInput += ' ' + userInput
            continue
        

        data = prevInput + userInput
        print(f"parsing {data}")
        p = parser.parse(data)
        # print(p)

        prevInput = ''

    pass