# -*- coding: UTF-8 -*-
import pandas as pd 
import numpy as np 


df = pd.read_csv(u"最终test.csv")

df['Child'] = df['Age']
df.loc[(df.Age <= 12), 'Child'] = 1
df.loc[(df.Age > 12), 'Child'] = 0

df['Mother'] = 0
df.loc[((df.Parch > 1) & (df.Name.str.contains('Mrs'))), 'Mother'] = 1

df['Family_size'] = df['Parch']+df['SibSp']

#计算每张船票使用的人数
Ticket_Count = df.groupby('Ticket', as_index = False)['PassengerId'].count()
#获取使用人数为1的船票
Ticket_Count_0 = Ticket_Count[Ticket_Count.PassengerId == 1]['Ticket']
#当船票在已经筛选出使用人数为1的船票中时, 将0赋值给GroupTicket, 否则将1赋值给GroupTicket
df['GroupTicket'] = np.where(df.Ticket.isin(Ticket_Count_0), 0, 1)

df.to_csv("test_child_mother_family_ticketgroup.csv")