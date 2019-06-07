projectFolder = 'F:/myProjects/tfKeras/UCSC/CMPS203/MLSQL/'
import logging, sys, math,os
sys.path.append(str(projectFolder))

from data.db import db
from EstimatorMeta import EstimatorMeta
from TrainingProfile import TrainingProfile

if __name__ == "__main__":

    tables = [EstimatorMeta, TrainingProfile]
    db.connect()
    db.drop_tables(tables)
    db.create_tables(tables)
    db.close()
    
    pass