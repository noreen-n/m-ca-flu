#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 15:47:33 2024

@author: noreenchau
"""

def force(p, x, y):
    
    fx=0
    fy=0
    
    for i in range (len(p)-1):
        fx = fx - ((p[i]+p[i+1])/2)*(y[i]-y[i+1])
        fy = fy + ((p[i]+p[i+1])/2)*(x[i]-x[i+1])
    
    print("trainée")
    print(fx)
    print("portance")
    print(fy)
    return fx,fy

