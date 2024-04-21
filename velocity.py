#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 16:34:14 2024

@author: mariebaptiste
"""


import numpy as np

from deriv import deriv


def velocity(phi, dom, h):
    
    u = np.zeros((phi.shape[0],phi.shape[1]))
    v = np.zeros((phi.shape[0],phi.shape[1]))
    
    for i in range (phi.shape[0]):
        for j in range (phi.shape[1]) :
            if(dom[i, j] != 0):
                u[i][j] = deriv(phi[i][j-1], phi[i][j], phi[i][j+1], dom[i][j-1], dom[i][j], dom[i][j+1], h)
                v[i][j] = - deriv(phi[i-1][j], phi[i][j], phi[i+1][j], dom[i-1][j], dom[i][j], dom[i+1][j], h)

    return u,v
            

    