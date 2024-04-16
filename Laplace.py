#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 13:08:26 2024

@author: noreenchau
"""
 
from getCoeff import getCoeff 
import numpy as np

from scipy.sparse import csc_matrix
from scipy.sparse.linalg import spsolve

def Laplace(dom, num, cl):
    colonne = np.array([])
    ligne = np.array([])
    data = np.array([])
    cols = np.array([])

    dim = np.max(num)
    vecteur = np.zeros(dim)
    
    #print(vecteur)

   
    for i in range (1, dom.shape[0]-1):
        for k in range (1, dom.shape[1]-1):

            j,a,b = getCoeff(num[i-1, k], num[i+1, k], num[i, k-1], num[i, k+1], num[i, k], dom[i, k], cl[i, k])
            
            vecteur[num[i, k]-1] = b
            
            if dom[i,k]!=0 :
                colonne = np.concatenate((colonne, j), axis=None)
                data = np.concatenate((data, a), axis=None)
            
            if dom[i, k] == 1:
                for l in range (5):   #mettre 5*la valeur de la ligne
                    ligne = np.concatenate((ligne, num[i, k]-1), axis=None)
            elif dom[i, k] == 2:    #mettre 1 fois la valeur
                ligne = np.concatenate((ligne, num[i, k]-1), axis=None)


    taille = 80240#(dom.shape[0]-2)*(dom.shape[1]-2) ???
 
    for d in range (len(colonne)):
        colonne[d] -=1
        
    A = csc_matrix((data, (ligne, colonne)), shape=(taille, taille))
    

    solution = spsolve(A, vecteur, permc_spec=None, use_umfpack=True)

    #print("solution")    
    #print(solution)
    
    matriceSolution = np.zeros((num.shape[0],num.shape[1]))
    
    for i in range (1, num.shape[0]-1):
        for j in range (1, num.shape[1]-1):
            index = num[i][j]
            matriceSolution[i][j] = solution[index-1]  
            
    #print("matrice solution")
    #print(matriceSolution)
            
    return matriceSolution
