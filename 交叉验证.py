# -*- coding: UTF-8 -*-
from sklearn import linear_model
import numpy as np 
import matplotlib as mpl 
import matplotlib.pyplot as plt 
from sklearn.ensemble import RandomForestRegressor
import pandas as pd
from sklearn import cross_validation 


df = pd.read_csv(u"最终train.csv")

train_df = df.filter(regex = 'Survived|Age_.*|SibSp|Parch|Fare_.*|Cabin_.*|Embarked_.*|Sex_.*|Pclass_.*')
train_np = train_df.as_matrix()


y = train_np[:, 0]
X = train_np[:, 1:]
clf = linear_model.LogisticRegression(C = 1.0, penalty='l1', tol=1e-6)

print cross_validation.cross_val_score(clf, X, y, cv = 10)
