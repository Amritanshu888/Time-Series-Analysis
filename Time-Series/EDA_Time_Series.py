#!/usr/bin/env python
# coding: utf-8

# ## Time Series EDA

# In[1]:


## Install Pandas Data Reader
get_ipython().system('pip install pandas-datareader')


# In[2]:


import pandas_datareader as pdr
import pandas as pd
from datetime import datetime


# In[4]:


df_tesla=pdr.get_data_yahoo('TSLA')


# In[7]:


df_tesla.tail()


# In[10]:


df_tesla['High'].plot(figsize=(12,4))


# In[11]:


## xlimit and y limit
df_tesla['High'].plot(xlim=['2020-01-01','2021-09-01'],figsize=(12,4))


# In[13]:


## xlimit and y limit
df_tesla['High'].plot(xlim=['2020-01-01','2021-09-01'],ylim=[0,900],figsize=(12,4))


# In[15]:


## xlimit and y limit and coloring
df_tesla['High'].plot(xlim=['2020-01-01','2021-09-01'],ylim=[0,900],figsize=(12,4),ls='--',c='green')


# In[17]:


df_tesla.index


# In[20]:


index=df_tesla.loc['2020-01-01':'2021-09-01'].index
share_open=df_tesla.loc['2020-01-01':'2021-09-01']['Open']


# In[21]:


share_open


# In[22]:


index


# In[25]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[28]:


figure,axis=plt.subplots()
plt.tight_layout()
## Preventing overlapping
figure.autofmt_xdate()
axis.plot(index,share_open)


# In[29]:


## Datetime Index


# In[32]:


df_tesla=df_tesla.reset_index()


# In[33]:


df_tesla.info()


# In[42]:


df_tesla=df_tesla.set_index('Date',drop=True)


# In[43]:


df_tesla.head()


# In[44]:


## datetime
from datetime import datetime


# In[45]:


datetime(2021,11,21)


# In[52]:


datetime.now()


# In[64]:


date=datetime(2021,11,21)


# In[65]:


date


# In[67]:


date.date()


# In[69]:


date.day


# In[71]:


date.weekday()


# In[72]:


date.year


# In[73]:


date.month


# ## Time Resampling

# In[74]:


df_tesla.head()


# In[76]:


df_tesla.resample(rule='A').min()


# In[77]:


df_tesla.resample(rule='A').max()


# In[79]:


##year end frequency
df_tesla.resample(rule='A').max()['Open'].plot()


# In[81]:


##quaterly start frequency
##https://towardsdatascience.com/resample-function-of-pandas-79b17ec82a78
df_tesla.resample(rule='QS').max()['High'].plot()


# In[83]:


##Business End Frequency
##https://towardsdatascience.com/resample-function-of-pandas-79b17ec82a78
df_tesla.resample(rule='BA').max()


# In[84]:


df_tesla.resample(rule='BQS').max()


# In[87]:


##plotting
df_tesla['Open'].resample(rule='A').mean().plot(kind='bar')


# In[92]:


df_tesla['Open'].resample(rule='M').max().plot(kind='bar',figsize=(15,6))


# In[100]:


df_tesla['High'].rolling(11).max().head(20)


# In[97]:


df_tesla.head()


# In[101]:


df_tesla['Open:30 days rolling']=df_tesla['Open'].rolling(30).mean()


# In[104]:


df_tesla.head(31)


# In[105]:


df_tesla[['Open','Open:30 days rolling']].plot(figsize=(12,5))


# ##Assignment
# ##news
# 1. Read the Microsoft Data using Pandas Data reader
# 2. Get the maximum price of the share from 2017 to 2022
# 3. Which is the date of the highest price of the stock?
# 4. Which is the date of the lowest price of the stock?
