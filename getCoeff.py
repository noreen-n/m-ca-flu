#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 15:38:34 2024

@author: mariebaptiste
"""

import numpy as np

def getCoeff(num_left, num_right, num_down, num_up, num_cent, type_cent, cl_cent):

    if type_cent == 1 :
        j = np.array([num_left, num_right, num_down, num_up, num_cent])
        b = 0
        a = np.array([1, 1, 1, 1, -4])
        return j,a,b

    elif type_cent == 2 :
        j = np.array([num_cent])
        b = cl_cent
        a = np.array([1])
        return j,a,b

    else :
        return 0,0,0