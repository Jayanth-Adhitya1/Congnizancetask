#!/usr/bin/env python
# coding: utf-8

# In[2]:


InputNumber = (input("Enter a Number : "))
OutputNumber = InputNumber[::-1]
if InputNumber == OutputNumber:
    print("The given number is a Palindrome")
else:
    print('The given number is not a Palindrome')

