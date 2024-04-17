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
from defineCl import createCl
from defineCl import borders

rho = 1000
g = 9.81
C =0

def main(cas):
    
    if cas == 1:
        h = 0.5
        dom = np.loadtxt('1-dom.txt', dtype = int)
        num = np.loadtxt('1-num.txt', dtype = int)
        cl = np.loadtxt('1-cl.txt', dtype = float)
        
        phi = Laplace(dom, num, cl)
        u,v = velocity(phi, dom, h)
        p = pressure(rho, g, u, v, C)
        
        fig,ax = plt.subplots()
        plt.gca().invert_yaxis()
        p1 = ax.imshow(phi, extent=(0, np.shape(cl)[1]*h, np.shape(dom)[0]*h, 0), cmap='inferno')
        plt.colorbar(p1)
        plt.title("Fonction de courant")
        
        fig,ax = plt.subplots()
        plt.gca().invert_yaxis()
        p1 = ax.imshow(u, extent=(0, np.shape(cl)[1]*h, np.shape(dom)[0]*h, 0), cmap='inferno')
        plt.colorbar(p1)
        plt.title("Vitesse u")
        
        fig,ax = plt.subplots()
        plt.gca().invert_yaxis()
        p1 = ax.imshow(v, extent=(0, np.shape(cl)[1]*h, np.shape(dom)[0]*h, 0), cmap='inferno')
        plt.colorbar(p1)
        plt.title("Vitesse v")
        
        fig,ax = plt.subplots(figsize=(3, 7))
        plt.gca().invert_yaxis()
        plt.gca().invert_yaxis()
        dimension1 = u.shape[0]
        dimension2 = u.shape[1]
        m = np.arange(0, dimension1*h, h)
        n = np.arange(0, dimension2*h, h)
        N, M = np.meshgrid(n, m)
        plt.title("Lignes de courant")
        strm=ax.streamplot(N, M, v, u, 1)
        
        fig,ax = plt.subplots()
        plt.gca().invert_yaxis()
        p1 = ax.imshow(p, extent=(0, np.shape(cl)[1]*h, np.shape(dom)[0]*h, 0), cmap='inferno')
        plt.colorbar(p1)
        plt.title("Pression")
        
        
        
    if cas == 2:
        h = 2
        dom = np.loadtxt('2-dom.txt', dtype = int)
        num = np.loadtxt('2-num.txt', dtype = int)
        x,y = borders(dom)
        cl = createCl(dom, 3.5)
        
        phi = Laplace(dom, num, cl)
        
        u,v = velocity(phi, dom, h)
        p = pressure(rho, g, u, v, C)

        #dim = np.max(num)
        #xx = np.zeros(dim) 
        #yy = np.zeros(dim)
        uArray = []
        vArray = []
        pArray = []

        for i in range (1, num.shape[0]-1):
            for j in range (1, num.shape[1]-1):
                index = num[i][j]
                #xx[index-1] = i
                #yy[index-1] = j
                uArray.insert(index-1, u[i][j])
                vArray.insert(index-1, v[i][j])
                pArray.insert(index-1, p[i][j])
        
        circu(uArray, vArray, x, y)
        force(pArray, x, y)
                
        fig,ax = plt.subplots()
        plt.gca().invert_yaxis()
        p1 = ax.imshow(phi, extent=(0, np.shape(cl)[1]*h, np.shape(dom)[0]*h, 0), cmap='inferno')
        plt.colorbar(p1)
        plt.title("Fonction de courant")
        
        fig,ax = plt.subplots()
        plt.gca().invert_yaxis()
        p1 = ax.imshow(u, extent=(0, np.shape(cl)[1]*h, np.shape(dom)[0]*h, 0), cmap='inferno')
        plt.colorbar(p1)
        plt.title("Vitesse u")
        
        fig,ax = plt.subplots()
        plt.gca().invert_yaxis()
        p1 = ax.imshow(v, extent=(0, np.shape(cl)[1]*h, np.shape(dom)[0]*h, 0), cmap='inferno')
        plt.colorbar(p1)
        plt.title("Vitesse v")
    
        fig,ax = plt.subplots(figsize=(3, 7))
        plt.gca().invert_yaxis()
        dimension1 = u.shape[0]
        dimension2 = u.shape[1]
        m = np.arange(0, dimension1*h, h)
        n = np.arange(0, dimension2*h, h)
        N, M = np.meshgrid(n, m)
        plt.title("Lignes de courant")
        strm=ax.streamplot(N, M, v, u, 1)
        
        fig,ax = plt.subplots()
        plt.gca().invert_yaxis()
        p1 = ax.imshow(p, extent=(0, np.shape(cl)[1]*h, np.shape(dom)[0]*h, 0), cmap='inferno')
        plt.colorbar(p1)
        plt.title("Pression")
        
        
        
    if cas == 3:
        h = 2
        dom = np.loadtxt('3-dom.txt', dtype = int)
        num = np.loadtxt('3-num.txt', dtype = int)
        x,y = borders(dom)
        cl = createCl(dom, 3.5)
        
        phi = Laplace(dom, num, cl)
        u,v = velocity(phi, dom, h)
        p = pressure(rho, g, u, v, C)
        
        fig,ax = plt.subplots()
        plt.gca().invert_yaxis()
        p1 = ax.imshow(phi, extent=(0, np.shape(cl)[1]*h, np.shape(dom)[0]*h, 0), cmap='inferno')
        plt.colorbar(p1)
        plt.title("Fonction de courant")
        
        fig,ax = plt.subplots()
        plt.gca().invert_yaxis()
        p1 = ax.imshow(u, extent=(0, np.shape(cl)[1]*h, np.shape(dom)[0]*h, 0), cmap='inferno')
        plt.colorbar(p1)
        plt.title("Vitesse u")
        
        fig,ax = plt.subplots()
        plt.gca().invert_yaxis()
        p1 = ax.imshow(v, extent=(0, np.shape(cl)[1]*h, np.shape(dom)[0]*h, 0), cmap='inferno')
        plt.colorbar(p1)
        plt.title("Vitesse v")
        
        fig,ax = plt.subplots(figsize=(3, 7))
        plt.gca().invert_yaxis()
        dimension1 = u.shape[0]
        dimension2 = u.shape[1]
        m = np.arange(0, dimension1*h, h)
        n = np.arange(0, dimension2*h, h)
        N, M = np.meshgrid(n, m)
        plt.title("Lignes de courant")
        strm=ax.streamplot(N, M, v, u, 1)
        
        fig,ax = plt.subplots()
        plt.gca().invert_yaxis()
        p1 = ax.imshow(p, extent=(0, np.shape(cl)[1]*h, np.shape(dom)[0]*h, 0), cmap='inferno')
        plt.colorbar(p1)
        plt.title("Pression")
        
        
        
    if cas == 4:
        h = 2
        dom = np.loadtxt('4-dom.txt', dtype = int)
        num = np.loadtxt('4-num.txt', dtype = int)
        contour = np.loadtxt('4-contourObj.txt', dtype = int)
        
        x = np.zeros(contour.shape[0])
        y = np.zeros(contour.shape[0])
        
        for i in range (contour.shape[0]):
            x[i] = contour[i][0]
            y[i] = contour[i][1]
            
        # prendre x et y par rapport au doc contour
        cl = createCl(dom, 3.5)
        
        phi = Laplace(dom, num, cl)
        u,v = velocity(phi, dom, h)
        p = pressure(rho, g, u, v, C)
        
        fig,ax = plt.subplots()
        plt.gca().invert_yaxis()
        p1 = ax.imshow(phi, extent=(0, np.shape(cl)[1]*h, np.shape(dom)[0]*h, 0), cmap='inferno')
        plt.colorbar(p1)
        plt.title("Fonction de courant")
        
        fig,ax = plt.subplots()
        plt.gca().invert_yaxis()
        p1 = ax.imshow(u, extent=(0, np.shape(cl)[1]*h, np.shape(dom)[0]*h, 0), cmap='inferno')
        plt.colorbar(p1)
        plt.title("Vitesse u")
        
        fig,ax = plt.subplots()
        plt.gca().invert_yaxis()
        p1 = ax.imshow(v, extent=(0, np.shape(cl)[1]*h, np.shape(dom)[0]*h, 0), cmap='inferno')
        plt.colorbar(p1)
        plt.title("Vitesse v")
        
        fig,ax = plt.subplots(figsize=(3, 7))
        plt.gca().invert_yaxis()
        dimension1 = u.shape[0]
        dimension2 = u.shape[1]
        m = np.arange(0, dimension1*h, h)
        n = np.arange(0, dimension2*h, h)
        N, M = np.meshgrid(n, m)
        plt.title("Lignes de courant")
        strm=ax.streamplot(N, M, v, u, 1)
        
        fig,ax = plt.subplots()
        plt.gca().invert_yaxis()
        p1 = ax.imshow(p, extent=(0, np.shape(cl)[1]*h, np.shape(dom)[0]*h, 0), cmap='inferno')
        plt.colorbar(p1)
        plt.title("Pression")
        
main(4)


