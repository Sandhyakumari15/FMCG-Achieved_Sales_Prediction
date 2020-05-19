#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 03:28:58 2020


"""

import pandas as  pd
import warnings
warnings.filterwarnings("ignore",category=DeprecationWarning)

train1=pd.read_csv("train1.csv")
test1=pd.read_csv("test1.csv")

train1.drop(train1.columns[[0,4]], axis = 1, inplace = True)
test1.drop(test1.columns[[0,4]], axis = 1, inplace = True)

import re
p=re.compile(r'\D')
train1['TARGET_IN_EA']=[p.sub('',x) for x in train1['TARGET_IN_EA']]
train1['ACH_IN_EA']=[p.sub('',x) for x in train1['ACH_IN_EA']]
test1['TARGET_IN_EA']=[p.sub('',x) for x in test1['TARGET_IN_EA']]

train1['TARGET_IN_EA']=pd.to_numeric(train1['TARGET_IN_EA'])
train1['ACH_IN_EA']=pd.to_numeric(train1['ACH_IN_EA'])
test1['TARGET_IN_EA']=pd.to_numeric(test1['TARGET_IN_EA'])


from sklearn import preprocessing
label_encoder=preprocessing.LabelEncoder()
train1['PROD_CD']=label_encoder.fit_transform(train1['PROD_CD'])
train1['SLSMAN_CD']=label_encoder.fit_transform(train1['SLSMAN_CD'])
test1['PROD_CD']=label_encoder.fit_transform(test1['PROD_CD'])
test1['SLSMAN_CD']=label_encoder.fit_transform(test1['SLSMAN_CD'])

X = train1.iloc[:,0:4]
Y = train1['ACH_IN_EA']  


X_matrix = X.as_matrix()
Y_matrix = Y.as_matrix()
x_matrix=x.as_matrix()
import xgboost as xgb
xgb1 = xgb.XGBRegressor(learning_rate=0.01,max_depth=9,min_child_weight=2,n_estimators=2000,booster= 'gbtree',base_score=0.5,random_state=0)
xgb1.fit(X_matrix, Y_matrix)


import pickle
#Saving Model to disk
pickle.dump(xgb1,open('model.pkl','wb'))

#loading model to compare results
model = pickle.load(open('model.pkl','rb'))
##from sklearn.linear_model import LinearRegression
#regressor = LinearRegression()

#Fitting model with trainig data
#regressor.fit(X_matrix, Y_matrix)

# Saving model to disk
#pickle.dump(regressor, open('model.pkl','wb'))

# Loading model to compare the results
#model = pickle.load(open('model.pkl','rb'))
