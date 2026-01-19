#!/usr/bin/env python
# coding: utf-8

# ARIMA and Seasonal ARIMA
# 
# Autoregressive Integrated Moving Averages
# The general purpose of ARIMA model is the following
# -Visualize the Time Series Data
# -Make the time series data stationary
# -Plot the Correlation and AutoCorrelation Charts
# -Construct the ARIMA Model or Seasonal ARIMA based on the data
# -Use the model to make predictions.

# In[2]:


import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


df = pd.read_csv("C:/Users/Amritanshu Bhardwaj/Downloads/perrin-freres-monthly-champagne.csv")


# In[4]:


df.head()


# In[5]:


df.tail()


# In[6]:


## Cleaning up the data
df.columns = ["Month","Sales"]
df.head()


# In[7]:


# Drop last 2 rows
df.drop(106,axis=0,inplace=True)


# In[8]:


df.tail()


# In[9]:


df.drop(105,axis=0,inplace=True)


# In[10]:


df.tail()


# In[11]:


# Convert Month into Datetime
df['Month'] = pd.to_datetime(df['Month'])


# In[12]:


df.head()


# In[13]:


df.set_index('Month',inplace=True)


# In[14]:


df.head()


# In[15]:


df.describe()


# Step 2 : Visualize the Data

# In[16]:


df.plot()


# In[17]:


### Testing for Stationanrity
from statsmodels.tsa.stattools import adfuller


# In[18]:


test_result = adfuller(df['Sales'])


# In[21]:


# Ho : It is non stationary
# H1 : It is stationary

def adfuller_test(sales):
    result= adfuller(sales)
    labels = ['ADF Test Statistic','p-value','#Lags Used','Number of Observations Used']
    for value,label in zip(result,labels):
        print(label+' : '+str(value))
    if result[1] <= 0.05:
        print("Strong evidence against null hypothesis(Ho),reject the null hypothesis.Data has no unit root and is stationary")
    else:
        print('weak evidence against null hypothesis, time series has unit root indicating it is non-stationary')    


# In[22]:


adfuller_test(df['Sales'])


# Differencing

# In[23]:


df['Sales First Difference'] = df['Sales']-df['Sales'].shift(1)


# In[24]:


df['Sales'].shift(1)


# In[25]:


df['Seasonal First Difference'] = df['Sales']-df['Sales'].shift(12)


# In[26]:


df.head(14)


# In[27]:


# Again test dickey fuller test
adfuller_test(df['Seasonal First Difference'].dropna())


# In[28]:


df['Seasonal First Difference'].plot()


# Auto Regressive Model

# In[31]:


from pandas.plotting import autocorrelation_plot
autocorrelation_plot(df['Sales'])
plt.show()


# In[32]:


from statsmodels.graphics.tsaplots import plot_acf,plot_pacf


# In[34]:


import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

fig = plt.figure(figsize=(12, 8))
ax1 = fig.add_subplot(211)
plot_acf(df['Seasonal First Difference'].iloc[13:], lags=40, ax=ax1)
ax2 = fig.add_subplot(212)
plot_pacf(df['Seasonal First Difference'].iloc[13:], lags=40, ax=ax2)
plt.show()


# In[35]:


## For non-seasonal data
## p=1 , d=1 , q = 0 or 1
from statsmodels.tsa.arima_model import ARIMA


# In[37]:


from statsmodels.tsa.arima.model import ARIMA

# Fit the ARIMA model
model = ARIMA(df['Sales'], order=(1, 1, 1))
model_fit = model.fit()

# Summary of the model
print(model_fit.summary())


# In[38]:


df['forecast'] = model_fit.predict(start=90,end=103,dynamic=True)
df[['Sales','forecast']].plot(figsize=(12,8))


# In[39]:


import statsmodels.api as sm


# In[40]:


model = sm.tsa.statespace.SARIMAX(df['Sales'],order=(1,1,1),seasonal_order=(1,1,1,12))
results = model.fit()


# In[41]:


df['forecast'] = results.predict(start=90,end=103,dynamic=True)
df[['Sales','forecast']].plot(figsize=(12,8))


# In[42]:


from pandas.tseries.offsets import DateOffset
future_dates = [df.index[-1] + DateOffset(months=x) for x in range(0,24)]


# In[43]:


future_dates_df = pd.DataFrame(index=future_dates[1:],columns=df.columns)


# In[44]:


future_dates_df.tail()


# In[45]:


future_df = pd.concat([df,future_dates_df])


# In[46]:


future_df['forecast'] = results.predict(start=104,end=120,dynamic=True)
future_df[['Sales','forecast']].plot(figsize=(12,8))

