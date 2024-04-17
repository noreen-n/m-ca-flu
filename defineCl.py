# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 16:07:02 2024

@author: Jules
"""

import numpy as np


dom = np.loadtxt('2-dom.txt', dtype = int)

def borders(dom) :
    
    x = []
    y = []

    for i in range (2, dom.shape[0]-3):
        for k in range (2, dom.shape[1]-3):
            if(dom[i][k] == 2):
                x.append(i)
                y.append(k)
    
    return x, y

def createCl(dom, Q):
    
    x,y = borders(dom)
    cl = np.zeros((dom.shape[0], dom.shape[1]))
    
    for i in range(len(x)):
        for k in range(len(y)):
            if(dom[x[i]][y[k]] == 2):
                cl[x[i]][y[k]] = Q/2
            
    for i in range (2, dom.shape[0]-2):
        cl[i][dom.shape[1]-2]= Q
    
    side = np.linspace(0, Q, dom.shape[1]-2)
    
    clSide = np.zeros(len(side) + 2)
    
    for i in range(len(side)):
        clSide[i+1] = side[i]

    #print(cl.shape)
    #print(len(clSide))
    cl[:][1] = clSide[:]
    cl[dom.shape[0]-2][:] = clSide[:]    
        
    return cl
            

#cl = createCl(dom, 3.5)
    