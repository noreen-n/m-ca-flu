#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 16:34:14 2024

@author: mariebaptiste
"""


import numpy as np

from Laplace import Laplace
from deriv import deriv

dom = np.loadtxt('1-dom.txt', dtype = int)
num = np.loadtxt('1-num.txt', dtype = int)
cl = np.loadtxt('1-cl.txt', dtype = float)
h = 0.5

def velocity(phi, dom, h):
    
    u = np.zeros((phi.shape[0],phi.shape[1]))
    v = np.zeros((phi.shape[0],phi.shape[1]))
    
    for i in range (1, phi.shape[0]-1):
        for j in range (1, phi.shape[1]-1) :
           u[i][j] = deriv(phi[i][j-1], phi[i][j], phi[i][j+1], dom[i][j-1], dom[i][j], dom[i][j+1], h)
           v[i][j] = - (deriv(phi[i-1][j], phi[i][j], phi[i+1][j], dom[i-1][j], dom[i][j], dom[i+1][j], h))
           
    print("u")
    print(u)
    
    print("v")
    print(v)
           
    return u,v
            

phi = Laplace(dom, num, cl)
velocity(phi, dom, h)

    