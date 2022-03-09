#!/usr/bin/env python
# coding: utf-8

# In[8]:


import numpy as np

X = ([1, 2, 3], [2, 3, 4], [3, 4, 5])
Y = ([4, 5, 6], [5, 6, 7], [6, 7, 8])
Sum = np.add(X, Y)
Product = np.dot(X, Y)
print("The Sum of the two arrays are: ")
print(Sum)
print("The Product of the two arrays are: ")
print(Product)

