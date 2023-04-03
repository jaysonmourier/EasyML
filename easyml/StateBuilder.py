from textx import metamodel_from_str
import pandas as pd
from . import log, grammar, Dataset

class StateBuilder:

    dataset: pd.DataFrame

    def __init__(self, filepath: str):
        self.metamodel = metamodel_from_str(grammar)
        
        try:
            self.model = self.metamodel.model_from_file(file_name=filepath)
        except Exception:
            log.fatal(1, "Error during initialization. Check the validity of the script name.")
        
        self.load_dataset()

    def load_dataset(self):
        log.info("Loading dataset...")

        if not self.model.use_csv.csv_file:
            log.fatal(1, "error script")

        default_values = {
            'sep': ',',
            'header': 0,
            'index_col': None,
            'names': None,
            'encoding': 'utf-8',
            'skip_blank_lines': True,
            'na_values': ""
        }

        def get_value(option_name, textx_obj):
            if textx_obj is None:
                return default_values[option_name]
            return getattr(textx_obj, option_name)

        options = {opt: get_value(opt, getattr(self.model.use_csv.options, opt, None)) for opt in default_values if opt != 'skip_blank_lines'}

        print(options)

        self.dataset = Dataset(self.model.use_csv.csv_file, **options)
        self.dataset.load()
