#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 09:55:04 2024

@author: mariebaptiste
"""

def deriv(f_left, f_c, f_right, type_left, type_c, type_right, h):
    
    if type_c == 0 :
        return 0
    #elif type_c ==2 :
    elif (type_right == 0) :
        return (f_c - f_left)/h             #deriveArriere
    elif (type_left == 0) :
        return (f_right - f_c)/h            #deriveAvant
    else :
        return (f_right - f_left)/(2*h)         #deriveCentre
        """

def deriv(f_left, f_c, f_right, type_left, type_c, type_right, h):
    
    #Sécurité
    if type_c == 0:
        v = 0
        
    #Décentrement à gauche
    elif type_right == 0:
        v = (f_c - f_left)/h
    
    #Décentrement à droite 
    elif type_left == 0:
        v = (f_right - f_c )/h
    
    else:
        v = (f_right - f_left)/(2*h)
        
    return v
    """
    