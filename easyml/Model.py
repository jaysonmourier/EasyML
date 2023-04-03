from tqdm import tqdm
import multiprocessing as mp

class Model:
    def __init__(self, model):
        self.model = model
        self.score = 0

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
