# -*- coding: UTF-8 -*-
import pandas as pd 
import numpy as np 

df = pd.read_csv(u"最终train.csv")
df1 = df
Age1 = df['Age']
#print type(Age1)
df1['Age1'] = Age1
df1['TheOld'] = Age1
df1['TheYoung'] = Age1

df1.loc[(df.Age1 <= 12), 'Age1'] = 1
df1.loc[(df.Age1 > 12), 'Age1'] = 0
df1.loc[(df.Age >= 50), 'TheOld'] = 1
df1.loc[(df.Age < 50), 'TheOld'] = 0
df1.loc[((df.Age < 50) & (df.Age >12)), 'TheYoung'] = 1
df1.loc[((df.Age >= 50) | (df.Age <= 12)), 'TheYoung'] = 0



df1['Child'] = df1.pop('Age1')

#dummies_Child = pd.get_dummies(df1['Child'], prefix = 'Child')
#df1 = pd.concat([df1, dummies_Child], axis=1)
df1.to_csv(u"生成child.csv")



