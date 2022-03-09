#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
x = np.array([1,0,5,0,8])
y = np.array([1,0,5,0,8])
print("First array:")
print(x)
print("Second array:")
print(y)
isArrayEqual = np.allclose(x, y)
if isArrayEqual:
    print("Both Arrays are Equal")
else:
    print("Both arrays are not Equal")

