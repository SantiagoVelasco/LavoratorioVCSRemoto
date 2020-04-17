# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 20:51:23 2020

@author: david
"""

import numpy as np

fayala = np.array([['Juan','Amparo','Antonio','María','Lisa','Leonardo','Javier','Santiago'],

                   ["M","F","M","F","F","M","M","M"],

                   ["SI","SI","SI","NO","NO","SI","NO","SI"],

                   ["1","2","1","NA","NA","1","NA","1"]])

#Punnto 1

def Contiene(fayala) :

    c = 0

    f = len(fayala[0])

    for r in range(0,f):

        co = fayala[2,r]

        if co == "SI" :

            c = c +1

            print(str(fayala[0,r])," Salió positivo para diabetes de tipo " + str(fayala[3,r]))

    print("El numero de personas con diavetes en la familia es ", str(c)," Personas")

Contiene(fayala)

#Punto 2

def genero(fayala):

    f = len(fayala[0])

    CM = 0

    CF = 0

    for r in range(0,f):

        co = fayala[2,r]

        if co == "SI" :

            g = fayala[1,r]

            if g == "M" :

                CM = CM + 1

            else :

                CF = CF + 1

    if CM == CF :

        print("Los dos generos son igual de propensos")

    else :

        if CF < CM :

            print("Es más propenso el género masculino a contraer la enfermedad")

        else :

            print("Es más  propenso el género Femenino a contraer la enfermedad")

genero(fayala)

# Punto 3

def tipo(fayala) :

    f = len(fayala[0])

    T1 = 0

    T2 = 0

    for r in range(0,f):

        co = fayala[2,r]

        if co == "SI" :

            t = fayala[3,r]

            if t == "1" :

                T1 = T1 + 1

            else :

                T2 = T2 + 1

    print("El numero de casos de diabetes en la familia de tipo 1 es " + str(T1))

    print("El numero de casos de diabetes en la familia de tipo 2 es " + str(T2))

    if T2 == T1 :

        print("Los dos tipos son igual de propensos")

    else :

        if T2 < T1:

            print("Es màs propenso el tipo 1 de diabetes en la familia")

        else :

            print("Es màs propenso el tipo 2 de diabetes en la familia")

tipo(fayala)