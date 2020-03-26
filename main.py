# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 13:16:50 2020

@author: david
"""


a = float(input("Ingrese el 1er número: "))
c = float(input("Ingrese el 2do número: "))

print("El producto de los números es: " + str(a*c))
print("El doble del 1er número es: " + str(a*2))


#%% Punto 10

b = float(input("Ingrese un 1er número: "))
d = float(input("Ingrese un 2do número: "))
pot = b**2
raiz = d**(1/2)

print("El cuadrado del 1er número es: " + str(pot))
print("La raíz del 2do número es: " + str(raiz))

#%% Punto 12

a = float(input("Ingrese el número a: "))
b = float(input("Ingrese el número b: "))
c = float(input("Ingrese el número c: "))
d = b**2 - 4*a*c
if d > 0:
    x1 = (-b+d**(1/2))/(2*a)
    x2 = (-b-d**(1/2))/(2*a)
    print("La primera solución es: " + str(x1))
    print("La segunda solución es: " + str(x2))
else:
    if d==0:
        x = -b/2*a
        print("x1 y x2 son iguales y corresponden a: " + str(x))
    else:
        print("No existe solución.")
