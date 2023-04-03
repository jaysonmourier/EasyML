from textx import metamodel_from_str
from . import log, grammar, Dataset, Model

from sklearn.svm import SVC
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import GradientBoostingClassifier

class ContextBuilder:

    dataset: Dataset
    model: Model
    test_size: float

    def __init__(self, filepath: str):
        self.metamodel = metamodel_from_str(grammar)
        
        try:
            self.model = self.metamodel.model_from_file(file_name=filepath)
        except Exception:
            log.fatal(1, "Error during initialization. Check the validity of the script name.")
        
        self.load_dataset()
        self.load_features_and_target()
        self.load_test_size()
        self.dataset.split(self.test_size)
        self.load_model()
        self.model.train(self.dataset.Xtrain, self.dataset.Ytrain)
        self.model.accuracy(self.dataset.Xtest, self.dataset.Ytest)
        log.info("Total score: " + str(self.model.score))

    def load_dataset(self):
        log.info("Loading dataset...")

        if not self.model.use_csv.csv_file:
            log.fatal(1, "No csv file provided")

        default_values = {
            'sep': ',',
            'header': 0,
            'index_col': None,
            'names': None,
            'encoding': 'utf-8',
            'na_values': ""
        }

        def get_value(option_name, textx_obj):
            if textx_obj is None:
                return default_values[option_name]
            return getattr(textx_obj, option_name)

        options = {opt: get_value(opt, getattr(self.model.use_csv.options, opt, None)) for opt in default_values}

        self.dataset = Dataset(self.model.use_csv.csv_file, **options)
        self.dataset.load()

    def load_features_and_target(self):
        log.info("Loading features and target...")
        
        if self.model.features is None:
            features = []
        else:
            features = self.model.features.feature_names

        if self.model.target is None:
            target = ""
        else:
            target = self.model.target.target_column
        
        self.dataset.features = features
        self.dataset.target = target

    def load_test_size(self):
        log.info("Loading size of testing set...")
        
        test_size = self.model.test.test if self.model.test is not None else 20

        if test_size < 0 or test_size > 99:
            test_size = 20

        self.test_size = test_size / 100

    def load_model(self):
        log.info("Loading model...")

        model_name = self.model.model.model_type if self.model.model.model_type is not None else "SVM"

        m = None

        if model_name == "SVM":
            m = SVC()
        elif model_name == "XGBoost":
            m = GradientBoostingClassifier()
        elif model_name == "Linear":
            m = LinearRegression()

        self.model = Model(m)