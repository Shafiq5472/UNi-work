# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 13:53:53 2022

@author: SHA NU
"""


""""Differenciation"""

import sympy as sp
from sympy import diff,Derivative,Symbol,exp,sin,simplify

x = Symbol('x')

def g(x):
    return x**3*exp(x**2)

z= simplify(diff(g(x),x))
print("The differenciation of g(x) is:",z)

"Practice"
def f(x):
    return x**2 + 4*x
def q(x):
    return x**5*5 +2*x +85
r = f(x)+q(x)
a = simplify(diff(r,x))
print("The differenciation of f(x) is:",a)