#!/usr/bin/env python
# coding: utf-8

# In[2]:


row = int(input("Number of rows : "))
k = row - 1
for i in range(0, row):
    for j in range(0, k):
        print(end=" ")
    k = k - 1
    for j in range(0, i + 1):
        print('* ', end="")
    print()

