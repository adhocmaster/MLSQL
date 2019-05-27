from data.db import db
import datetime
from data.Estimator import Estimator
from engine.LR import LR

class ASTProcessor:

    def __init__(self):
        pass
    
    def createEstimator(self, name, estimatorType, loss, lr = 0.001, optimizer = None, regularizer = None):

        print(f"""name = {name}, 
                estimatorType={estimatorType}, 
                loss={loss}, 
                lr={lr}, 
                optimizer={optimizer}, 
                regularizer={regularizer}
                """)
        with db:
            estimator = Estimator.create(name = name, 
                                        estimatorType=estimatorType, 
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
    
