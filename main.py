import pandas as pd
from textx import metamodel_from_file

easyml_meta = metamodel_from_file('easyml.tx')
easy_model = easyml_meta.model_from_str('main.easyml')

df = pd.read_csv(easy_model.name, skipinitialspace=True, usecols= easy_model.names)
