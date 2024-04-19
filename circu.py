#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 15:47:03 2024

@author: noreenchau
"""

def circu(u, v, x, y):
    
    c=0
         
    for i in range (len(x)-1):
        if (x[i] == x[i+1]):
            c = c + (y[i+1]-y[i])*((v[i]+v[i+1])/2)
        elif (y[i] == y[i+1]):
            c = c + (x[i+1]-x[i])*((u[i]+u[i+1])/2)
            
    print("circu : ", c)
    return c


