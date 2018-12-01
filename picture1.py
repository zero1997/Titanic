# -*- coding: UTF-8 -*-


import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
#一二三四

font = 'SimHei'
data_train = pd.read_csv('train.csv')
#print train_data.head()
#print train_data.info()
#data_train.Survived.value_counts().plot.pie()

#train_data['Age'].value_counts().plot.scatter()
#plt.show()
#plt.savefig(u'扇形图.png')
#print(train_data.describe())
#fig = plt.figure()
#fig = plt.figure(figsize(4, 3), facecolor = 'blue')
#fig=plt.figure(figsize=(4,3),facecolor='blue')
#plt.scatter(train_data.Survived, train_data.Age)
#train_data.Age[train_data.Pclass == 2].plot(kind='kde')

plt.subplot2grid((2,3), (0, 0))
data_train.Survived.value_counts().plot(kind = 'bar')
#plt.title(u'获救情况', fontproperties = font)
plt.title(u"获救情况 (1为获救)", fontproperties='SimHei')  # 标题
plt.ylabel(u'人数', fontproperties = 'SimHei')

plt.subplot2grid((2, 3), (0, 2))
plt.scatter(data_train.Survived, data_train.Age)
plt.ylabel(u'年龄', fontproperties = 'SimHei')
plt.grid(b = True, which = 'major', axis = 'y')#样式
plt.title(u"年龄与是否获救的关系", fontproperties = font)


plt.subplot2grid((2, 3), (1, 0), colspan = 2)
#plt.subplot2grid((2, 3), (1, 0))
data_train.Age[data_train['Pclass'] == 1].plot.kde()
data_train.Age[data_train.Pclass == 2].plot.kde()
data_train.Age[data_train.Pclass == 3].plot.kde()
plt.xlabel(u'年龄', fontproperties = font)
plt.ylabel(u'密度', fontproperties = font)
plt.title(u'各等级的乘客年龄分布', fontproperties = font)
plt.legend((u'1', u'2', u'3'))

plt.subplot2grid((2, 3), (1, 2))
plt.scatter(data_train.Fare, data_train.Survived)
plt.xlabel('nfare')
plt.ylabel('num')
plt.title(u'fare与survive的关系', fontproperties = font)

plt.tight_layout()

#plt.savefig(u"test_picture1")
plt.show()

