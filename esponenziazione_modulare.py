# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 15:15:36 2020

@author: loren

Esponenziazione modulare
"""

def modexp(p, g, x):
    result = 1
    while x > 0:
        result = (result * g) % p
        x = x - 1