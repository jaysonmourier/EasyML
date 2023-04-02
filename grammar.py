grammar = """
Language:
    use_csv=UseCSV
    features=Features
    target=Target
    model=Model
    standardize=Standardize?
;

UseCSV:
    'USE' csv_file=STRING
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
"""