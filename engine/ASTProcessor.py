from data.db import db
from data.Estimator import Estimator
class ASTProcessor:
    def createEstimator(self, name, estimatorType, loss, lr = 0.001, optimizer = None, regularizer = None):
        db.connect()
        estimator = Estimator.create(name = name, type=estimatorType, loss=loss, lr=lr, optimizer=optimizer, regularizer=regularizer)