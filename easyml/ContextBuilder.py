from textx import metamodel_from_str

from easyml.PDFBuilder import plot
from . import log, grammar, Dataset, Model
from joblib import dump

from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder

from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import GradientBoostingClassifier

import numpy as np
import pandas as pd

class ContextBuilder:

    dataset: Dataset
    algo: Model
    test_size: float

    def __init__(self, filepath: str):
        self.metamodel = metamodel_from_str(grammar)
        
        try:
            self.model = self.metamodel.model_from_file(file_name=filepath)
        except Exception:
            log.fatal(1, "Error during initialization. Check the validity of the script name.")
        
        
        self.load_dataset()
        self.load_features_and_target()
        self.extract_features()
        self.convert_target_string_columns_to_numeric()
        self.convert_features_string_columns_to_numeric()
        self.load_test_size()
        self.dataset.split(self.test_size)
        self.load_std()
        self.load_model()
        self.algo.train(self.dataset.Xtrain, self.dataset.Ytrain)
        self.algo.accuracy(self.dataset.Xtest, self.dataset.Ytest)
        print(self.model.features.feature_names)
        #exit()
        #plot(self.model.use_csv.csv_file, self.model.features.feature_names, self.model.model.model_type ,self.model.target.target_column,self.test_size)
        log.info("Total score: " + str(self.algo.score))
        log.info("Best params: " + str(self.algo.best_params()))
        log.info("Best score: " + str(self.algo.best_score()))

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

    def extract_features(self):
        log.info("Extract feature...")
        self.dataset.dataframe = self.dataset.dataframe[self.dataset.features + [self.dataset.target]]

    def convert_target_string_columns_to_numeric(self):
        col = self.dataset.target

        le = LabelEncoder()

        if self.dataset.dataframe[col].dtype == 'object':
            try:
                self.dataset.dataframe[col] = le.fit_transform(self.dataset.dataframe[col])
            except Exception as e:
                print(f"Erreur lors de la transformation de la colonne '{col}': {str(e)}")
    
    def convert_features_string_columns_to_numeric(self):
        col = self.dataset.features

        ohe = OneHotEncoder(sparse_output=False)

        for col in self.dataset.dataframe.columns:
            if self.dataset.dataframe[col].dtype == 'object':
                try:
                    encoded_col = ohe.fit_transform(self.dataset.dataframe[[col]])

                    self.dataset.dataframe.drop(col, axis=1, inplace=True)

                    for i, category in enumerate(ohe.categories_[0]):
                        self.dataset.dataframe[f"{col}_{category}"] = encoded_col[:, i]
                except Exception as e:
                    print(f"Erreur lors de la transformation de la colonne '{col}': {str(e)}")

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
            m = self.build_svm()
        elif model_name == "XGBoost":
            m = self.build_gb()
        elif model_name == "Logistic":
            m = self.build_lr()

        self.algo = Model(m)

    def load_std(self):
        self.std = self.model.standardize if self.model.standardize else None

    def export_model(self, output: str ="model.joblib"):
        dump(self.algo, output)

    def __str__(self):
        pass


    def build_svm(self):
        param_grid = {
            'svc__C': [0.1, 1, 10, 100],
            'svc__gamma': [0.001, 0.01, 0.1, 1],
            'svc__kernel': ['linear', 'rbf', 'sigmoid']
        }

        pipeline = Pipeline([
            ('scaler', StandardScaler() if self.std else None),
            ('svc', SVC())
        ])

        return GridSearchCV(pipeline, param_grid=param_grid, cv=5, n_jobs=-1, verbose=3)
    
    def build_gb(self):
        param_grid = {
            'gb__n_estimators': [50, 100, 200],
            'gb__learning_rate': [0.01, 0.1, 1],
            'gb__max_depth': [3, 5, 7]
        }

        pipeline = Pipeline([
            ('scaler', StandardScaler() if self.std else None),
            ('gb', GradientBoostingClassifier())
        ])

        return GridSearchCV(pipeline, param_grid=param_grid, cv=5, n_jobs=-1, verbose=3)


    def build_lr(self):
        param_grid = {
            'penalty': ['l1', 'l2', 'elasticnet'],
            'C': np.logspace(-4, 4, 20),
            'solver': ['newton-cg', 'lbfgs', 'liblinear', 'sag', 'saga'],
            'max_iter': [1000, 2000, 5000]
        }

        pipeline = Pipeline([
            ('scaler', StandardScaler() if self.std else None),
            ('lr', LogisticRegression())
        ])

        logreg = LogisticRegression(random_state=42)

        return GridSearchCV(logreg, param_grid, cv=5, verbose=3, n_jobs=-1)