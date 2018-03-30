# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 13:57:15 2018

@author: Samantha
"""

def promedio4(vector):
    vector_prolijo = []
    for i in range((len(vector)-1)/4):
        vector_prolijo.append((vector[4*i+3]+vector[4*i+2] + vector[4*i+1] + vector[4*i])/4.)
    return vector_prolijo

def promedio2(vector):
    vector_prolijo = []
    for i in range((len(vector)-1)/2):
        vector_prolijo.append((vector[2*i+1] + vector[2*i])/2.)
    return vector_prolijo