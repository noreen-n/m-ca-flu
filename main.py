#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 15:43:52 2024

@author: noreenchau
"""

import numpy as np

import matplotlib.pyplot as plt

from Laplace import Laplace
from velocity import velocity
from pressure import pressure
from circu import circu
from force import force

dom = np.loadtxt('1-dom.txt', dtype = int)
num = np.loadtxt('1-num.txt', dtype = int)
cl = np.loadtxt('1-cl.txt', dtype = float)
h = 0.5
rho = 1000
g = 9.81
C =0

phi = Laplace(dom, num, cl)
u,v = velocity(phi, dom, h)
p = pressure(rho, g, u, v, C)
print(u)
uArray = []
vArray = [] 

dim = np.max(num)
x = np.zeros(dim) 
y = np.zeros(dim)  # x et y pas juste doivent être les coordonnées du contour de l'ilot en partant d'un point puis sens des aiguille d'une montre
pArray = []

for i in range (1, num.shape[0]-1):
    for j in range (1, num.shape[1]-1):
        index = num[i][j]
        x[index-1] = i
        y[index-1] = j
        uArray.insert(index-1, u[i][j])
        vArray.insert(index-1, v[i][j])
        pArray.insert(index-1, u[i][j])
        
#xArray = np.array(x)
print("x")
print(x)
#yArray = np.array(y)
print("y")
print(y)

        
circu(uArray, vArray, x, y)
force(pArray, x, y)

fig,ax = plt.subplots()

#plt.subplot(1, 3, 1)
#plt.plot(u)
#plt.title("u")
#plt.subplot(1, 3, 2)
#plt.plot(v)
#plt.title("v")
#plt.subplot(1,3,3)
#plt.plot(p)
#plt.title("p")

dimension = u.shape[0]

m = np.arange(0, dimension, 1)
n = np.arange(0, dimension, 1)

#p2 = ax.imshow(u)
strm=ax.streamplot(m, n, u, v, 1) #plus pour vitesse
#fig.colorbar(p2)
#fig.color(p2)
# ou strm à la place de p2
