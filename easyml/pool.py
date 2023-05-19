from .model import Model

class Pool:

    test_size: float

    def __init__(self, test_size, *models):
        self.models = models

    def __load_models(self):
        for model in self.models:
            model.load()