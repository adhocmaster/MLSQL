from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score
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
        self.train(name, Xtrain, Xtest)
        dic['training_accuracy'] = accuracy_score(yTrain, self.predict(name, Xtrain))
        if Xtest is not None:
            dic['validation_accuracy'] = accuracy_score(yTest, self.predict(name, Xtest))
        return dic
        

    def train(self, name, X, y):
                
        estimator = self.load(name).fit(X, y)
        return self.save(name, estimator)

    
    def predict(self, name, X):
        return self.load(name).predict(X)

    
