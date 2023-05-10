LOAD "data/train.csv"
USE battery_power, dual_sim
PREDICT m_dep
COMPUTE SVM USING STD
COMPARE XGB, XGB, SVM, LogisticRegression