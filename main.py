#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 15:43:52 2024

@author: noreenchau
"""

import numpy as np

from Laplace import Laplace
from velocity import velocity
from pressure import pressure
from circu import circu

dom = np.loadtxt('1-dom.txt', dtype = int)
num = np.loadtxt('1-num.txt', dtype = int)
cl = np.loadtxt('1-cl.txt', dtype = float)
h = 0.5
rho = 1000
g = 9.81
C =0

x = np.array([])
y = np.array([])

for i in range (1, num.shape[0]-1):
    for j in range (1, num.shape[1]-1):
        index = num[i][j]
        x.insert((index-1), i)
        y.insert((index-1), j)

phi = Laplace(dom, num, cl)
u,v = velocity(phi, dom, h)
#pressure(rho, g, u, v, C)
circu(u, v, x, y)
