'''
Created on 2016. 4. 22.

@author: David
'''

from ctypes.test import test_sizes
import math
import scipy

import Quandl, math
import pandas
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression

import numpy as np


df = Quandl.get("WIKI/GOOGL")

df = df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume']]
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close']) / df['Adj. Close'] * 100.0
df['PCT_CHANGE'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Close'] * 100.0

df = df[['Adj. Close', 'HL_PCT', 'PCT_CHANGE', 'Adj. Volume']]

#print df.head()

forecast_col = 'Adj. Close'
df.fillna(-99999, inplace=True)

forecast_out = int(math.ceil(0.01*len(df)))

df['label'] = df[forecast_col].shift(-forecast_out)
df.dropna(inplace=True)

x = np.array(df.drop(['label'], 1))
y = np.array(df['label'])

x = preprocessing.scale(x)

#x = x[:-forecast_out+1]
#df.dropna(inplace=True)
y = np.array(df['label'])

x_train, x_test, y_train, y_test = cross_validation.train_test_split(x, y, test_size=0.2)

clf = LinearRegression(n_jobs=-1)
# clf = svm.SVR(kernel='poly')

clf.fit(x_train, y_train)
clf.score(x_test, y_test)

accuracy = clf.score(x_test, y_test)



print accuracy






