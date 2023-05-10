from .context import Context
from .log import fatal, info
from .model import Model
from .pool import Pool
from .dataset import Dataset

from textx import metamodel_from_str
import pandas as pd

class ContextBuilder:

    context: Context = None
    dataset: Dataset = None
    pool: Pool
    _model: Model
    features: list
    target: list
    std: bool = False

    def __init__(self, grammar_path: str, dsl_path: str):
        try:
            self.metamodel = metamodel_from_str(grammar_path)
            self.model = self.metamodel.model_from_file(file_name=dsl_path)
        except Exception as e:
            print(e)
            fatal(1, "Error during initialization. Check the validity of the script name.")

        self.hydrate_dataset()
        self.hydrate_features()
        self.hydrate_target()
        self.hydrate_test_size()
        self.hydrate_pool()
        self.extract_std()
        self.dataset.features = self.features
        self.dataset.target = self.target
        self.dataset.test_size = self.test_size
        self.context = Context(self.dataset, self.pool, self._model)
        self.context.std = self.std

    def hydrate_dataset(self):
        info("Load dataset...")
        sep = ","
        header = 0
        index_col = None
        names = None
        encoding = "utf-8"
        na_values = ""

        if not self.__object_exists(self.model, "load_csv.csv_path"):
            fatal(1, "Please, provide a csv file.")

        if self.__object_exists(self.model, "load_csv.options.sep"):
            sep = self.model.load_csv.options.sep

        if self.__object_exists(self.model, "load_csv.options.header"):
            header = self.model.load_csv.options.header

        if self.__object_exists(self.model, "load_csv.options.index_col"):
            index_col = self.model.load_csv.options.index_col

        if self.__object_exists(self.model, "load_csv.options.names"):
            names = self.model.load_csv.options.names

        if self.__object_exists(self.model, "load_csv.options.encoding"):
            encoding = self.model.load_csv.options.encoding

        if self.__object_exists(self.model, "load_csv.options.na_values"):
            na_values = self.model.load_csv.options.na_values

        path = self.model.load_csv.csv_path

        try:
            self.dataset = Dataset(
                path,
                sep,
                header,
                index_col,
                names,
                encoding,
                na_values
            )
        except Exception as e:
            fatal(1, "Unable to load dataset.")

    def hydrate_features(self):
        info("Load features...")
        if not self.__object_exists(self.model, "features_list.features_name"):
            fatal(1, "Please, provide a list of features")
        self.features = [feature.feature_name for feature in self.model.features_list.features_name]
    
    def hydrate_target(self):
        info("Load target...")
        if not self.__object_exists(self.model, "target.target_name"):
            fatal(1, "Please, provide a target name.")

        self.target = self.model.target.target_name

        if self.target in self.features:
            self.features.remove(self.target)

        if len(self.features) < 1:
            fatal(1, "Not enough features for training.")
        
        if not set([self.target] + self.features).issubset(set(self.dataset.dataframe.columns)):
            fatal(1, "One or more specified variables are not present in the dataset.")

    def hydrate_pool(self):
        info("Creating pool...")
        self.models_name = set()
        self.models = list()
        if not self.__object_exists(self.model, "model.model_name"):
            fatal(1, "Please, provide a valid model name.")

        self.models_name.add(self.model.model.model_name)
        self._model = Model(self.model.model.model_name)

        if self.__object_exists(self.model, "models.models_list"):
            self.models_name.update([*self.model.models.models_list])

        for model in self.models_name:
            self.models.append(Model(model))

        self.pool = Pool(self.test_size, *self.models)

    def hydrate_test_size(self):
        info("Exctract test size parameter...")
        if not self.__object_exists(self.model, "model.option.test_size"):
            self.test_size = 0.2
            return
        
        self.test_size = self.model.model.option.test_size

        if self.test_size < 0 or self.test_size > 99:
            self.test_size = 0.2
        else:
            self.test_size /= 100

    def extract_std(self):
        if self.model.model.std is not None:
            self.std = True
        
    def get_context(self):
        info("Building context...")
        return self.context
    
    def __object_exists(self, obj, path):
        try:
            parts = path.split('.')
            for part in parts:
                obj = getattr(obj, part)
            return True
        except AttributeError:
            return False
