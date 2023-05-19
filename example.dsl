LOAD "data/credit_customers.csv"
USE installment_commitment, personal_status
PREDICT credit_history
COMPUTE SVM USING STD
COMPARE XGB, XGB, SVM, LogisticRegression