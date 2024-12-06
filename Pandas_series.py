#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# ### Creating a Series from list, 

# In[31]:


data = [10,20,30,40,50]
s1= pd.Series(data)
print(s1)


# ### Creating a Series from Dictionary

# In[22]:


dict =  {'a': '10', 'b' :'20', 'c': '30','d':'40'}
s2 = pd.Series(dict, name= 'mine')
print(s2)


# ### Creating list from Numpy array

# In[27]:


numpy = np.array([1,2,3,4])
s3 = pd.Series(numpy,name = 'Rimsha',dtype = int)
print(s3)


# ### Element-wise Operations

# In[34]:


s1 + 5


# ### Series must be one dimensional

# In[41]:


pd.Series(np.arange(15,25))


# In[42]:


pd.Series(np.arange(15,25).reshape(5,2))


# In[ ]:




