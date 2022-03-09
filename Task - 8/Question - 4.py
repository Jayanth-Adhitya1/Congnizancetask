#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
x = pd.Series(['amrita', 'school', 'of', 'engineering' 'chennai' , 'campus'])
y = x.str.capitalize()
print(y)

