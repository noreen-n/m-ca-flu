# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 16:07:02 2024

@author: Jules
"""

import numpy as np

#dom = np.loadtxt('2-dom.txt', dtype = int)

def borders(dom):
    
    x = []
    y = []
    x_start = 0
    y_start = 0
    
    for i in range (2, dom.shape[0]-3):
        for k in range (2, dom.shape[1]-3):
            if(dom[i][k] == 2):
                
                x_start = i
                y_start = k
                break 
        else:
            continue
        break

    
    for l in range (y_start, dom.shape[1]-3):
        if(dom[x_start][l]==2):
            x.append(x_start)
            y.append(l)
            y_max = l
            
 
    for c in range(x_start+1, dom.shape[0]-3):
        if(dom[c][y_max]==2):
            x.append(c)
            y.append(y_max)
            x_max = c

    for d in range(y_max-1, y_start, -1 ):
        if(dom[x_max][d]==2):
            x.append(x_max)
            y.append(d)

    
    for j in range (x_max, x_start,-1):
        if(dom[j][y_start] ==2):
            x.append(j)
            y.append(y_start)
    x.append(x_start)
    y.append(y_start)
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

def createCl4(dom, Q, x, y, h):
    
    cl = np.zeros((dom.shape[0], dom.shape[1]))
            
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

    longueurCanal = h*(dom.shape[1]-3)
    hauteurIlot = h*(np.min(y) + (np.max(y)-np.min(y))/2 - 1)
    yIlot = int(hauteurIlot)
    
    
    for i in range(len(x)):
        cl[x[i]][y[i]] = Q*yIlot/longueurCanal
        
    return cl
            

#cl = createCl(dom, 3.5)
    