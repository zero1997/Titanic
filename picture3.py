# -*- coding: UTF-8 -*-


import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt


font = "SimHei"
data_train = pd.read_csv("train.csv")
#年龄与是否获救关系
data_train.Age[data_train.Survived == 1].plot.kde()
data_train.Age[data_train.Survived == 0].plot.kde()
plt.title(u"年龄与是否获救的关系", fontproperties = font)
plt.xlabel(u"年龄", fontproperties = font)
plt.ylabel(u"密度", fontproperties = font)
plt.legend((u'1', u'0'))
plt.savefig(u"年龄与获救情况")


Survived_m = data_train.Survived[data_train.Sex == 'male'].value_counts()
Survived_f = data_train.Survived[data_train.Sex == 'female'].value_counts()
df = pd.DataFrame({u'male':Survived_m, u'female':Survived_f})
df.plot(kind = 'bar', stacked = True)
plt.title(u"性别与是否获救的关系", fontproperties = font)
plt.xlabel(u"是否获救", fontproperties = font)
plt.ylabel(u"人数", fontproperties = font)
#plt.legend((u'male', u'female'))
plt.savefig(u"性别与获救情况")


plt.show()
