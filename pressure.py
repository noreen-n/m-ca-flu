#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 15:47:51 2024

@author: noreenchau
"""

rho = 1000
g = 9.81
C =0

from Laplace import Laplace
from velocity import velocity

import numpy as np 

#dom = np.loadtxt('1-dom.txt', dtype = int)
#num = np.loadtxt('1-num.txt', dtype = int)
#cl = np.loadtxt('1-cl.txt', dtype = float)
#h = 0.5

def pressure(rho, g, u, v, C):
    
    p = np.zeros((u.shape[0], u.shape[1]))
    
    for i in range (1, u.shape[0]-1):
        for j in range (1, u.shape[1]-1):
           p[i][j] = rho*g*(C - (u[i][j]**2 + v[i][j]**2)/2*g)
    
    print("p")
    print(p)
    return p


#phi = Laplace(dom, num, cl)
#u,v = velocity(phi, dom, h)
#pressure(rho, g, u, v, C)

