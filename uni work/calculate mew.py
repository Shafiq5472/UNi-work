# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 10:04:23 2022

@author: SHA NU
"""

a = [88,55,65,45,15,85,97,35,15,45,88,65,15,97,28,28,45,45,88]
mark = sorted(a)
print("The sorted Marks is:",mark)

x=[]
for i in range(len(mark)):
    if mark[i-1] != mark[i]:
        x.append(mark[i])
print("The value of x is:",x)

y=[]
for i in range(len(x)):
    p=0
    for j in range(len(mark)):
        if x[i] == mark[j]:
            p=p+1
    y.append(p)
print("The value of y is:",y)

b=sum(y)
mew=[]
for i in range(4):
    z=0
    for j in range(len(x)):
        z = z + (x[j]**i*y[j]/b)
    mew.append(z)
print("The value of mew is",mew)

        
        
        
        
        
        
        