# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 13:50:13 2022

@author: SHA NU
"""

#%%
import numpy as np

a = np.array([50,40,85,64])
b = np.array([5,8,4,3])
mew=[]
for i in range(len(a)):
    mew.append(np.sum(a**i*b/np.sum(b)))
print("The value of mew is:\n",mew)
