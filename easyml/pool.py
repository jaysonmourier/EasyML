from .model import Model

class Pool:

    test_size: float

    def __init__(self, test_size, *models):
        self.models = models
        self.__load_models()

    def __load_models(self):
        for model in self.models:
            model.load()