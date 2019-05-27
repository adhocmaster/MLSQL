projectFolder = 'F:/myProjects/tfKeras/UCSC/CMPS203/MLSQL/'
import logging, sys, math,os

currentFolder = os.path.abspath('')
try:
    sys.path.remove(str(currentFolder))
except ValueError: # Already removed
    pass

sys.path.append(str(projectFolder))

from parser.lexer import *
from parser.parser import *
import ply.yacc as yacc
import dill

parser = yacc.yacc()

# with open("parser/parser.dill", "wb") as f:
#     dill.dump(parser, f)

data = '''
CREATE MODEL modName
'''

parser.parse(data)