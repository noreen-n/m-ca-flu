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
#parcours en sens horloger
def borderss(dom):
    
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
            y.append(l)
    
    for d in range(dom.shape[1]-3, 0, -1 ):
        if(dom[c][d]==2):
            x.append(dom.shape[0]-1-x_start)
            y.append(d)

    
    for j in range (dom.shape[0]-3, x_start,-1):
        if(dom[j][y_start] ==2):
            x.append(j)
            y.append(y_start)
    x.append(x_start)
    y.append(y_start)
    return x, y

def createCl(dom, x, y, Q):
    
    cl = np.zeros((dom.shape[0], dom.shape[1]))
    
    for i in range(len(x)):
        for k in range(len(y)):
            if(dom[int(x[i])][int(y[k])] == 2):
                cl[int(x[i])][int(y[k])] = Q/2
            
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
            

#cl = createCl(dom, x, y, 35)
    
