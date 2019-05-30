import re
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
class FormulaProcessor:

    def __init__(self, formula):

        self.formula = formula
        yX = self.stringFilter(re.split(r'\~+', self.formula))
        
        if len(yX) != 2:
            raise Exception(f"{formula} does not have $a~b$ format")

        self.fieldY = yX[0]
        self.formulaX = yX[1]
        self.fieldsX = self.stringFilter(re.split(r'\++', self.formulaX))

        pass
    

    def stringFilter(self, strings):

        filtered = []

        for s in strings:
            s = s.strip()
            if len(s) > 0:
                filtered.append(s)
        
        return filtered
    

    def getDataFromSQLDB(self, dataDb, trainingProfile, randomSeed = 42):
        """returns (XTrain, XValidation, yTrain, yValidation) training and validation X,y, does not support categorical data yet"""

        df = pd.read_sql(trainingProfile.source, dataDb.connection())

        X = df[self.fieldsX].values
        y = df[self.fieldY].values
        
        if trainingProfile.validation_split <= 0:
            return X, None, y, None

        return train_test_split(X, y, test_size = trainingProfile.validation_split , random_state = randomSeed)
