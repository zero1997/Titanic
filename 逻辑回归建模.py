# -*- coding: UTF-8 -*-
from sklearn import linear_model
import numpy as np 
import matplotlib as mpl 
import matplotlib.pyplot as plt 
from sklearn.ensemble import RandomForestRegressor
import pandas as pd


df = pd.read_csv(u"最终train.csv")

train_df = df.filter(regex = 'Survived|Age_.*|SibSp|Parch|Fare_.*|Cabin_.*|Embarked_.*|Sex_.*|Pclass_.*')
train_np = train_df.as_matrix()


y = train_np[:, 0]
X = train_np[:, 1:]
clf = linear_model.LogisticRegression(C = 1.0, penalty='l1', tol=1e-6)
clf.fit(X, y)

model_feature = pd.DataFrame({"columns": list(train_df.columns)[1:], "coef": list(clf.coef_.T)})
model_feature.to_csv("model_feature.csv")

'''
df_test = pd.read_csv(u"最终test.csv")
test = df_test.filter(regex='Age_.*|SibSp|Parch|Fare_.*|Cabin_.*|Embarked_.*|Sex_.*|Pclass_.*')
predictions = clf.predict(test)
result = pd.DataFrame({'PassengerId':df_test['PassengerId'].as_matrix(), 'Survived':predictions.astype(np.int32)})
result.to_csv("logistic_regression_predictions.csv", index=False)
'''