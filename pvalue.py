# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 13:34:50 2018

@author: Samantha
"""

import numpy as np
from scipy.optimize import curve_fit
from scipy.stats import chi2


#Defino la funcion por la que quiero ajustar
def funcion(x,m,b):
    return m*x+b

#Levanto los datos (acá los creo para no poner txt)
#Se levantan con datos = np.loadtxt('datos.txt')
x = np.linspace(0, 10, 100)
y_casi = funcion(x, 2, 3)
y_noise = 0.5*np.random.normal(size=x.size)
y = y_casi + y_noise
err_y = np.std(y_noise)

#Ajusto
popt, pcov = curve_fit(funcion, x, y)
ajuste_y = funcion(x, *popt)

#Defino la función que calcula la distancia de los puntos al ajuste
def err(y,f,s):
    return (y-f)/s

#Defino la variable chi2
s = sum((err(y, ajuste_y, err_y))**2)

#Los grados de libertad de la chi2 son #puntos-#parametros de la funcion
gdl = len(y)-2 
pvalue = chi2.sf(x=s, df=gdl)

print('pvalue = {}').format(pvalue)