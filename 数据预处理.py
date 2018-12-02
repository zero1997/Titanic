# -*- coding: UTF-8 -*-

import numpy as np 
import matplotlib as mpl 
import matplotlib.pyplot as plt 
from sklearn.ensemble import RandomForestRegressor
import pandas as pd
#import sklearn.preprocessing as preprocessing
from sklearn import preprocessing


def set_missing_ages(df):
    age_df = df[['Age', 'Pclass', 'SibSp', 'Parch', 'Fare']]
    #知道年龄的列
    known_age = age_df[age_df.Age.notnull()].as_matrix()
    unknown_age = age_df[age_df.Age.isnull()].as_matrix()

    #把知道年龄的矩阵拿来训练
    y = known_age[:, 0]
    X = known_age[:, 1:]
    
    rfr = RandomForestRegressor(random_state=0, n_estimators=2000, n_jobs=-1)
    rfr.fit(X, y)

    #对不知道年龄的矩阵进行预测
    predictedAges = rfr.predict(unknown_age[:, 1:])
    df.loc[(df.Age.isnull()), 'Age'] = predictedAges
    return df, rfr

def set_missing_cabin(df):
    #分成知道cabin的和不知道的
    df.loc[ (df.Cabin.notnull()), 'Cabin'] = 'yes'
    df.loc[ (df.Cabin.isnull()), 'Cabin'] = 'no'
    return df

def set_index_num(data_train):
    dummies_Cabin = pd.get_dummies(data_train['Cabin'], prefix = 'Cabin')
    dummies_Embarked = pd.get_dummies(data_train['Embarked'], prefix = 'Embarked')
    dummies_Sex = pd.get_dummies(data_train['Sex'], prefix = 'Sex') 
    dummies_Pclass = pd.get_dummies(data_train['Pclass'], prefix='Pclass')
    df = pd.concat([data_train, dummies_Cabin, dummies_Embarked, dummies_Pclass, dummies_Sex], axis = 1)
    df.drop(['Cabin', 'Embarked', 'Pclass', 'Sex'], axis = 1, inplace = True)
    return df

def scalling_age_fare(df):
    scaler = preprocessing.StandardScaler()
    
    age_scale_param = scaler.fit(df['Age'].values.reshape(-1,1))
    df['Age_scaled'] = scaler.fit_transform(df['Age'].values.reshape(-1,1), age_scale_param)
    fare_scale_param = scaler.fit(df['Fare'].values.reshape(-1,1))
    df['Fare_scaled'] = scaler.fit_transform(df['Fare'].values.reshape(-1,1), fare_scale_param)
    
    '''
    scaler.fit(df['Age'].values.reshape(-1, 1))
    scaler.fit(df['Fare'].values.reshape(-1, 1))
    '''
    return df, age_scale_param, fare_scale_param

def set_missing_ages_test(df, rfr):
    age_df = df[['Age', 'Pclass', 'SibSp', 'Parch', 'Fare']]
    unknown_age = age_df[age_df.Age.isnull()].as_matrix()
    predictedAges = rfr.predict(unknown_age[:, 1:])
    df.loc[(df.Age.isnull()), 'Age'] = predictedAges
    return df





#训练集数据
data_train = pd.read_csv(u'train.csv')
#print data_train['Cabin']
#data_train = set_missing_ages(data_train)
data_train, rfr = set_missing_ages(data_train)
#data_train.to_csv(u'Age和Cabin处理之后.csv')
#data_train = set_index_num(data_train)
#data_train.to_csv(u"类目因子数值化之后.csv")
#data_train, age_scale_param, fare_scale_param = scalling_age_fare(data_train)
#data_train.to_csv(u"Age和Fare特征化之后.csv")




#测试集数据

data_test = pd.read_csv("test.csv")
data_test = set_missing_ages_test(data_test, rfr)
#data_test = set_missing_cabin
data_test.to_csv(u"test1.csv")

#data_test = pd.read_csv("test.csv")
#data_test = set_missing_cabin(data_test)
#data_test = scalling_age_fare(data_test)

'''
scaler = preprocessing.StandardScaler()
data_test['Age_scaled'] = scaler.fit_transform(data_test['Age'].values.reshape(-1,1), age_scale_param)
data_test['Fare_scaled'] = scaler.fit_transform(data_test['Fare'].values.reshape(-1,1), fare_scale_param)


data_test = set_index_num(data_test)

data_test.to_csv(u"test2.csv")
'''