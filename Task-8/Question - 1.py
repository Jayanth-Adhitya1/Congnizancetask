#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
Array = np.array([1,2,3,4,5])
Gap = 5
Output = np.zeros(len(Array) + (len(Array)-1)*(Gap))
Output[::Gap+1] = Array
print(Output)

