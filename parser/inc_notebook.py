projectFolder = 'F:/myProjects/tfKeras/UCSC/CMPS203/MLSQL/'
import logging, sys, math,os

currentFolder = os.path.abspath('')
try:
    sys.path.remove(str(currentFolder))
except ValueError: # Already removed
    pass

sys.path.append(str(projectFolder))
