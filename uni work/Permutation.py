# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 10:41:21 2022

@author: SHA NU
"""

# A Python program to print all
# permutations using library function
from itertools import permutations

# Get all permutations of [1, 2, 3]
perm = permutations([1, 2, 3])

# Print the obtained permutations
for i in list(perm):
    print (i)
    
perm = permutations([1, 2, 3], 2)
# Print the obtained permutations
for i in list(perm):
    print (i)