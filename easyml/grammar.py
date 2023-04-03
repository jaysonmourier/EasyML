grammar = """
Language:
    use_csv=UseCSV
    features=Features
    target=Target
    test=TEST?
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
    na_values=NA_VALUES?
'}'
;

SEPARATOR:
'SEP' sep=STRING
;

HEADER:
'HEADER' header=INT
;

INDEX_COL:
'INDEX COL' index_col=INT
;

NAMES:
'NAMES' names*=ID[',']
;

ENCODING:
'ENCODING' encoding=STRING
;

NA_VALUES:
'NA VALUES' na_values*=STRING[',']
;

TEST:
'TEST' test=INT
;

"""