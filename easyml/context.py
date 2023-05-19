from .dataset import Dataset
from .pool import Pool
from .model import Model
from .log import info

from joblib import dump

class Context:

    std: bool = False

    def __init__(self, dataset: Dataset, pool: Pool, model: Model):
        self.dataset = dataset
        self.pool = pool
        self.model = model
        self.dataset.split()

    def train_model(self):
        info("Training...")
        self.model.train(self.dataset.Xtrain, self.dataset.Ytrain)

    def export_model(self, output):
        dump(self.model.model, output)