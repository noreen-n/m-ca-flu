#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 15:47:33 2024

@author: noreenchau
"""

import numpy as np

def force(p, x, y):
    
    fx=0
    fy=0
    
    for i in range (len(x)-1):
        fx = fx + p[i]*(x[i+1]*y[i]-x[i]*y[i])
        fy = fy + p[i]*(x[i]*y[i+1]-x[i]*y[i])
    
    
    return fx,fy

p = np.array([3,4,5,7,3])
x = np.array([0,0,3,3,0])
y = np.array([0,3,3,0,0])
fx,fy = force(p,x,y)
print(fx)
print(fy)

force(p, x, y)
    