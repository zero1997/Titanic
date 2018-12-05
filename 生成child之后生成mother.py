# -*- coding: UTF-8 -*-
import pandas as pd 
import numpy as np 


df = pd.read_csv(u"生成child.csv")
df['Mother'] = 0

df.loc[((df.Parch > 1) & (df.Name.str.contains('Mrs'))), 'Mother'] = 1



df.to_csv(u"生成child之后生成mother.csv")