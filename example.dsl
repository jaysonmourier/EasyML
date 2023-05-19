LOAD "data/credit_customers.csv"
USE installment_commitment, personal_status
PREDICT credit_history
COMPUTE XGB WITH 35% OF TEST USING STD
COMPARE XGB, SVM, LogisticRegression