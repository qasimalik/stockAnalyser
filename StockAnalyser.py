#importing all the required libraries
import pandas as pd
import datetime
import numpy as np
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
import yfinance as yf

#initializing the basic variables like start, end and stock names
start = "2015-01-01"
end = "2020-01-01"
Tata_Steel = yf.download('TATASTEEL.NS', start, end)
Maruti = yf.download('MARUTI.NS', start, end)
ITC = yf.download('ITC.NS', start, end)

#plotting the line graph

'''
Tata_Steel['Open'].plot(label = 'Tata_Steel', figsize = (10, 5))
Maruti['Open'].plot(label = 'Maruti')
ITC['Open'].plot(label = 'ITC')
plt.legend()
plt.show()
'''

#plotting the volume graph
'''
Tata_Steel['Volume'].plot(label = 'Tata_Steel', figsize = (10, 5))
Maruti['Volume'].plot(label = 'Maruti')
ITC['Volume'].plot(label = 'ITC')
plt.legend()
plt.show()
'''


#Plotting the Market Capitalisation Graph
'''
Tata_Steel['MarktCap'] = Tata_Steel['Open'] * Tata_Steel['Volume']
Maruti['MarktCap'] = Maruti['Open'] * Maruti['Volume']
ITC['MarktCap'] = ITC['Open'] * ITC['Volume']
Tata_Steel['MarktCap'].plot(label = 'Tata_Steel', figsize = (10, 5))
Maruti['MarktCap'].plot(label = 'Maruti')
ITC['MarktCap'].plot(label = 'ITC')
plt.legend()
plt.show()
'''

#Plotting the Moving Average graph

'''
Tata_Steel['MA50'] = Tata_Steel['Open'].rolling(50).mean()
Tata_Steel['MA200'] = Tata_Steel['Open'].rolling(200).mean()
Tata_Steel['Open'].plot(figsize = (10, 5))
Tata_Steel['MA50'].plot()
Tata_Steel['MA200'].plot()
plt.legend()
plt.show()
'''

#Plotting the Scattered Plot Matrix graph
'''
data = pd.concat([Tata_Steel['Open'],Maruti['Open'],ITC['Open']],axis = 1)
data.columns = ['Tata_SteelOpen','MarutiOpen','ITCOpen']
scatter_matrix(data, figsize = (10,5), hist_kwds= {'bins':250})
plt.legend()
plt.show()
'''

#Plotting the Volatility graph

Tata_Steel['returns'] = (Tata_Steel['Close']/Tata_Steel['Close'].shift(1)) -1
Maruti['returns'] = (Maruti['Close']/Maruti['Close'].shift(1))-1
ITC['returns'] = (ITC['Close']/ITC['Close'].shift(1)) - 1
Tata_Steel['returns'].hist(bins = 100, label = 'Tata_Steel', alpha = 0.5, figsize = (10, 5))
Maruti['returns'].hist(bins = 100, label = 'Maruti', alpha = 0.5)
ITC['returns'].hist(bins = 100, label = 'ITC', alpha = 0.5)
plt.legend()
plt.show()
