#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 15:47:51 2024

@author: noreenchau
"""

import numpy as np 

def pressure(rho, g, u, v, C):
    
    p = np.zeros((u.shape[0], u.shape[1]))
    
    for i in range (1, u.shape[0]-1):
        for j in range (1, u.shape[1]-1):
           p[i][j] = rho*g*(C - (u[i][j]**2 + v[i][j]**2)/(2*g))
    
    #print("p")
    #print(p)
    return p


