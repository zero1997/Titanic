# -*- coding: UTF-8 -*-
import matplotlib as mpl 
import matplotlib.pyplot as plt 
import pandas as pd 


data_train = pd.read_csv('train.csv')
font = 'SimHei'

mpl.rcParams['font.sans-serif'] = [font] # 指定默认字体
 
 #然后我们再来看看各种舱级别情况下各性别的获救情况
fig=plt.figure(figsize = (8, 6), dpi = 150)
#fig = plt.figure()
fig.set(alpha = 0.65)
plt.title(u"根据舱等级和性别的获救情况", fontproperties = font)
 #分为男高级，男低级，女高级，女低级

#fig(figsize=(6, 6.5))
plt.xticks([])
plt.yticks([])

ax1 = fig.add_subplot(1, 4, 1)
#plt.xticks()
data_train.Survived[data_train.Sex == 'male'][ data_train.Pclass != 3].value_counts().plot(kind = 'bar', label = 'male highclass')
#ax1.set_xticklabels()
ax1.set_xticklabels([u'未获救', u'获救'], rotation = 0)
ax1.legend([u"男性/高级舱"], loc = 'best')


ax2 = fig.add_subplot(142, sharey = ax1)
data_train.Survived[data_train.Sex == 'male'][data_train.Pclass == 3].value_counts().plot(kind = 'bar', label = 'male lowclass')
ax2.set_xticklabels([u'未获救', u'获救'], rotation = 0)
ax2.legend([u"男性/低级舱"], loc = 'best')

ax3=fig.add_subplot(143, sharey = ax1)
data_train.Survived[data_train.Sex == 'female'][data_train.Pclass != 3].value_counts().plot(kind='bar', label="female highclass")
ax3.set_xticklabels([u"获救", u"未获救"], rotation=0)
ax3.legend([u"女性/高级舱"], loc='best')

ax4 = fig.add_subplot(144, sharey = ax1)
data_train.Survived[data_train.Sex == 'female'][data_train.Pclass == 3].value_counts().plot(kind = 'bar')
ax4.set_xticklabels([u'未获救', u'获救'], rotation = 0)
ax4.legend([u'女性/低级舱'], loc = 'best')


plt.savefig(u"根据舱等级和性别的获救情况")
plt.show()