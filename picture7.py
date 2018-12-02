# -*- coding: UTF-8 -*-
import matplotlib as mpl 
import matplotlib.pyplot as plt 
import pandas as pd 


data_train = pd.read_csv('train.csv')
font = 'SimHei'
mpl.rcParams['font.sans-serif'] = [font] # 指定默认字体


#有无cabin对是否获救的影响
fig = plt.figure(figsize = (8, 6))
xlist = [0, 1]


plt.title(u"有无cabin对是否获救的影响")
plt.yticks([])
plt.xticks([])
ax1 = fig.add_subplot(121)
data_train.Survived[pd.notnull(data_train.Cabin)].value_counts().plot(kind = 'bar')
plt.legend([u"有Cabin信息"])
plt.plot(xlist)

ax2 = fig.add_subplot(122, sharey = ax1)
data_train.Survived[pd.isnull(data_train.Cabin)].value_counts().plot(kind = 'bar')
plt.legend([u"无Cabin信息"])


plt.savefig(u"有无cabin对是否获救的影响")
plt.show()