# -*- coding: UTF-8 -*-
from sklearn import linear_model
import numpy as np 
import matplotlib as mpl 
import matplotlib.pyplot as plt 
from sklearn.ensemble import RandomForestRegressor
import pandas as pd
from sklearn import cross_validation 
from sklearn.ensemble import BaggingRegressor


if __name__ == '__main__':
    df = pd.read_csv(u"生成child_mother_family_ticketgroup.csv")
    #print df
    train_df = df.filter(regex = 'Survived|Age_.*|SibSp|Parch|Fare_.*|Cabin_.*|Embarked_.*|Sex_.*|Pclass.*|Mother|Child|Family_size')
    train_np = train_df.as_matrix()
    y = train_np[:, 0]
    X = train_np[:, 1:]
    clf = linear_model.LogisticRegression(C = 1.0, penalty='l1', tol=1e-6)

    bagging_clf = BaggingRegressor(clf, n_estimators=20, max_samples=0.8, max_features=1.0, bootstrap=True, bootstrap_features=False, n_jobs=-1)
    bagging_clf.fit(X, y)


    df_test = pd.read_csv(u"test_child_mother_family_ticketgroup.csv")
    test = df_test.filter(regex = 'Age_.*|SibSp|Parch|Fare_.*|Cabin_.*|Embarked_.*|Sex_.*|Pclass.*|Mother|Child|Family_size')
    predictions = bagging_clf.predict(test)
    result = pd.DataFrame({'PassengerId':df_test['PassengerId'].as_matrix(), 'Survived':predictions.astype(np.int32)})
    result.to_csv(u"模型3_bagging预测结果.csv")
