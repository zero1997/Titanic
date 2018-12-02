 # -*- coding: UTF-8 -*-
import matplotlib as mpl 
import matplotlib.pyplot as plt 
import pandas as pd 


data_train = pd.read_csv('train.csv')
font = 'SimHei'

mpl.rcParams['font.sans-serif'] = [font] # 指定默认字体
 
 #然后我们再来看看各种舱级别情况下各性别的获救情况

 
 
 #然后我们再来看看各种舱级别情况下各性别的获救情况


 
fig = plt.figure()
fig.set(alpha=0.2)  # 设定图表颜色alpha参数
 
Survived_cabin = data_train.Survived[pd.notnull(data_train.Cabin)].value_counts()
Survived_nocabin = data_train.Survived[pd.isnull(data_train.Cabin)].value_counts()
df=pd.DataFrame({u'有':Survived_cabin, u'无':Survived_nocabin}).transpose()
df.plot(kind='bar', stacked=True)
plt.title(u"按Cabin有无看获救情况")
plt.xlabel(u"Cabin有无") 
plt.ylabel(u"人数")
plt.show()


