# -*- coding: UTF-8 -*-
import pandas as pd 
import numpy as np 

df = pd.read_csv(u"生成child之后生成mother.csv")

df['Family_size'] = df['Parch']+df['SibSp']

df.to_csv(u"生成child_mother之后生成family.csv")