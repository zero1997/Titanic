# -*- coding: UTF-8 -*-

import numpy as np 
import matplotlib as mpl 
import matplotlib.pyplot as plt 
from sklearn.ensemble import RandomForestRegressor
import pandas as pd
#import sklearn.preprocessing as preprocessing
from sklearn import preprocessing

data_test = pd.read_csv(u"test_填补年龄和cabin_onehot之后.csv")
#print data_test.describe()
#a = 35.627188