#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 15:47:21 2024

@author: noreenchau
"""

def deriv(f_left, f_c, f_right, type_left, type_c, type_right, h):
    
    if type_c == 1 :
        return (f_right - f_left)/(2*h)         #deriveCentre
    elif type_right == 0 :
        return (f_c - f_left)/h             #deriveArriere
    elif type_left == 0 :
        return (f_right - f_c)/h            #deriveAvant
    
