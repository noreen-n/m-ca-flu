# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 16:07:02 2024

@author: Jules
"""

import numpy as np

dom = np.loadtxt('3-dom.txt', dtype = int)

def borders(dom) :
    
    x = []
    y = []

    for i in range (2, dom.shape[0]-3):
        for k in range (2, dom.shape[1]-3):
            if(dom[i][k] == 2):
                x.append(i)
                y.append(k)
    
    return x, y

x, y = borders(dom)

def createCl(dom, x, y, Q):
    
    cl = np.zeros((dom.shape[0], dom.shape[1]))
    
    for i in range(len(x)):
        for k in range(len(y)):
            if(dom[x[i]][y[k]] == 2):
                cl[x[i]][y[k]] = Q/2
            
    for i in range (2, dom.shape[0]-2):
        cl[i][1]= Q
    
    side = np.linspace(35, 0, dom.shape[1]-2)
    
    #print(len(side))
    #print(cl.shape)
    
    #print(side)
    
    clSide = np.zeros(len(side) + 2)
    clSide[0] = 0
    clSide[len(side)] = 0
    
    for i in range (0, len(side)-1):
        clSide[i+1] = side[i]

    print(cl.shape)
    print(len(clSide))
    cl[:][1] = clSide[:]
    cl[dom.shape[0]-2][:] = clSide[:]    
        
    return cl
            

cl = createCl(dom, x, y, 35)
    