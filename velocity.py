#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 15:48:03 2024

@author: noreenchau
"""

import numpy as np
from scipy.sparse import csc_matrix

import Laplace as laplace
from deriv import deriv

dom = np.loadtxt('1-dom.txt', dtype = int)
num = np.loadtxt('1-num.txt', dtype = int)
cl = np.loadtxt('1-cl.txt', dtype = float)
h = 0.5

def velocity(phi, dom, h):
    
    u = csc_matrix(phi.shape[0], phi.shape[1])
    v = csc_matrix(phi.shape[0], phi.shape[1])
    
    for i in range (1, phi.shape[0]-1):
        for j in range (1, phi.shape[1]-1) :
           u[i][j] = deriv(phi[i][j-1], phi[i][j], phi[i][j+1], dom[i][j-1], dom[i][j], dom[i][j+1], h)
           v[i][j] = -deriv(phi[i-1][j], phi[i][j], phi[i+1][j], dom[i-1][j], dom[i][j], dom[i+1][j], h)
           
    return u,v
            

velocity(laplace(dom, num, cl), dom, h)
    