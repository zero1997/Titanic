# -*- coding: UTF-8 -*-
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt


df_train = pd.read_csv(u"生成child_mother_family_ticketgroup.csv")

df_train['Family_kind'] = 0
df_train.loc[(df_train.Family_size >= 2) & (df_train.Family_size <= 4), 'Family_kind'] = 1

df_train.to_csv(u"生成child_mother_family_ticketgroup_family离散.csv")