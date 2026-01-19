#!/usr/bin/env python
# coding: utf-8

# In[3]:


import yfinance as yf
import pandas as pd

# Download AAPL data
df = yf.download('AAPL', start='2010-01-01', end='2024-11-21')

# Display the first few rows
df.head()


# In[4]:


df.tail()


# In[ ]:


df1 = df.reset_index()['Close']
## df.reset_index():
#Resets the index of the DataFrame df.
#Converts the existing index (e.g., Date if it's a time-series dataset) into a regular column.

#['Close']:
#Selects only the Close column from the reset DataFrame.
#The Close column typically contains the closing prices of the AAPL stock for each trading day.


# In[8]:


df1


# In[9]:


import matplotlib.pyplot as plt
plt.plot(df1)


# In[ ]:


## LSTM are sensitive to the scale of the data . So we apply Minmax scaler


# In[10]:


import numpy as np


# In[11]:


df1


# In[12]:


from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler(feature_range=(0,1))
df1 = scaler.fit_transform(np.array(df1).reshape(-1,1))


# In[13]:


print(df1)


# In[14]:


## splitting dataset into train and test split
training_size = int(len(df1)*0.65)
test_size = len(df1)-training_size
train_data,test_data = df1[0:training_size,:],df1[training_size:len(df1),:1]

#0:training_size:
#Selects rows from the 0th index (start) up to, but not including, training_size.
##, ::
#Selects all columns (:) in those rows.
#df1[training_size:len(df1), :1]
#df1:
#Again, refers to the 2D array-like structure.
#training_size:len(df1):
#Selects rows starting from training_size to the last row (len(df1)).
#, :1:
#Selects the first column only (:1 slices from the 0th column to, but not including, the 1st column).


# In[15]:


training_size,test_size


# In[16]:


train_data


# In[17]:


import numpy
#convert an array of values into dataset matrix
def create_dataset(dataset,time_step=1):
    dataX,dataY = [],[]
    for i in range(len(dataset)-time_step-1):
        a = dataset[i:(i+time_step),0]
        dataX.append(a)
        dataY.append(dataset[i+time_step,0])
    return numpy.array(dataX),numpy.array(dataY)    


# In[18]:


time_step = 100
X_train,y_train = create_dataset(train_data,time_step)
X_test , y_test = create_dataset(test_data,time_step)


# In[19]:


print(X_train.shape),print(y_train.shape)


# In[20]:


print(X_test.shape),print(y_test.shape)


# In[21]:


## reshape input to be [samples,time steps , features] which is required for LSTM
X_train = X_train.reshape(X_train.shape[0],X_train.shape[1],1)
X_test = X_test.reshape(X_test.shape[0],X_test.shape[1],1)


# In[22]:


## Create the stacked LSTM model
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import LSTM


# In[23]:


model = Sequential()
model.add(LSTM(50,return_sequences=True,input_shape=(100,1)))
model.add(LSTM(50,return_sequences=True))
model.add(LSTM(50))
model.add(Dense(1))
model.compile(loss="mean_squared_error",optimizer='adam')


# In[25]:


model.summary()


# In[26]:


model.fit(X_train,y_train,validation_data=(X_test,y_test),epochs=100,batch_size=64,verbose=1)


# In[27]:


import tensorflow as tf


# In[28]:


tf.__version__


# In[29]:


train_predict = model.predict(X_train)
test_predict = model.predict(X_test)


# In[30]:


# Transform to original form
train_predict = scaler.inverse_transform(train_predict)
test_predict = scaler.inverse_transform(test_predict)


# In[31]:


# Calculate RMSE performance metrics
import math
from sklearn.metrics import mean_squared_error
math.sqrt(mean_squared_error(y_train,train_predict))


# In[32]:


math.sqrt(mean_squared_error(y_test,test_predict))

