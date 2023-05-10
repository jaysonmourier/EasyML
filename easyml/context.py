from .dataset import Dataset
from .pool import Pool
from .model import Model

class Context:

    std: bool = False

    def __init__(self, dataset: Dataset, pool: Pool, model: Model):
        self.dataset = dataset
        self.pool = pool
        self.model = model

    def train_model(self):
        pass