#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 15:48:21 2024

@author: noreenchau
"""

from getCoeff import getCoeff 
import numpy as np

from scipy.sparse import csc_matrix
from scipy.sparse.linalg import spsolve


dom = np.loadtxt('1-dom.txt', dtype = int) #essayer d'enlever les dtype
num = np.loadtxt('1-num.txt', dtype = int)
cl = np.loadtxt('1-cl.txt', dtype = float)

def Laplace(dom, num, cl):
    
    colonne = np.array([])
    ligne = np.array([])
    data = np.array([])
    vecteur = np.array([])
    
    for i in range (1, dom.shape[0]-1):
        for k in range (1, dom.shape[1]-1):
            
            j,a,b = getCoeff(num[i-1, k], num[i+1, k], num[i, k-1], num[i, k+1], num[i, k], dom[i, k], cl[i, k])
            
            colonne = np.concatenate((colonne, j), axis=None)
            
            if dom[i, k] == 1:
                for l in range (5):   #mettre 5*la valeur de la ligne
                    ligne = np.concatenate((ligne, num[i, k]-1), axis=None)
            elif dom[i, k] == 2:    #mettre 1 fois la valeur
                ligne = np.concatenate((ligne, num[i, k]-1), axis=None)
                
            data = np.concatenate((data, a), axis=None)
            vecteur = np.concatenate((vecteur, b), axis=None)
    
    taille = (dom.shape[0]-2)*(dom.shape[1]-2)
    for d in range (len(colonne)):
        colonne[d] = colonne[d]-1
    
    print("taille :", taille)
    
    print("ligne :", ligne)
    print("colonne :", colonne)
    
    print("data :", data)
    
    A = csc_matrix((data, (ligne, colonne)), shape=(taille, taille))
    
    print("A")
    print(A)
    
    print("vecteur")
    print(vecteur)
    
    solution = spsolve(A, vecteur, permc_spec=None, use_umfpack=True) #Voir remettre sous forme de matrice 
    
    print("solution")
    print(solution)
            
            
    
Laplace(dom, num ,cl)
    
