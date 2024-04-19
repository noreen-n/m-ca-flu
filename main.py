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
from defineCl import borders, borderss

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
        
        """x,y = borderss(dom)
        
        uArray = np.zeros(len(x))
        vArray = np.zeros(len(x))
        pArray = np.zeros(len(x))
        
        for pr in range (0, len(x)-1): # -1 ou -2 en fonction de si on doit boucler la boucle ou pas
            pArray[pr] = p[x[pr]][y[pr]]
            uArray[pr] = u[x[pr]][y[pr]]
            vArray[pr] = v[x[pr]][y[pr]]
            
        pArray[len(x)-1] = p[x[0]][y[0]]
        uArray[len(x)-1] = u[x[0]][y[0]]
        vArray[len(x)-1] = v[x[0]][y[0]]
        
        circu(uArray, vArray, x, y)
        force(pArray, x, y)"""
        
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
        strm=ax.streamplot(N, M, v, u, 0.9, broken_streamlines=False)
        
        fig,ax = plt.subplots()
        plt.gca().invert_yaxis()
        p1 = ax.imshow(p, extent=(0, np.shape(cl)[1]*h, np.shape(dom)[0]*h, 0), cmap='inferno')
        plt.colorbar(p1)
        plt.title("Pression")
        
        
        
    if cas == 2:
        h = 2
        dom = np.loadtxt('2-dom.txt', dtype = int)
        num = np.loadtxt('2-num.txt', dtype = int)
        x,y = borderss(dom)
        cl = createCl(dom, 3.5)
        
        phi = Laplace(dom, num, cl)
        
        u,v = velocity(phi, dom, h)
        p = pressure(rho, g, u, v, C)

        uArray = np.zeros(len(x))
        vArray = np.zeros(len(x))
        pArray = np.zeros(len(x))
        
        for pr in range (0, len(x)-1): 
            pArray[pr] = p[x[pr]][y[pr]]
            uArray[pr] = u[x[pr]][y[pr]]
            vArray[pr] = v[x[pr]][y[pr]]
            
        pArray[len(x)-1] = p[x[0]][y[0]]
        uArray[len(x)-1] = u[x[0]][y[0]]
        vArray[len(x)-1] = v[x[0]][y[0]]
        
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
        strm=ax.streamplot(N, M, v, u, 0.8, broken_streamlines=False)
        
        fig,ax = plt.subplots()
        plt.gca().invert_yaxis()
        p1 = ax.imshow(p, extent=(0, np.shape(cl)[1]*h, np.shape(dom)[0]*h, 0), cmap='inferno')
        plt.colorbar(p1)
        plt.title("Pression")
        
        
        
    if cas == 3:
        h = 2
        dom = np.loadtxt('3-dom.txt', dtype = int)
        num = np.loadtxt('3-num.txt', dtype = int)
        x,y = borderss(dom)
        cl = createCl(dom, 3.5)
        
        phi = Laplace(dom, num, cl)
        u,v = velocity(phi, dom, h)
        p = pressure(rho, g, u, v, C)
        
        uArray = np.zeros(len(x))
        vArray = np.zeros(len(x))
        pArray = np.zeros(len(x))
        
        for pr in range (0, len(x)-1): 
            pArray[pr] = p[x[pr]][y[pr]]
            uArray[pr] = u[x[pr]][y[pr]]
            vArray[pr] = v[x[pr]][y[pr]]
            
        pArray[len(x)-1] = p[x[0]][y[0]]
        uArray[len(x)-1] = u[x[0]][y[0]]
        vArray[len(x)-1] = v[x[0]][y[0]]
        
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
        strm=ax.streamplot(N, M, v, u, 0.9, broken_streamlines=False)
        
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
            
        cl = createCl(dom, 3.5)
        
        phi = Laplace(dom, num, cl)
        u,v = velocity(phi, dom, h)
        p = pressure(rho, g, u, v, C)
        
        uArray = np.zeros(len(x))
        vArray = np.zeros(len(x))
        pArray = np.zeros(len(x))
        
        for pr in range (0, len(x)-1): 
            pArray[pr] = p[int(x[pr])][int(y[pr])]
            uArray[pr] = u[int(x[pr])][int(y[pr])]
            vArray[pr] = v[int(x[pr])][int(y[pr])]
            
        pArray[len(x)-1] = p[int(x[0])][int(y[0])]
        uArray[len(x)-1] = u[int(x[0])][int(y[0])]
        vArray[len(x)-1] = v[int(x[0])][int(y[0])]
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
        strm=ax.streamplot(N, M, v, u, 0.9, broken_streamlines=False)
        
        fig,ax = plt.subplots()
        plt.gca().invert_yaxis()
        p1 = ax.imshow(p, extent=(0, np.shape(cl)[1]*h, np.shape(dom)[0]*h, 0), cmap='inferno')
        plt.colorbar(p1)
        plt.title("Pression")
        
main(4)


