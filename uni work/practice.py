# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 12:50:56 2022

@author: Mr shanu
"""
#%%
import numpy as np
from numpy import exp, sin, cos, pi
import sympy as sp
from sympy import Symbol
x=Symbol('x y')

x=[50,60,70,80,90]
y=[30,15,10,5,2]

a=[]
for i in range(len(x)):
    a.append(x[i]**0*y[i])
    totnum=np.sum(a)

    av=totnum/np.sum(y)

print("The first Moment of Marks is:",av)


#%%
import numpy as np
from numpy import exp, sin, cos, pi, sum
import sympy as sp
from sympy import Symbol
x=Symbol('x y')

x=[50,60,70,80,90]
y=[30,15,10,5,2]

d=[]
for i in range(len(x)):
    d.append(x[i]**1*y[i]) 

avg=sum(d)/sum(y)

print("The second Moment of Marks is:",avg)

#%%
import numpy as np
from numpy import exp, sin, cos, pi
import sympy
import sympy
from sympy import Symbol
x=Symbol('x y')

x=[50,60,70,80,90]
y=[30,15,10,5,2]

A=[]
for i in range(len(x)):
    A.append((x[i])**2*y[i])
totnum=np.sum(A)

z=totnum/np.sum(y)
print("The third Moment of Marks is:",z)

#%%
import numpy as np
from numpy import exp, sin, cos, pi, sum
import sympy as sp
from sympy import Symbol
x=Symbol('x y')

x=[50,60,70,80,90]
y=[30,15,10,5,2]

b=[]
for i in range(len(x)):
    b.append(x[i]**3*y[i]) 
    
aveg=sum(b)/sum(y)

print("The fourth Moment of Marks is:",aveg)

#%%
import numpy as np
from numpy import exp, sin, cos, pi, sum
import sympy
from sympy import Symbol
x=Symbol('x y')

x=[50,60,70,80,90]
y=[30,15,10,5,2]
mew=[]
for j in range(0,4):    
    a=[]
    for i in range(len(x)):
        a.append((x[i])**j*y[i])
        m = sum(a)/sum(y)
    mew.append(m)
print(mew)
