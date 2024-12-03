#!/usr/bin/env python
# coding: utf-8

# In[3]:


get_ipython().system('conda install pandas==1.5.3')


# In[4]:


import numpy as np
import pandas as pd


# In[10]:


pd.Series(np.arange(5),name='data')


# In[12]:


ser = pd.Series(np.arange(5))


# In[13]:


ser.mean()


# In[17]:


ser.values


# In[16]:


ser.index= [10,20,30,40,50]


# In[21]:


ser


# In[20]:


ser.name='Series name'


# In[22]:


ser.dtype


# In[ ]:




