# -*- coding: UTF-8 -*-
import matplotlib as mpl 
import matplotlib.pyplot as plt 
import pandas as pd 


data_train = pd.read_csv('train.csv')
font = 'SimHei'
mpl.rcParams['font.sans-serif'] = [font] # 指定默认字体

#研究登船港口和获救情况

fig = plt.figure(figsize =(8, 6))
plt.xticks([])
plt.yticks([])
plt.title(u"登船港口和获救情况的关系")

ax1 = fig.add_subplot(131)
data_train.Survived[data_train.Embarked == 'S'].value_counts().plot(kind = 'bar')
ax1.set_xticklabels([u"未获救", u'获救'], rotation = 0)

plt.legend([u"S港"])

ax2 = fig.add_subplot(132, sharey = ax1)
data_train.Survived[data_train.Embarked == 'C'].value_counts().plot(kind = 'bar')
plt.legend([u"C港"])
ax2.set_xticklabels([u"未获救", u'获救'], rotation = 0)

ax3 = fig.add_subplot(133, sharey = ax1)
data_train.Survived[data_train.Embarked == 'Q'].value_counts().plot(kind = 'bar')
plt.legend([u"Q港"])
ax3.set_xticklabels([u"未获救", u'获救'], rotation = 0)

plt.savefig(u"登船港口与获救情况的关系")
plt.show()