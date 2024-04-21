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
from defineCl import createCl

#dom = np.loadtxt('2-dom.txt', dtype = int)
#num = np.loadtxt('2-num.txt', dtype = int)
#cl = createCl(dom, 3.5)

def Laplace(dom, num, cl):
    colPhi = np.array([])
    rowPhi = np.array([])
    dataPhi = np.array([])

    size = np.max(num)
    rowVector = np.array([])
    dataVector = np.array([])
   
    for i in range (1, dom.shape[0]-1):
        for k in range (1, dom.shape[1]-1):

            j,a,b = getCoeff(num[i-1, k], num[i+1, k], num[i, k-1], num[i, k+1], num[i, k], dom[i, k], cl[i, k])

            if(dom[i,k] != 0):
                colPhi = np.concatenate((colPhi, j), axis=None)
                dataPhi = np.concatenate((dataPhi, a), axis=None)   
            
            if dom[i, k] == 1:
                for l in range (5):   #mettre 5*la valeur de la ligne
                    rowPhi = np.concatenate((rowPhi, num[i, k]-1), axis=None)
            
            elif dom[i, k] == 2:    #mettre 1 fois la valeur
                rowPhi = np.concatenate((rowPhi, num[i, k]-1), axis=None)
                dataVector = np.concatenate((dataVector, b), axis=None)
                rowVector = np.concatenate((rowVector, num[i, k]-1), axis=None)
 
    
    for d in range (len(colPhi)): #parce que indices de colonnes commencent à 0
        colPhi[d] -= 1
    
    colVector = np.zeros(len(rowVector))

    A = csc_matrix((dataPhi, (rowPhi, colPhi)), shape=(size, size))
    vector = csc_matrix((dataVector, (rowVector, colVector)), shape=(size, 1))
    solution = spsolve(A, vector, permc_spec=None, use_umfpack=True)

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

#print(Laplace(dom, num, cl))