# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 17:15:13 2020

@author: david
"""


#%% Punto 1

x1 = float(input("Ingrese x1: "))
y1 = float(input("Ingrese y1: "))
x2 = float(input("Ingrese x2: "))
y2 = float(input("Ingrese y2: "))

de = ((x2-x1)**2+(y2-y1)**2)**(1/2)
print("La distancia euclidiana entre los dos puntos es: " + str(de))

#%% Punto 2

x = int(input("Ingrese un número de cuatro cifras: "))
a = (x%10)
b = (x//10)%10
c = (x//100)%10
d = (x//1000)%10

print(str(a)+str(b)+str(c)+str(d))

#%% Punto 3

n1 = float(input("Ingrese su 1ra nota: "))
n2 = float(input("Ingrese su 2da nota: "))
n3 = float(input("Ingrese su 3ra nota: "))
n4 = float(input("Ingrese su 4ta nota: "))
n5 = float(input("Ingrese su 5ta nota: "))

p = n1*0.15+n2*0.2+n3*0.15+n4*0.3+n5*0.2

if p<2:
    print("El estudiante no puede habilitar.")
else:
    if p<3:
        print("El estudiante reprobó.")
    else:
        if p>4.5:
            print("Felicitaciones, el estudiante aprobó.")
        else:
            print("El estudiante aprobó.")
            
#%% Punto 4

n = int(input("Ingrese un número: "))
acu = 1
acum=1
print(str(acum))
while acu<n:
    acum=str(acum)+str(int(acu)+1)
    print(str(acum))
    acu=acu+1
