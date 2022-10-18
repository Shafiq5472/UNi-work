# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 14:21:23 2022

@author: SHA NU
"""

import scipy
from scipy.integrate import simpson

import sympy
from sympy import Symbol,exp,sin,cos,log,simplify,pi

import matplotlib.pyplot as plt


"NUMERICAL INTEGRATION"
x = [1,2,3,4,5,6]

def f(x):
    return x**3 - 5

y =[]
for i in range (len(x)):
    y.append(f(x[i]))
I = scipy.integrate.simpson(y,x)
plt.plot(y,x)
plt.xlabel('x')
plt.ylabel('y')

print("The value of y is:",y)
print("The integration of I w.r.t x is:",I)
