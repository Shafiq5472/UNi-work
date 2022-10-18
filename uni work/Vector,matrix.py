# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 11:40:29 2022

@author: SHA NU
"""
import numpy as np
from numpy import matrix,transpose,dot
import sympy as sp
from sympy import Symbol
x=Symbol('x y')

"VECTOR and matrix"
x = matrix([[50,60,70],[65,75,85],[69,78,98]])
y = transpose (matrix([3,5,9]))

c = dot(x,y)
print("The dot product of x and y is:\n",c)


"practice"
a = matrix([[12,2,3,4],[7,9,5,8],[7,0,0,9],[0,1,0,12]])
b = transpose(matrix([[1,4,3,0],[12,85,17,36],[1,8,56,0]]))

d = dot(a,b)
print("The dot product of x and y is:\n",d)