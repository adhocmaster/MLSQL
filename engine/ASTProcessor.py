from peewee import *
from data.db import db
import datetime
from data.Estimator import Estimator
from data.TrainingProfile import TrainingProfile
from engine.LR import LR
import pprint

class ASTProcessor:

    def __init__(self):

        self.pp = pprint.PrettyPrinter(indent=3)
        pass

    def hasDB(self, dbURL):
        
        estimatorDb = self.getDB(dbURL)
        if estimatorDb.connect():
            return True
        return False
    
    def getDB(self, dbURL):
        return SqliteDatabase(dbURL)
    
    def getEstimator(self, name):
        with db:
            return Estimator.select().where(Estimator.name == name).get()
    
    def getTrainingProfile(self, name):
        with db:
            return TrainingProfile.select().where(TrainingProfile.name == name).get()
    
    
    def createEstimator(self, name, estimatorType, formula = None, loss = None, lr = 0.001, optimizer = None, regularizer = None):

        print(f"""name = {name}, 
                estimatorType={estimatorType}, 
                formula={formula}, 
                loss={loss}, 
                lr={lr}, 
                optimizer={optimizer}, 
                regularizer={regularizer}
                """)
        with db:
            estimator = Estimator.create(name = name, 
                                        estimatorType=estimatorType, 
                                        formula=formula, 
                                        loss=loss, 
                                        lr=lr, 
                                        optimizer=optimizer, 
                                        regularizer=regularizer)

            if estimatorType == "LR":
                LR().create(name)
            
            else:
                estimator.delete()
                raise Exception(f"unrecognized estimator type{estimatorType}")

            estimator.isAvailable = True
            estimator.save()
            return estimator

    
    def createTrainingProfile(self, name, sql, validationSplit, batchSize, epoch, shuffle):

        print(f"""name={name},
                source={sql},
                validation_split={validationSplit},
                batch_size={batchSize},
                epoch={epoch},
                shuffle={shuffle}""")

        with db:
            trainingProfile = TrainingProfile.create(name=name,
                                                    source=sql,
                                                    validation_split=validationSplit,
                                                    batch_size=batchSize,
                                                    epoch=epoch,
                                                    shuffle=shuffle
                                                    )
        
            return trainingProfile
    

    def train(self, currentDB, estimatorName, trainingProfileName):

        try:
            estimator = self.getEstimator(estimatorName)
            trainingProfile = self.getTrainingProfile(trainingProfileName)

            self.pp.pprint(estimator)
            self.pp.pprint(trainingProfile)

            if estimator.estimatorType == 'LR':
                pass
                


        except Estimator.DoesNotExist as e:
            raise Exception(f"{estimatorName} estimator does not exist ({e}).")

        except TrainingProfile.DoesNotExist as e:
            raise Exception(f"{trainingProfileName} estimator does not exist ({e}.")
    
    
