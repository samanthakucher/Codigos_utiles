# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 14:25:49 2018

@author: Samantha
"""

import numpy as np
from scipy.optimize import curve_fit
from scipy import stats

def lineal(x,m,b):
    return m*x+b

#Levanto los datos (acá los creo para no poner txt)
x = np.linspace(0, 10, 100)
y_casi = lineal(x, 2, 3)
y_noise = 0.5*np.random.normal(size=x.size)
y = y_casi + y_noise
#faltan los errores

#polyfit sirve para polinomios en general
m,b = np.polyfit(x, y, 1) 

#curve fit sirve para funciones en general, y te da los errores de los parametros
popt, pcov = curve_fit(lineal, x, y)

#linregress sirve solo para lineales, y ya te da el R^2 y el p-value
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)