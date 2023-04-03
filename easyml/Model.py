class Model:
    def __init__(self, model):
        self.model = model
        self.score = 0

    def train(self, X, y):
        self.model.fit(X, y)

    def accuracy(self, Xtest, ytest):
        self.score = self.model.score(Xtest, ytest)
