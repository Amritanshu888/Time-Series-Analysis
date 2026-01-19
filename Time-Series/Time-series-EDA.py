#!/usr/bin/env python
# coding: utf-8

# In[2]:


## Install Pandas Data Reader
get_ipython().system('pip install pandas-datareader')


# In[3]:


import pandas_datareader as pdr
import pandas as pd
from datetime import datetime


# In[5]:


get_ipython().system('pip install yfinance')


# In[7]:


import yfinance as yf
# Fetch Tesla stock data
df_tsla = yf.download('TSLA')  ## Stock data


# In[8]:


type(df_tsla)


# In[9]:


df_tsla.head()


# In[10]:


df_tsla.tail()


# In[11]:


df_tsla.plot()


# In[13]:


df_tsla['High'].plot(figsize=(12,4))


# In[14]:


## x limit and y limit
df_tsla['High'].plot(xlim=['2020-01-01','2021-09-01'],figsize=(12,4)) ##start and end state specify kiya


# In[15]:


## x limit and y limit
df_tsla['High'].plot(xlim=['2020-01-01','2021-09-01'],ylim=[0,800],figsize=(12,4))
## y ke direction me values specify ki


# In[16]:


## x limit and y limit and coloring
df_tsla['High'].plot(xlim=['2020-01-01','2021-09-01'],ylim=[0,800],figsize=(12,4),c='green')


# In[17]:


## x limit and y limit and coloring and linestyle
df_tsla['High'].plot(xlim=['2020-01-01','2021-09-01'],ylim=[0,800],figsize=(12,4),c='green',ls='--')


# In[18]:


df_tsla.index


# In[ ]:


## How to read specific indexes (values at specific dates)
df_tsla.loc['2020-01-01':'2021-09-01']  #index based reading (iss date se uss date tak)


# In[20]:


df_tsla.loc['2020-01-01':'2021-09-01'].index


# In[21]:


index = df_tsla.loc['2020-01-01':'2021-09-01'].index
share_open = df_tsla.loc['2020-01-01':'2021-09-01']['Open']


# In[22]:


share_open


# In[23]:


index


# In[24]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[ ]:


figure,axis = plt.subplots()
plt.tight_layout()
figure.autofmt_xdate()  ##taki x axis ki value display hone me overlap na kare
# Auto formating x date is actually preventing overlapping
axis.plot(index,share_open)


# In[ ]:


## Datetime Index


# In[28]:


df_tsla.info()


# In[ ]:


df_tsla.reset_index()  ## Here u are getting date_time as a seperate column
## Date is the index here


# In[30]:


df_tsla = df_tsla.reset_index()


# In[31]:


df_tsla.info()


# In[ ]:


pd.to_datetime(df_tsla['Date']) ## Date in dataset was given in string format we converted it to datetime


# In[ ]:


df_tsla  ## Here u will see that date is not an index anymore as we reseted the index
# (Originally it was index)


# In[ ]:


## To make date as index 
df_tsla.set_index('Date',drop=True) ## don't forget to keep drop true, telling ki kis column ko 
# index banana hai 


# In[36]:


df_tsla = df_tsla.set_index('Date',drop=True)


# In[37]:


df_tsla.head()


# In[38]:


## datetime
from datetime import datetime


# In[39]:


datetime(2021,11,21)


# In[40]:


datetime.now()


# In[41]:


def add_num(num1,num2):
    return num1+num2


# In[ ]:


start_time = datetime.now()
num1 = 20
num2 = 30

add_num(num1,num2)
end_time = datetime.now()
print(end_time-start_time)  ##matlab ye addition wala operation 0 time me really fast execute 
# ho rha hai


# In[43]:


start_time = datetime.now()
num1 = 20
num2 = 30
for i in [1,2,3,4,5]:
    add_num(num1,num2)
end_time = datetime.now()
print(end_time-start_time)


# In[44]:


date = datetime(2021,11,21)


# In[45]:


date


# In[47]:


date.date()


# In[48]:


date.day


# In[49]:


date.weekday()


# In[50]:


date.year


# In[51]:


date.month


# Time Resampling

# In[52]:


df_tsla.head()


# In[53]:


df_tsla.resample(rule='A')


# In[ ]:


df_tsla.resample(rule='A').min()
#Ye aapko harr year ke harr ek attribute/instance/feature ki minimum value dega


# In[55]:


df_tsla.resample(rule='A').max()
#Ye aapko harr year ke harr ek attribute/instance/feature ki maximum value dega


# In[56]:


type(df_tsla.resample(rule='A').max()) ##its type is a dataframe


# In[57]:


df_tsla.resample(rule='A').max()['Open'].plot() ##Plotting with respect to open


# Rule 'A' basically means year and frequency

# In[ ]:


## quaterly start frequency
## Quaterly information u will be able to get(of max)
df_tsla.resample(rule='QS').max()


# In[ ]:


df_tsla.resample(rule='QS').max()['High'].plot()
## Quaterly high(instance) ka plot karna (max ko(of high))


# In[60]:


## Business End Frequency
df_tsla.resample(rule='BA').max()['High'].plot()


# In[ ]:


df_tsla.resample(rule='BA').max() ##Since its end frequency so from here bussiness is ending
## u can see 31'st 29'th in end date


# In[ ]:


## Bussiness quaterly start
## from here bussinesses are getting start so here u can see start date
df_tsla.resample(rule='BQS').max()


# In[63]:


## Plotting
df_tsla['Open'].resample(rule='BA').mean().plot(kind='bar')


# In[64]:


df_tsla['Open'].resample(rule='A').mean().plot(kind='bar')


# In[ ]:


df_tsla['Open'].resample(rule='M').mean()
## Help us to get monthly mean(u can do for any instance also)


# In[66]:


df_tsla['Open'].resample(rule='M').max()
## Help us to get monthly max(u can do for any instance also)


# In[68]:


df_tsla['Open'].resample(rule='M').max().plot(kind='bar',figsize=(15,6))


# In[69]:


df_tsla.head()


# In[70]:


df_tsla['High'].head()


# In[ ]:


df_tsla['High'].rolling(10) #Rolling of 10 days
## axis 0 i.e. we are doing it for column


# In[ ]:


df_tsla['High'].rolling(10).mean() ## On this rolling we are applying aggregate function and finding mean
## Here u are trying to find out rolling mean for 10 days


# In[78]:


df_tsla['High'].rolling(10).max()


# In[ ]:


df_tsla['High'].rolling(10).mean().head(20) ## since its rolling mean for 10 , isliye usse pehle ki values NaN ho gyi


# In[79]:


df_tsla['High'].rolling(10).max().head(20)


# In[74]:


## Creating a new columns
df_tsla['Open:30 days rolling'] = df_tsla['Open'].rolling(30).mean()


# In[75]:


df_tsla.head()


# In[ ]:


df_tsla.head(32)  ## Rolling was of 30 days isliye usse pehle ki values NaN ho gayi


# In[ ]:


df_tsla[['Open','Open:30 days rolling']].plot(figsize=(12,5))
## Note: with the help of rolling we can also do smoothening


# Rolling provides rolling windows calculation that's what we specifically do in moving average
# Orange line is the smoothened version of the blue line
# Whatever we discussed with respect to rolling window is specifically called mean average(which we got from rolling window).
# Next we will learn Exponentially weighted moving average(EWMA)
# Error trend seasonality(ETS).
# ARIMA
# ACF
# PACF
# Autocorrelation Plot
# Partial Autocorrelation Plot
# ARIMAX ,SARIMAX
# How to use FbProphet to do forecasting(library developed by facebook)

# Basic idea of Time series data
# 1. Upward Trend
# 2. Stationanry Trend
# 3. Downward Trend
# 4. Cyclic Trend

# Day 2 - Time Series
# 1. Simple Moving Average
# 2. Cummulative Moving Average
# 3. Exponential Weight Moving Average
# 4. Moving Average (Formula) --> ACF (AutoCorrelation Plot) (MA)
# 5. AutoRegreesive Model --> PACF (Partial AutoCorrelation) (AR)  Combine these two it becomes ARMA model
# 
# Next Class : ARIMA,ARIMAX,SARIMAX

# In[80]:


import pandas_datareader as pdr
import pandas as pd
from datetime import datetime


# In[81]:


import yfinance as yf

# Fetch Tesla stock data
df_tsla = yf.download('TSLA')
df_tsla


# In[ ]:


## Simple Moving Average
## Helps in smoothenning the curve (harr 5 instance ka average nikalna)


# In[82]:


df_tsla['Open'].plot(figsize=(15,6))


# In[83]:


df_tsla['Open:10 days rolling'] = df_tsla['Open'].rolling(window=10,min_periods=1).mean()


# In[85]:


df_tsla[['Open','Open:10 days rolling']].plot(figsize=(15,6))


# In[86]:


df_tsla[['Open','Open:10 days rolling']].plot(xlim=['2020-01-01','2021-01-01'],figsize=(15,6))


# In financing why do people use it
# Curve me jab price low jaye then its the buy time for u and jab price high jaye then its sell time for you to earn the profit
# (This is why people use it in stock market and finance) Used only for short term
# U need not depend only on 10 windows , u can use any number of windows u want.

# In[87]:


df_tsla['Open:30 days rolling'] = df_tsla['Open'].rolling(window=30,min_periods=1).mean()
df_tsla['Open:50 days rolling'] = df_tsla['Open'].rolling(window=50,min_periods=1).mean()


# In[88]:


df_tsla[['Open','Open:10 days rolling','Open:30 days rolling','Open:50 days rolling']].plot(xlim=['2020-01-01','2021-01-01'],figsize=(15,6))


# As the window size is increasing in rolling the curve is becoming smoothen(simple moving average)
# Major Disadvantage of Simple Moving Average:
# 1. U are giving similiar importance to all the data , for all the data points based on the window size
# u are using the formula (x1 + x2 + x3 + x4 + x5)/5 only , where n = window size.
# In time series our main focus should be given to recent data a lot.
# I want to give more importance or can say more weight to the recent data , and that weight is basically provided by some parameters
# that we are going to see in EWMA(Exponentially Weighted Moving Average)
# 
# 2. Cummulative Moving Average(CMA)
# if we have Open : 12 13 11 15 16 18
# Then in CMA we have : (12+13)/2 , (12+13+11)/3 , (12+13+11+15)/4 and this way u calculate CMA
# Very very easy u can use a function expanding to find it out.

# In[ ]:


## Expanding
# CMA
df_tsla['Open'].expanding().mean().plot(figsize=(10,5))


# EWMA - Exponentially Weighted Moving Average
# Here our focus should be more on the current upcoming data or just on the recent data that we are having so that 
# we can do the projection properly
# If u want to calculate EWMA with respect to t , then 
# EMWA(t) = a * x(t) + (1-a) * EMWA(t-1) , here a is weight , through which u are giving priority to your
# first data instead of the previous one , this is specifically done to prevent any kind of lags.

# In[ ]:


#EMWA - Exponentially Weighted Moving Average or Exponential Moving Average


# In[ ]:


## EMA(Exponential moving average) tesla shares
# Lets's smoothing factor - 0.1
df_tsla['EMA_0.1'] = df_tsla['Open'].ewm(alpha=0.1,adjust=False).mean()


# In[94]:


df_tsla[['Open','EMA_0.1']].plot(xlim=['2020-01-01','2021-01-01'],figsize=(15,6))


# In[95]:


df_tsla['EMA_0.3'] = df_tsla['Open'].ewm(alpha=0.3,adjust=False).mean()


# In[96]:


df_tsla[['Open','EMA_0.1','EMA_0.3']].plot(xlim=['2020-01-01','2021-01-01'],figsize=(15,6))


# In[ ]:


## EWMA(Exponential weighted moving average) tesla shares
# U can do it with the help of span(in days)in ewm() function
df_tsla['EMA_5days'] = df_tsla['Open'].ewm(span=5).mean()


# In[99]:


df_tsla[['Open','EMA_5days']].plot(figsize=(15,5))


# In[100]:


df_tsla[['Open','EMA_0.1','EMA_5days']].plot(figsize=(15,5))


# Which moving average is the best ?
# Exponential Weighted Moving Average is the best
# 
# In ARIMA --> AR + I + MA
# AR - Auto Regreesion
# MA - Moving Average
# If u combine only these two , then it will specifically become ARMA model
# (ARMA model is good for forecasting specifically sales(monthly production), but is not good for stock predictions(waste of time))
# (No model is good for stocks)
# 
# Interview Questions:
# For moving average do you use PACF plot or ACF plot ??
# Where is PACF used or where is ACF used ??

# Moving Average Models
# Let's say my expectation w.r.t the people attending the live session is u = 10 (mean/average expectation)
# So if I want to calculate or create moving average models my formula will be like this :
# MA = u + Coefficient1 * Error term with respect to previous time stamp. Here my mean u = 10.
# This is how model does forecasting of future with your previous data. I have t-1 data , t-2 data then with these previous
# data we will be able to predict the future data values.

# ARIMA and SAIMAX , 1st thing to understand - Autoregression 2nd Moving Average
# 3rd one Integrated (I of arima)
# Autoregression is specifically done by graph which is called PACF(Partial Autocorrelation)
# Moving Average is basically done by Auto-correlation plots
# Integrated value can be found out by diffrential
# We will find out all these values and based on these we will solve the problem

# ARIMA 
# Autoregression : Suppose i have dataset giving monthly sales of onions , let's say right now its april month 
# then Jan Feb  March April
#     t-3  t-2   t-1   t
# In autoregression we are just trying to apply some regression algorithmns in order to find out that what
# may be the sale in may month. Here if my k value is 4 , then I will see my previous 4 months (this is called as lags),
# lags is u refering to ur previous months to find out the sales of ur next months. And each and every previous month
# may have a direct or indirect impact on the sales of next month.
# Regression algorithms : y = mx + c (now we apply this w.r.t timestamp)
# How do we define our k value ??
# Ot = B0 + B1*Ot-1 + B2*Ot-2 + B3*Ot-3 , here B1 , B2 , B3 are coefficients whichare helping to determine how much the
# values Ot-1 , Ot-2 .... are impacting Ot. (Lags basically means timestamp).
# PACF is giving correlation from a specific lag to the current timestamp. Graph: x me lags and y me PACF. Graph me it specifies 
# a range , on both above and below axis (specifies upper bound and lower bound). (NOTE: Graphs are been plotted both above and
# below the x axis(parallel to x-axis)). The upper bound and lower bound basically specifies that if it is crossing the upper 
# bound or lower bound , then that timestamp has some impact on the current timestamp(Useful in calculating the sales).If uss timestamp 
# pe plotted hist ka height is below that range(upper or lower) ,then that time stamp has no correlation with the current timestamp.
# This is PACF graph. This PACF graph helps us to find out AutoCorrelation.
# (Do theory part in notebook , better to write for formulas and better understanding)

# In[102]:


import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sms
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')


# In[128]:


df_airline = pd.read_csv("C:/Users/Amritanshu Bhardwaj/Downloads/AirPassengers.csv")
df_airline.head()


# In[129]:


df_airline.isnull().sum()


# In[131]:


df_airline.tail()


# In[132]:


df_airline.dropna(axis=0,inplace=True)


# In[133]:


df_airline.isnull().sum()


# In[134]:


df_airline.info()


# In[135]:


df_airline['Month'] = pd.to_datetime(df_airline['Month'])


# In[136]:


df_airline.info()


# In[137]:


df_airline.head()


# In[138]:


df_airline.set_index('Month',inplace=True)


# In[139]:


df_airline.head()


# In[140]:


df_airline.plot()  ##This looks like a seasonal data(Graphs moving continiously up and down)
## Our dataset should not be seasonal it should be stationanry


# In[141]:


from statsmodels.tsa.stattools import adfuller


# In[142]:


def adf_test(series):
    result = adfuller(series)
    print('ADF Statistics: {}'.format(result[0]))
    print('p-value:{}'.format(result[1]))
    if result[1] <= 0.05:
        print("strong evidence against the null hypothesis,reject the null hypothesis.Data has no unit root and its stationary")
    else:
        print("Weak evidence against null hypothesis,time series has unit root,indicating it is non-stationary")        


# In[143]:


adf_test(df_airline["#Passengers"])


# In[144]:


##Use Techniques Differencing(to make it stationary)(shifting by 1 as we are doing differencing by one day)
df_airline["Passengers First Difference"] = df_airline["#Passengers"] - df_airline["#Passengers"].shift(1)


# In[145]:


df_airline.head()


# In[146]:


adf_test(df_airline["Passengers First Difference"].dropna())


# In[ ]:


## Still non-stationary do second differencing(u can also directly do it from #Passengers itself by doing shift of 2)
df_airline['Passengers Second Difference'] = df_airline['Passengers First Difference']-df_airline['Passengers First Difference'].shift(1)
##Lekin kyunki first difference se nikal rhe hai isliye shift of 1 hi kiya


# In[ ]:


adf_test(df_airline['Passengers Second Difference'].dropna())  ##Now it became stationary


# In[151]:


## 12 months
## Use techniques Differencing
df_airline['Passengers 12 Difference'] = df_airline["#Passengers"]-df_airline["#Passengers"].shift(12)


# In[ ]:


adf_test(df_airline['Passengers 12 Difference'].dropna())
## If u have seasonal data go for this kind of 12 month difference


# In[149]:


from statsmodels.graphics.tsaplots import plot_acf,plot_pacf


# In[ ]:


acf = plot_acf(df_airline['Passengers Second Difference'].dropna())
## With the help of ACF we calculate a parameter called as Q


# In[ ]:


acf_12 = plot_acf(df_airline['Passengers 12 Difference'].dropna())
## Here we are going to see seasonality(Note: For seasonal data use SARIMAX only)
## Here Q value is 5 , as 5 are beyond the bounds , i.e. creating impacts (here we are not considering 0th position on x-axis)
## We don't count for 0.


# In[154]:


result = plot_pacf(df_airline['Passengers Second Difference'].dropna())


# In[158]:


pacf_12 = plot_pacf(df_airline['Passengers 12 Difference'].dropna())


# In[ ]:


## Split train and test data
df_airline


# In[159]:


from datetime import datetime,timedelta
train_dataset_end = datetime(1955,12,1)
test_dataset_end = datetime(1960,12,1)


# With Help of ACF u are performing Moving Average , u find out q value
# With the help of PACF u are performing auto regression , u find out p value

# In[160]:


train_data = df_airline[:train_dataset_end]
test_data = df_airline[train_dataset_end + timedelta(days=1):test_dataset_end]


# In[161]:


## Prediction
pred_start = test_data.index[0]
pred_end = test_data.index[-1]


# In[162]:


test_data


# In[166]:


## Create a ARIMA model
from statsmodels.tsa.arima.model import ARIMA


# In[164]:


train_data


# In[ ]:


model_ARIMA = ARIMA(train_data['#Passengers'],order=(10,2,12)) 
## 10 denotes p value when we plotted pacf curve for two time differencing(kha se we could take so that its highly crossing bounds)
# , 2 - denotes how many time we did differencing
## ,probably two times (this is not for seasonal , where we did differencing of 12) , 12 is q value in acf curve for 
## two differencing , 0th ko chor kar kha se highly bound cross hua(12 th data having a high impact)
#(p,d,q)  q is moving average , while p from pacf is auto correlation


# In[168]:


model_Arima_fit = model_ARIMA.fit()


# In[169]:


model_Arima_fit.summary()


# In[170]:


## Prediction
pred_start_date = test_data.index[0]
pred_end_date = test_data.index[-1]
print(pred_start_date)
print(pred_end_date)


# In[171]:


pred = model_Arima_fit.predict(start = pred_start_date,end = pred_end_date)
residuals = test_data['#Passengers']-pred


# In[172]:


residuals


# In[173]:


model_Arima_fit.resid.plot(kind='kde')


# In[174]:


test_data['Predicted_ARIMA'] = pred


# In[175]:


test_data[['#Passengers','Predicted_ARIMA']].plot()


# In[176]:


acf12 = plot_acf(df_airline['Passengers 12 Difference'].dropna())
pacf12 = plot_pacf(df_airline['Passengers 12 Difference'].dropna())


# In[ ]:


## Create a SARIMA model
from statsmodels.tsa.statespace.sarimax import SARIMAX
## sarima is for seasonal data 


# In[181]:


model_SARIMA = SARIMAX(train_data['#Passengers'],order=(3,0,5),seasonal_order=(0,1,0,12))
# p = 3 , as bound passing and in middle is 3 in partial autocorrelation me.
# d = 0 , as this is sarimax for seasonal
# q = 5 , as 5 is in close to middle and crossing the bound in autocorrelation


# In[182]:


model_SARIMA_fit = model_SARIMA.fit()


# In[183]:


model_SARIMA_fit.summary()


# In[184]:


test_data.tail()


# In[185]:


#prediction
pred_start = test_data.index[0]
pred_end_date = test_data.index[-1]
print(pred_start_date)
print(pred_end_date)


# In[186]:


pred_SARIMA = model_SARIMA_fit.predict(start=datetime(1956,6,6),end=datetime(1960,12,1))
residuals = test_data['#Passengers']-pred_SARIMA


# In[187]:


model_SARIMA_fit.resid.plot()


# In[188]:


model_SARIMA_fit.resid.plot(kind='kde')


# In[189]:


test_data['Predicted_SARIMA'] = pred_SARIMA


# In[190]:


test_data


# In[191]:


test_data[['#Passengers','Predicted_SARIMA','Predicted_ARIMA']].plot()

