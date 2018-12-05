# -*- coding: UTF-8 -*-
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt


df_train = pd.read_csv(u"生成child_mother之后生成family.csv")

#计算每张船票使用的人数
Ticket_Count = df_train.groupby('Ticket', as_index = False)['PassengerId'].count()
#获取使用人数为1的船票
Ticket_Count_0 = Ticket_Count[Ticket_Count.PassengerId == 1]['Ticket']
#当船票在已经筛选出使用人数为1的船票中时, 将0赋值给GroupTicket, 否则将1赋值给GroupTicket
df_train['GroupTicket'] = np.where(df_train.Ticket.isin(Ticket_Count_0), 0, 1)

df_train.to_csv(u"生成child_mother_family_ticketgroup.csv")