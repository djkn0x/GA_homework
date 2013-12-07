import json
import urllib
import os
import time
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.cross_validation import train_test_split

# Specify directory for storing data
dir_out = '/home/GA10/data/yahoo_finance_data'
if not os.path.exists(dir_out):
    os.mkdir(dir_out)
    print 'created directory %s' % dir_out

# Use list of NASDAQ stocks that have IPOed in the last few years 
symbols = ['VMW', 'N', 'RAX', 'YOKU', 'TMH', 'INXN', 'YGE', 'PRO', 'BITA', 'ARX', 'JKS', 'CAP', 'IL', 
           'IPHI', 'RST', 'RLD', 'ISS', 'LDK', 'MXL', 'DQ', 'STV', 'CIS', 'NED']
tmp =[]

for symbol in symbols:

    # Grab data from Yahoo Finance 
    time.sleep(.5)
    data_out = {}
    url = 'http://ichart.finance.yahoo.com/table.csv?s=%s&d=6&e=24&f=2013&g=d&a=4&b=18&c=2012&ignore=.csv' % (symbol)
    data = urllib.urlopen(url).read()
    file = '%s/%s_data.csv' % (dir_out, symbol)
    f = open(file,'w')
    f.write('%s' % str(data))
    f.close()
    data = data.split('\n')
    for d in data[1:-1]:
        try:
            d = d.split(',')
            close = d[6]
            tmp.append(close)
        except:pass
    file = '%s/%s_data.csv' % (dir_out, symbol)
    read_file = pd.read_csv(file)
    
    # Set parameters for Linear Regression model
    data = read_file.drop(['Date', 'Close', 'Open', 'High', 'Adj Close'], axis=1)
    y = read_file['Adj Close']
    
    # Create training and test datasets
    X_train,X_test,y_train,y_test=train_test_split(data, y, test_size=0.33, random_state=23)
    
    # Run Linear Regression model on training data
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Print out RSS for each model
    print ('Residual sum of squares for %s: %.2f \n' % (symbol, np.mean((model.predict(X_test) - y_test) **2)))
    print ('R^2, coefficient of determination for %s: %.2f \n' % (symbol, model.score(X_test, y_test)))
