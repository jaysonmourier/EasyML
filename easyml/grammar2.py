grammar = """
Language:
    load_csv=LoadCSV
    features_list=FeaturesList
    target=Target
    model=Model
    models=Models?
;

LoadCSV:
    'LOAD' csv_path=STRING options=CSV_OPTIONS?
;

CSV_OPTIONS:
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

FeaturesList:
    'USE' features_name*=feature[','] option=Standardize?
;

feature:
    feature_name=ID
;


Target:
    'PREDICT' target_name=ID
;

Model:
    'COMPUTE' model_name=ModelName option=ModelOption? std=Standardize?
;

Standardize:
    'USING STD'
;

ModelName:
    'SVM' | 'XGB' | 'LogisticRegression'
;

ModelOption:
    'WITH' test_size=INT '% OF TEST'
;

Models:
    'COMPARE' models_list*=ModelName[',']?
;

"""