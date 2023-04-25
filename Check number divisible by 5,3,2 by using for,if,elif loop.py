#!/usr/bin/env python
# coding: utf-8

# In[2]:


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

 
# check if the number is divisible by 5
for num in numbers:
    if num % 3 == 0:
        
        print("The number", num, "is divisible by 3")
# check if the number is divisible by 3

    elif num % 5 == 0:
        print("The number", num, "is divisible by 5") 
    elif num % 2 == 0:
        print("The number", num, "is divisible by 2")
    else:
        print("The number", num, "is not divisible by 3 or 5")

