#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sms
import pandas as pd

get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


df_airline=pd.read_csv('airline_passengers.csv')
df_airline.head()


# In[3]:


df_airline.isnull().sum()


# In[4]:


df_airline.tail()


# In[5]:


df_airline.dropna(axis=0,inplace=True)


# In[6]:


df_airline.isnull().sum()


# In[8]:


df_airline.info()


# In[9]:


df_airline['Month']=pd.to_datetime(df_airline['Month'])


# In[10]:


df_airline.info()


# In[11]:


df_airline.head()


# In[12]:


df_airline.set_index('Month',inplace=True)


# In[13]:


df_airline.head()


# In[14]:


df_airline.plot()


# In[15]:


from statsmodels.tsa.stattools import adfuller


# In[16]:


def adf_test(series):
    result=adfuller(series)
    print('ADF Statistics: {}'.format(result[0]))
    print('p- value: {}'.format(result[1]))
    if result[1] <= 0.05:
        print("strong evidence against the null hypothesis, reject the null hypothesis. Data has no unit root and is stationary")
    else:
        print("weak evidence against null hypothesis, time series has a unit root, indicating it is non-stationary ")


# In[17]:


adf_test(df_airline['Thousands of Passengers'])


# In[18]:


## Use Techniques Differencing
df_airline['Passengers First Difference']=df_airline['Thousands of Passengers']-df_airline['Thousands of Passengers'].shift(1)


# In[19]:


df_airline.head()


# In[20]:


adf_test(df_airline['Passengers First Difference'].dropna())


# In[21]:


## Use Techniques Differencing
df_airline['Passengers Second Difference']=df_airline['Passengers First Difference']-df_airline['Passengers First Difference'].shift(1)


# In[22]:


adf_test(df_airline['Passengers Second Difference'].dropna())


# In[23]:


### 12 months 
## Use Techniques Differencing
df_airline['Passengers 12 Difference']=df_airline['Thousands of Passengers']-df_airline['Thousands of Passengers'].shift(12)


# In[24]:


adf_test(df_airline['Passengers 12 Difference'].dropna())


# In[26]:


from statsmodels.graphics.tsaplots import plot_acf,plot_pacf


# In[27]:


acf = plot_acf(df_airline["Passengers Second Difference"].dropna())


# In[28]:


acf12 = plot_acf(df_airline["Passengers 12 Difference"].dropna())
pacf12 = plot_pacf(df_airline["Passengers 12 Difference"].dropna())


# In[29]:


result = plot_pacf(df_airline["Passengers Second Difference"].dropna())


# In[30]:


pacf12 = plot_pacf(df_airline["Passengers 12 Difference"].dropna())


# In[31]:


### split train and test data
df_airline


# In[32]:


from datetime import datetime,timedelta
train_dataset_end=datetime(1955,12,1)
test_dataset_end=datetime(1960,12,1)


# In[34]:


train_data=df_airline[:train_dataset_end]
test_data=df_airline[train_dataset_end+timedelta(days=1):test_dataset_end]


# In[35]:


##prediction
pred_start_date=test_data.index[0]
pred_end_date=test_data.index[-1]


# In[36]:


test_data


# In[37]:


## create a ARIMA model
from statsmodels.tsa.arima_model import ARIMA


# In[42]:


train_data


# In[125]:


model_ARIMA=ARIMA(train_data['Thousands of Passengers'],order=(0,2,0))


# In[126]:


model_Arima_fit=model_ARIMA.fit()


# In[127]:


model_Arima_fit.summary()


# In[128]:


test_data


# In[112]:


##prediction
pred_start_date=test_data.index[0]
pred_end_date=test_data.index[-1]
print(pred_start_date)
print(pred_end_date)


# In[113]:


pred=model_Arima_fit.predict(start=pred_start_date,end=pred_end_date)
residuals=test_data['Thousands of Passengers']-pred


# In[114]:


pred


# In[115]:


residuals


# In[116]:


model_Arima_fit.resid.plot(kind='kde')


# In[117]:


test_data['Predicted_ARIMA']=pred


# In[118]:


test_data[['Thousands of Passengers','Predicted_ARIMA']].plot()


# In[119]:


acf12 = plot_acf(df_airline["Passengers 12 Difference"].dropna())
pacf12 = plot_pacf(df_airline["Passengers 12 Difference"].dropna())


# In[84]:


## create a SARIMA model
from statsmodels.tsa.statespace.sarimax import SARIMAX


# In[96]:


model_SARIMA=SARIMAX(train_data['Thousands of Passengers'],order=(3,0,5),seasonal_order=(0,1,0,12))


# In[97]:


model_SARIMA_fit=model_SARIMA.fit()


# In[98]:


model_SARIMA_fit.summary()


# In[101]:


test_data.tail()


# In[102]:


##prediction
pred_start_date=test_data.index[0]
pred_end_date=test_data.index[-1]
print(pred_start_date)
print(pred_end_date)


# In[120]:


pred_Sarima=model_SARIMA_fit.predict(start=datetime(1956,6,6),end=datetime(1960,12,1))
residuals=test_data['Thousands of Passengers']-pred_Sarima


# In[121]:


model_SARIMA_fit.resid.plot()


# In[122]:


model_SARIMA_fit.resid.plot(kind='kde')


# In[123]:


test_data['Predicted_SARIMA']=pred_Sarima


# In[94]:


test_data


# In[124]:


test_data[['Thousands of Passengers','Predicted_SARIMA','Predicted_ARIMA']].plot()


# In[ ]:




