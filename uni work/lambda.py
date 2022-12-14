# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 19:25:29 2022

@author: shano
"""

import scipy.optimize
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.style

matplotlib.style.use('fivethirtyeight')
%matplotlib inline

f = lambda x: np.cos(x) - x
g = np.sin

h = lambda x: f(x) - g(x)

x = np.linspace(0,3,100)
plt.plot(x, f(x), zorder=1)
plt.plot(x, g(x), zorder=1)

x_int = scipy.optimize.fsolve(h, 1.0)
y_int = f(x_int)

plt.scatter(x_int, y_int, marker='x', s=150, zorder=2, 
            linewidth=2, color='black')

plt.xlim([0,3])
plt.ylim([-4,2])