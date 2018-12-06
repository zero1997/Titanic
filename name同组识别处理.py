# -*- coding: UTF-8 -*-
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt


train =  pd.read_csv(u"生成child_mother_family_ticketgroup_family离散.csv")
test = pd.read_csv(u"test_child_mother_family_ticketgroup_family离散.csv")
all_data = pd.concat([train, test], ignore_index=True)
#print type(all_data['Sex_female'])
#print all_data.index

all_data['Surname'] = all_data['Name'].apply(lambda x: x.split(',')[0].strip())
#print all_data['Surname']
#all_data['Surname']=all_data['Name'].apply(lambda x:x.split(',')[0].strip())
Surname_count = dict(all_data['Surname'].value_counts())
all_data['FamilyGroup'] = all_data['Surname'].apply(lambda x: Surname_count[x])
Female_Child_Group = all_data.loc[(all_data['FamilyGroup'] >= 2) & ((all_data['Age'] <= 12) | (all_data['Sex'] == 'female'))]
Male_Adult_Group = all_data.loc[(all_data['FamilyGroup'] >= 2) & (all_data['Age'] >= 12) & (all_data['Sex'] == 'male')]

Female_Child_Group = Female_Child_Group.groupby('Surname')['Survived'].mean()
Dead_List = set(Female_Child_Group[Female_Child_Group.apply(lambda x: x == 0)].index)
#print Dead_List
Male_Adult_List = Male_Adult_Group.groupby('Surname')['Survived'].mean()
Survived_List = set(Male_Adult_List[Male_Adult_List.apply(lambda x: x==1)].index)
print Survived_List