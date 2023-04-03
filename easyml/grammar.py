grammar = """
Language:
    use_csv=UseCSV
    features=Features
    target=Target
    model=Model
    standardize=Standardize?
;

UseCSV:
    'USE' csv_file=STRING options=FILE_OPTIONS?
;

Features:
    'FEATURES' feature_names*=ID[',']
;

Target:
    'TARGET' target_column=ID
;

Model:
    'MODEL' model_type=ModelType
;

ModelType:
    'SVM' | 'XGBoost' | 'Linear'
;

Standardize:
    'STD'
;

FILE_OPTIONS:
'{'
    sep=SEPARATOR?
    header=HEADER?
    index_col=INDEX_COL?
    names=NAMES?
    encoding=ENCODING?
    skip_blank_lines=SKIP_BLANK_LINES?
    na_values=NA_VALUES?
'}'
;

SEPARATOR:
'SEP' STRING
;

HEADER:
'HEADER' INT
;

INDEX_COL:
'INDEX COL' INT
;

NAMES:
'NAMES' names*=ID[',']
;

ENCODING:
'ENCODING' STRING
;

SKIP_BLANK_LINES:
'SKIP BLANK LINES'
;

NA_VALUES:
'NA VALUES' na_values*=STRING[',']
;

"""