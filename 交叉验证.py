# -*- coding: UTF-8 -*-
from sklearn import linear_model
import numpy as np 
import matplotlib as mpl 
import matplotlib.pyplot as plt 
from sklearn.ensemble import RandomForestRegressor
import pandas as pd
from sklearn import cross_validation 


df = pd.read_csv(u"生成child_mother_family_ticketgroup.csv")
train_df = df.filter(regex = 'Survived|Age_.*|Fare_.*|Cabin_.*|Embarked_.*|Sex_.*|Pclass_.*|Child|Family_size|Mother|GroupTicket')

'''
df = pd.read_csv(u"生成child_mother之后生成family.csv")
train_df = df.filter(regex = 'Survived|Fare_.*|Cabin_.*|Embarked_.*|Sex_.*|Pclass_.*|Child|TheOld|TheYoung|Mother|Family_size|Age_.*')
'''
train_np = train_df.as_matrix()


y = train_np[:, 0]
X = train_np[:, 1:]
clf = linear_model.LogisticRegression(C = 1.0, penalty='l1', tol=1e-6)
clf.fit(X, y)
#df = pd.DataFrame({"columns": list(train_df.columns)[:1], "coef": list(clf.coef_.T)})
model_feature = pd.DataFrame({"columns": list(train_df.columns)[1:], "coef": list(clf.coef_.T)})
print model_feature
result = cross_validation.cross_val_score(clf, X, y, cv = 20)
print result.mean()
