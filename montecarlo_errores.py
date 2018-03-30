# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 14:00:19 2018

@author: Samantha
"""

import numpy as np
from scipy.stats import norm

#Se usa para funciones que no se puedan aproximar linealmente, como 1/x
#Sup que medí una variable 'y' y quiero p=1/y

#Levanto los datos (acá los creo para no poner txt)
y_casi = np.linspace(0,10, 100)
y_noise = 0.5*np.random.normal(size=y_casi.size)
y = y_casi + y_noise
err_y = np.std(y_noise)
p = 1./y

N=int(1e4) #Genero 10000 numeros aleatorios (con distrib gaussiana)
errores = []
for i in range(0,len(y)):
    l = norm.rvs(loc=y[i], scale=err_y, size=N) #para cada 'y', genero una gaussiana
    p = 1.00/l #le aplico la funcion
    mu, std = norm.fit(p) #ajusto por una gaussiana
    errores.append(std) #me quedo con la desviacion estandar
    
print(errores) #son los errores de la variable p
