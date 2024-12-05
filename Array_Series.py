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


# ### Sorting

# In[23]:


prices = np.array([5.99, 6.99, 22.49, 99.99, 4.99, 49.99])

prices.sort()


# In[24]:


prices


# In[26]:


top3 = prices[-3:]
top3


# In[27]:


print(f"Mean: {top3.mean()}")
print(f"Min: {top3.min()}")
print(f"Max: {top3.max()}")
print(f"Median: {np.median(top3)}")


# In[28]:


price_tiers = np.array(["budget", "budget", "mid-tier", "luxury", "mid-tier", "luxury"])


# In[29]:


np.unique(price_tiers)


# In[ ]:




