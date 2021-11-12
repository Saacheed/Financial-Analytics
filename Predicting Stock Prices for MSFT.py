#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np  
import pandas as pd  
from pandas_datareader import data as wb  
import matplotlib.pyplot as plt  
from scipy.stats import norm
get_ipython().run_line_magic('matplotlib', 'inline')

ticker = 'MSFT' 
data = pd.DataFrame()
data[ticker] = wb.DataReader(ticker, data_source='yahoo', start='2000-1-1')['Adj Close']

log_returns = np.log(1 + data.pct_change())
u = log_returns.mean()
var = log_returns.var()
drift = u - (0.5 * var)
stdev = log_returns.std()

drift.values
stdev.values

t_intervals = 250
iterations = 10

daily_returns = np.exp(drift.values + stdev.values * norm.ppf(np.random.rand(t_intervals, iterations)))


# In[5]:


S0 = data.iloc[-1]
S0


# In[7]:


price_list = np.zeros_like(daily_returns)
price_list


# In[9]:


price_list[0]


# In[11]:


price_list[0] = S0
price_list


# In[14]:


for t in range(1, t_intervals):
    price_list[t] = price_list[t - 1] * daily_returns[t]


# In[16]:


price_list


# In[17]:


plt.figure(figsize=(10,6))
plt.plot(price_list);

