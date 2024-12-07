#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as np


# In[3]:


np.Series(range(5))


# ### Changing data type to float

# In[6]:


np.Series(range(5)).astype('float')


# In[12]:


np.Series(range(5)).astype('float').mean()


# ### Changing data type to boolean

# In[9]:


np.Series(range(5)).astype('bool')


# In[13]:


np.Series(range(5)).astype('bool').sum()


# ### Changing data type to object

# In[10]:


np.Series(range(5)).astype('object')


# In[19]:


np.Series(range(5)).astype('object').sum()


# ### Changing data type int to string

# In[11]:


np.Series(range(5)).astype('string')


# In[21]:


#It will raise an error
np.Series(range(5)).astype('string').sum()


# In[18]:


np.Series(['a','b','c'])


# ### Changing string to int

# In[17]:


np.Series(['a','b','c']).astype('int')


# In[ ]:




