from sklearn.linear_model import LinearRegression
from sklearn.metrics import median_absolute_error
import dill
from engine.EstimatorManager import EstimatorManager

class LRManager(EstimatorManager):

    def __init__(self):
        super(LRManager,self).__init__()


    def create(self, name):
        estimator = LinearRegression()
        return self.save(name, estimator)

    def trainValidate(self, name, Xtrain, Xtest, yTrain, yTest):

        dic = {}
        self.train(name, Xtrain, yTrain)
        dic['training_mae'] = median_absolute_error(yTrain, self.predict(name, Xtrain))
        if Xtest is not None:
            dic['validation_mae'] = median_absolute_error(yTest, self.predict(name, Xtest))
        return dic
        

    def train(self, name, X, y):
                
        estimator = self.load(name)
        estimator.fit(X, y)
        return self.save(name, estimator)

    
    def predict(self, name, X):
        estimator = self.load(name)
        pred =  estimator.predict(X)
        return pred

    
