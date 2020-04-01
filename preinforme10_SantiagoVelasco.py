# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 12:15:45 2020

@author: david
"""

import numpy as np

def utilidadKellogs():
    utilidad = np.array([int(27834), int(23789), int(30189), 
                         int(30967), int(32501), int(32701),
                         int(31665), int(17155), int(4614), int(834)])
    return utilidad

# Punto 1

def difeMedia(utilidad):
    long = len(utilidad)
    prome1 = (utilidad[long-1]+utilidad[long-2])/2
    prome2 = (utilidad[0]+utilidad[1])/2
    difMedia = prome1-prome2
    print('La diferencia en el promedio de la utilidad operacional en ' +
          'los últimos 2 años comparada con los primeros 2 es de $'
          + str(difMedia) + ' millones de pesos.\n')
    
# Punto 2

def mayorUlt(utilidad):
    mayor = utilidad[0]
    long = len(utilidad)
    for i in range(1, long):
        if mayor < utilidad[i]:
            mayor = utilidad[i]
    return mayor

def menorUlt(utilidad):
    menor = utilidad[0]
    long = len(utilidad)
    for i in range(1, long):
        if menor > utilidad[i]:
            menor = utilidad[i]
    return menor

def diferencia(menor, mayor):
    difeUtilidad = mayor - menor
    print('La diferencia de utilidad entre el año con mayor utilidad' +
          ' y el año con menor es de $' + str(difeUtilidad) + ' millones.\n')

# Punto 3

def mediana(utilidad):
    kellogs = np.sort(utilidad)
    m = int(len(kellogs))
    if m%2==0:
        m = m/2 -1
        p1 = kellogs[int(m)]
        p2 = kellogs[int(m+1)]
        medianaa = (p1 + p2)/2
    else:
        m = (m//2) + 1
        medianaa = kellogs[int(m)]
    return medianaa

# Punto 4

def promedio(utilidad, medianaa):
    long = len(utilidad)
    suma = 0
    for i in range(0,long):
         suma = suma + utilidad[i]
    prome = suma/long
    print('La media es: ' + str(round(prome, 2)))
    if prome > medianaa:
        resta = prome - medianaa
        print('La media es ' + str(round(resta, 2)) + 
              ' mayor que la mediana.\n')
    else:
        resta = medianaa - prome
        print('La mediana es ' + str(round(resta, 2)) + 
              ' mayor que la media.\n')
    
# Punto 5

def utiliAcumulada(utilidad):
    long = len(utilidad)
    suma = 0
    a = 2008
    for i in range(0, long):
        suma = suma + utilidad[i]
    print('La utilidad operacional acumulada es de: $' + 
          str(round(suma, 2)) + ' millones de pesos colombianos.')
    for i in range(0, long):
        porcent = (utilidad[i]*100)/suma
        print('El año ' + str(a) + ' le aporta %' + str(round(porcent, 2)) +
              ' a la utilidad operacional acumulada.')
        a = a + 1
        

# Punto 6

def deficit(utilidad):
    long = len(utilidad)
    ult = utilidad[long-1]
    defi = utilidad[long-2] - ult
    print('\nEl déficit de la utilidad operacional del año 2017 con respecto' 
          + ' a la del año anterior es de: $' + str(defi) + 
          ' millones de pesos\n')

# Punto 7

def defiPorcentaje(utilidad):
    long = len(utilidad)
    a = 2017
    for i in range(0, long-1):
        ult = utilidad[long-1]
        defi = utilidad[long-2] - ult
        defiPorcen = (defi*100)/ult
        long = long-1
        print('El déficit de utilidad operacional del año ' + str(a) + 
              ' fue de: ' +  str(round(defiPorcen, 2)) + '%')
        a = a-1
    
#----------------------------------Corriendo--------------------------------#

utilidadKellogs()
utilidad = utilidadKellogs()
difeMedia(utilidad)
menor = menorUlt(utilidad)
mayor = mayorUlt(utilidad)
diferencia(menor, mayor)
mediana(utilidad)
medianaa = mediana(utilidad)
print('La mediana es: ' + str(medianaa))
promedio(utilidad, medianaa)
utiliAcumulada(utilidad)
deficit(utilidad)
defiPorcentaje(utilidad)