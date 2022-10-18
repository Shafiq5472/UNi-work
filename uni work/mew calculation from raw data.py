# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 14:21:35 2022

@author: Mr Kakarotto
"""

import numpy as np
data=[1,2,2,3,1,4,6,9,20,4,4,9,10,10,12,12,13,13,14,13]
data1=sorted(data)
print("Sorted data1 is",data1)
x=[]
y=[] 
for i in range(len(data1)):
    if data1[i-1] != data1[i]:
        x.append(data1[i])
print("The value of x is",x)

for i in range(len(x)):
    k=0
    for j in range(len(data1)):
        if x[i]==data1[j]:
            k=k+1
    y.append(k)
print("The value of y is",y)    

mew=[]
for i in range(4):
    z=0
    for j in range(len(x)):
        z=z+((x[j]**i*y[j])/np.sum(y))
    mew.append(z)
print("The value of mew is",mew)    
    
