# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 23:50:16 2022

@author: shano
"""
import numpy as np

x = np.arange(6).reshape(2,3)
print(x)
print("--------------------")
y = np.argwhere(x>1)
print(y)


