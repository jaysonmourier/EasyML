from tqdm import tqdm
import multiprocessing as mp

from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import GradientBoostingClassifier

class Model:
    model = None
    score: float

    def __init__(self, name):
        self.name = name
        self.score = 0
        self.__load_model()

    def train(self, X, y):
        self.model.fit(X, y)

    def accuracy(self, Xtest, ytest):
        self.score = self.model.score(Xtest, ytest)

    def best_params(self):
        return self.model.best_params_

    def best_score(self):
        return self.model.best_score_

    def track_progress(self, batches):
        pbar = tqdm(total=len(batches))
        for i, _ in enumerate(batches):
            pbar.update()
        pbar.close()

    def load(self):
        self.__load_model()

    def __str__(self):
        return self.name

    def __load_model(self):
        if self.name == "SVM":
            self.model = SVC()
        elif self.name == "Logistic":
            self.model = LogisticRegression()
        else:
            self.model = GradientBoostingClassifier()

class SVM(Model):
    pass

class LR(Model):
    pass

class XGB(Model):
    pass