import dill

class EstimatorManager:

    def __init__(self, clonable):
        self.clonable = clonable
        self.estimator_folder =  "engine/estimators/"



    def getPath(self, estimatorName):
        return self.estimator_folder + estimatorName + ".dill"
        

    def save(self, name, estimator):
        fname = self.getPath(name)
        with open(fname, "wb") as fp:
            dill.dump(estimator, fp)
    
        return estimator

    
    def load(self, name):
        
        fname = self.getPath(name)
        with open(fname, "rb") as fp:
            estimator = dill.load(fp)
        
        return estimator