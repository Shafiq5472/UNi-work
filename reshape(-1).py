# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 00:49:00 2022

@author: shano
"""
'''
numpy allow us to give one of new shape parameter as -1 (eg: (2,-1) or (-1,3) but not (-1, -1)).
 It simply means that it is an unknown dimension and we want numpy to figure it out.
 And numpy will figure this by looking at the 'length of the array and remaining dimensions'
 and making sure it satisfies the above mentioned criteria
 '''



import numpy as np

a = np.matrix([[1, 2, 3, 4], [5, 6, 7, 8]])
b = np.reshape(a, -1)
print(b)