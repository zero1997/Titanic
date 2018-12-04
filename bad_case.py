# -*- coding: UTF-8 -*-

from sklearn import linear_model
import numpy
import sklearn
import pandas as pd
from sklearn import cross_validation

df = pd.read_csv(u"最终train.csv")
split_train, split_cv = cross_validation.train_test_split(df, test_size = 0.3, random_state = 0)
train_df = split_train.filter(regex = 'Survived|Age_.*|SibSp|Parch|Fare_.*|Cabin_.*|Embarked_.*|Sex_.*|Pclass_.*')
train_np = train_df.as_matrix()
y = train_np[:, 0]
X = train_np[:, 1:]
clf = linear_model.LogisticRegression(C = 1.0, penalty='l1', tol=1e-6)
clf.fit(X, y)


cv_df = split_cv.filter(regex = 'Survived|Age_.*|SibSp|Parch|Fare_.*|Cabin_.*|Embarked_.*|Sex_.*|Pclass_.*')
cv_np = cv_df.as_matrix()
y = cv_np[:, 0]
X = cv_np[:, 1:]
predictions = clf.predict(X)

#之后和cv集、交叉验证集预测出来的数据进行对比

bad_cases = df.loc[df['PassengerId'].isin(split_cv[predictions != y]['PassengerId'].values)]

#print bad_cases
bad_cases.to_csv(u"bad_cases.csv")
