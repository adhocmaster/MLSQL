from sklearn.linear_model import LinearRegression
import dill

class LR:

    def create(self, name):
        estimator = LinearRegression()
        return self.save(name, estimator)


    def save(self, name, estimator):
        fname = "engine/estimators/" + name + ".dill"
        with open(fname, "wb") as fp:
            dill.dump(estimator, fp)
    
        return estimator

    
    def load(self, name):
        
        fname = "engine/estimators/" + name + ".dill"
        with open(fname, "rb") as fp:
            estimator = dill.load(fp)
        
        return estimator


    def train(self, name, X, y):
                
        estimator = self.load(name).fit(X, y)
        return self.save(name, estimator)

    
    def predict(self, name, X):
        return self.load(name).predict(X)
