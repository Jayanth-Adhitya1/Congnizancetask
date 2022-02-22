#!/usr/bin/env python
# coding: utf-8

# In[2]:


List = [["Roll_No", "Name", "Marks"], [1, "Akkil", 85], [2, "Anush", 94], [3, "Bawan", 69]]
#1
for i in List:
    for x in i:
        print(x,end=" ")
    print()
#2
print(List[2])

