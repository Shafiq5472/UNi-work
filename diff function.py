# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 00:40:11 2022

@author: shano
"""
'''
Calculate the n-th discrete difference along the given axis.

The first difference is given by out[i] = a[i+1] - a[i] along the given axis,
 higher differences are calculated by using diff recursively.
 '''
import numpy as np
x = np.array([1, 2, 4, 7, 0])
a = np.diff(x)
print(a)

b = np.diff(x, n=2)
print(b)

y = np.array([[1, 3, 6, 10], [0, 5, 6, 8]])
c = np.diff(x)
print(c)

d = np.diff(x, axis=0)
print(d)