# -*- coding: UTF-8 -*-


import pandas as pd 
import matplotlib as mpl 
import matplotlib.pyplot as plt

font = "SimHei"
data_train = pd.read_csv('train.csv')


Survived_0 = data_train.Embarked[data_train.Survived == 0].value_counts()
Survived_1 = data_train.Embarked[data_train.Survived == 1].value_counts()
df=pd.DataFrame({u'survived':Survived_1, u'not':Survived_0})
df.plot(kind='bar', stacked=True) #画柱状图
plt.title(u"各登陆港口乘客的获救情况", fontproperties = font)
plt.xlabel(u"登陆港口", fontproperties = font)
plt.ylabel(u"人数", fontproperties = font)
plt.savefig("test_picture2")
plt.show()