from peewee import *
from data.db import db
import datetime
from data.EstimatorMeta import EstimatorMeta
from data.TrainingProfile import TrainingProfile
from engine.LRManager import LRManager
from engine.FormulaProcessor import FormulaProcessor
import pprint

class ASTProcessor:

    def __init__(self):

        self.pp = pprint.PrettyPrinter(indent=3)
        pass

    def hasDB(self, dbURL, dbEngine='sqlite3'):
        
        if dbEngine == 'sqlite3':
            try:
                open(dbURL, 'r')
                return True
            except FileNotFoundError:
                return False
        
        return False
    
    def getDB(self, dbURL):
        return SqliteDatabase(dbURL)
    
    def getEstimatorMeta(self, name):
        with db:
            return EstimatorMeta.select().where(EstimatorMeta.name == name).get()
    
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
            estimatorMeta = EstimatorMeta.create(name = name, 
                                        estimatorType=estimatorType, 
                                        formula=formula, 
                                        loss=loss, 
                                        lr=lr, 
                                        optimizer=optimizer, 
                                        regularizer=regularizer)
            
            if estimatorType == "LR":
                LRManager().create(name)
            
            else:
                estimatorMeta.delete()
                raise Exception(f"unrecognized estimator type{estimatorType}")

            estimatorMeta.isAvailable = True
            estimatorMeta.trainable = True
            estimatorMeta.save()
            return estimatorMeta

    
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
            #1 Check DB
            if currentDB is None:
                raise Exception(f"no Database chosen to draw training data from. hint: [USE DBUrl;]")
            
            #2 Check Estimator
            estimatorMeta = self.getEstimatorMeta(estimatorName)
            if estimatorMeta.trainable == False:
                raise Exception(f"Estimator {estimatorMeta.name} is not trainable. Try cloning?")

            #3 Get training profile
            trainingProfile = self.getTrainingProfile(trainingProfileName)

            #4 Prepared data with formula processor and Train
            return self.prepareDataAndTrain(currentDB, estimatorMeta, trainingProfile)
                       
        except EstimatorMeta.DoesNotExist as e:
            raise Exception(f"{estimatorName} estimator does not exist ({e}).")

        except TrainingProfile.DoesNotExist as e:
            raise Exception(f"{trainingProfileName} estimator does not exist ({e}.")
    
    
    def prepareDataAndTrain(self, currentDB, estimatorMeta, trainingProfile):

        #1 Prepared data with formula processor
        formulaProcessor = FormulaProcessor(estimatorMeta.formula)
        XTrain, XValidation, yTrain, yValidation = formulaProcessor.getDataFromSQLDB(currentDB, trainingProfile)

        self.pp.pprint("Running training with following configurations.")
        self.pp.pprint(estimatorMeta)
        self.pp.pprint(trainingProfile)

        #2 Train estimator with the data.
        if estimatorMeta.estimatorType == 'LR':
            estimatorManager = LRManager()
            accuracyDic = estimatorManager.trainValidate(estimatorMeta.name, XTrain, XValidation, yTrain, yValidation)
            self.postTrain(estimatorMeta)
            self.pp.pprint(accuracyDic)
            return accuracyDic

    
    def postTrain(self, estimatorMeta, stillTrainable = False):
        estimatorMeta.trainable = stillTrainable
        estimatorMeta.save()


    def cloneModel(self, fromName, toName, keepWeights = False):

        fromEstimatorMeta = self.getEstimatorMeta(fromName)
        
        if fromEstimatorMeta.estimatorType == 'LR':
            estimatorManager = LRManager()

            if estimatorManager.clonable == False:
                raise Exception(f"{fromEstimatorMeta.estimatorType} estimators cannot be cloned")
            else:
                estimatorMeta = self.createEstimator(name=toName,
                                                    estimatorType=fromEstimatorMeta.estimatorType,
                                                    formula=fromEstimatorMeta.formula,
                                                    loss=fromEstimatorMeta.loss,
                                                    lr=fromEstimatorMeta.lr,
                                                    optimizer=fromEstimatorMeta.optimizer,
                                                    regularizer=fromEstimatorMeta.regularizer                                
                                                    )
                return estimatorMeta
        pass
    
