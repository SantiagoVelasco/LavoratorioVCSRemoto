# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 14:54:18 2020

@author: david
"""

import numpy as np

#    Generador de arreglos de 4x12 de números aleatorios bajo un rango a-b   #
def generador (a, b):
    arreglo = np.random.randint(a, b, (4, 12))
    return arreglo

#------------Función que imprime un arreglo visualmente entendible-----------#
def imprimir(arreglo):
    ciudad, mes = arreglo.shape
    ciudades = np.array(["Bucaramanga  ", "Floridablanca", "Girón        ",
                         "Piedecuesta  "])
    meses = np.array(["            Ene Feb Mar Abr May Jun Jul Ago Sep Oct Nov Dic"])
    print(str(meses))
    for i in range(0, ciudad):
        print(str(ciudades[i]) + str(arreglo[i]))

#----------------Función que resta los elementos de 2 arreglos---------------#
def restador(ingresos, egresos):
    x, y = ingresos.shape
    resta = np.random.randint(0, 100, (4,12))
    for i in range(0, x):
        for k in range(0, y):
            resta[i][k] = ingresos[i, k] - egresos[i, k]
    return resta

#Función que dado el arreglo 'ganancias' anteriormente creado, indica cual es
#--------------------la fila o ciudad con mayores ganancias----------------#
def mejor_ciudad(ganancias):
    x, y = ganancias.shape
    ciudad = [0]
    ciudades = 0
    suma = 0
    resta = 0
    for i in range(0, x):
        resta = resta + ciudad[i-1]
        for k in range(0, y):
            suma = suma + ganancias[i, k]        
            ciudades = suma - resta
        ciudad.insert(i, ciudades)    
    citys = ["Bucaramanga", "Floridablanca", "Girón", "Piedecuesta"]
    best_city = ciudad[0]
    posbest = 0
    city = citys[0]
    for i in range(0, x):
        if best_city<ciudad[i]:
            best_city = ciudad[i]
            posbest = i
            city = citys[i]
    print("\nLa ciudad con mayores ganancias es: " + str(city)
          + " y se encuentra en la posición: " + str(posbest))

#-Dado el arreglo ganancias se calcula cual es la ciudad con menores ganancias-#
def peor_ciudad(ganancias):
    x, y = ganancias.shape
    ciudad = [0]
    ciudades = 0
    suma = 0
    resta = 0
    for i in range(0, x):
        resta = resta + ciudad[i-1]
        for k in range(0, y):
            suma = suma + ganancias[i, k]        
            ciudades = suma - resta
        ciudad.insert(i, ciudades)
    citys = ["Bucaramanga", "Floridablanca", "Girón", "Piedecuesta"]
    worst_city = ciudad[0]
    posworst = 0
    city = citys[0]
    for i in range(0, x):
        if worst_city>ciudad[i]:
            worst_city = ciudad[i]
            posworst = i
            city = citys[i]
    print("La ciudad con menores ganancias es: " + str(city) +
          " y se encuentra en la posición: " + str(posworst) + "\n")

#--------------Se calcula del arreglo ganancias qué mes es mayor-----------#
def mejor_mes(ganancias):
    x, y = ganancias.shape
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", 
             "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    citys = ["Bucaramanga", "Floridablanca", "Girón", "Piedecuesta"]
    for i in range(0, x):
        best_mes = ganancias[i, 0]
        number = 0
        for k in range(0, y):
            if best_mes<ganancias[i, k]:
                best_mes = ganancias[i, k]
                number = (k)
        print('El mejor mes de la ciudad ' + str(citys[i]) + ' es: '
                  + str(meses[number]))
    print('\n')
        
#--------------Se calcula del arreglo ganancias qué mes es menor------------#
def peor_mes(ganancias):
    x, y = ganancias.shape
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", 
             "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    citys = ["Bucaramanga", "Floridablanca", "Girón", "Piedecuesta"]
    for i in range(0, x):
        worst_mes = ganancias[i, 0]
        number = 0
        for k in range(0, y):
            if worst_mes>ganancias[i, k]:
                worst_mes = ganancias[i, k]
                number = (k)
        print('El peor mes de la ciudad ' + str(citys[i]) + ' es: '
                  + str(meses[number]))

#-------------Función que permite imprimir solo los meses que se quieren.
#----------------------------Estos meses son parámetros
def imprimir_personalizado(ganancias, z, w):
    ciudad, mes = ganancias.shape
    ciudades = ["Bucaramanga  ", "Floridablanca", "Girón        ",
                         "Piedecuesta  "]
    meses = ['         ', 'Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago',
             'Sep', 'Oct', 'Nov', 'Dic']
    print("\n" + str(meses[0]) + str(meses[z: w+1]))
    for i in range(0, ciudad):
        print(str(ciudades[i]) + str(ganancias[i, z-1:w]))

#-----------------Calcula promedio de arreglos de 2 dimenciones---------------#
def promedio(ingresos, egresos, ganancias):
    x, y = ganancias.shape
    citys = ["Bucaramanga", "Floridablanca", "Girón", "Piedecuesta"]
    print('\n')
    for i in range(0, x):
        suma = 0
        for k in range(0, y):
            suma = (suma + ingresos[i, k])
        promedio = suma/y
        print('El promedio de ingresos de la ciudad ' + str(citys[i]) + 
              ' es: ' + str(round(promedio, 2)))
    print('\n')
    for i in range(0, x):
        suma = 0
        for k in range(0, y):
            suma = (suma + egresos[i, k])
        promedio = suma/y
        print('El promedio de egresos de la ciudad ' + str(citys[i]) + 
              ' es: ' + str(round(promedio, 2)))
    print('\n')
    for i in range(0, x):
        suma = 0
        for k in range(0, y):
            suma = (suma + ganancias[i, k])
        promedio = suma/y
        print('El promedio de ganancias de la ciudad ' + str(citys[i]) + 
              ' es: ' + str(round(promedio, 2)))

#------------Se calcula el promedio, pero sin el mejor y peor mes-----------#
def promedio_2(ingresos, egresos, ganancias):
    citys = ["Bucaramanga", "Floridablanca", "Girón", "Piedecuesta"]
    x, y = ganancias.shape
    ingresos_altos = []
    ingresos_bajos = []
    print('\n')
    for i in range(0 , x):
        bajo = ingresos[i, 0]
        alto = ingresos[i, 0]
        suma = 0
        for k in range(0, y):
            if bajo>ingresos[i, k]:
                bajo = ingresos[i, k]
            if alto < ingresos[i, k]:
                alto = ingresos[i, k]
            suma = (suma + ingresos[i, k])
        ingresos_bajos.append(bajo)
        ingresos_altos.append(alto)
        promedio = (suma - ingresos_altos[i] - ingresos_bajos[i]) / (y-2)
        print('El promedio_2 de ingresos de la ciudad ' + str(citys[i]) + 
              ' es: ' + str(round(promedio, 2)))   
    print('\n')
    egresos_altos = []
    egresos_bajos = []
    for i in range(0 , x):
        bajo = egresos[i, 0]
        alto = egresos[i, 0]
        suma = 0
        for k in range(0, y):
            if bajo>egresos[i, k]:
                bajo = egresos[i, k]
            if alto < egresos[i, k]:
                alto = egresos[i, k]
            suma = (suma + egresos[i, k])
        egresos_bajos.append(bajo)
        egresos_altos.append(alto)
        promedio = (suma - egresos_altos[i] - egresos_bajos[i]) / (y-2)
        print('El promedio_2 de egresos de la ciudad ' + str(citys[i]) + 
              ' es: ' + str(round(promedio, 2)))
    print('\n')
    ganancias_altos = []
    ganancias_bajos = []
    for i in range(0 , x):
        bajo = ganancias[i, 0]
        alto = ganancias[i, 0]
        suma = 0
        for k in range(0, y):
            if bajo>ganancias[i, k]:
                bajo = ganancias[i, k]
            if alto < ganancias[i, k]:
                alto = ganancias[i, k]
            suma = (suma + ganancias[i, k])
        ganancias_bajos.append(bajo)
        ganancias_altos.append(alto)
        promedio = (suma - ganancias_altos[i] - ganancias_bajos[i]) / (y-2)
        print('El promedio_2 de ganancias de la ciudad ' + str(citys[i]) + 
              ' es: ' + str(round(promedio, 2)))
       
#------------Se calcula el porcentaje de meses que dieron ganancias y los 
#-----------------------------que dieron perdidas
def extraer_proporciones(ganancias):
    citys = ["Bucaramanga", "Floridablanca", "Girón", "Piedecuesta"]
    x, y = ganancias.shape
    print('\n')
    for i in range(0, x):
        perdidas = 0
        win = 0
        for k in range(0, y):
            if ganancias[i, k] < 0:
                perdidas +=1
            else:
                win +=1
        porcen_ganan = (win * 100)/12
        porcen_perdi = (perdidas * 100)/12
        print('El porcentaje de meses en los que se generan ganancias en ' + 
              str(citys[i]) + ' es: ' + str(round(porcen_ganan, 2)) + '%' + ' y el ' + 
              'porcentaje de meses en los que se generan perdidas es: ' +
              str(round(porcen_perdi, 2)) + '%')

#-----Función que a partir de 2 arreglos bidimensionales genera 2 arreglos
#--------------------------Tridimensionales
def generador3D(ingresos, egresos):
    ingresos3D = ([ingresos], [np.random.randint(90.5, 162.9, (4, 12))], 
                       [np.random.randint(81.9, 147.4, (4, 12))], 
                       [np.random.randint(74.1, 133.4, (4, 12))],
                       [np.random.randint(67, 120.7, (4, 12))])
    egresos3D = ([egresos], [np.random.randint(56.64, 122.72, (4, 12))], 
                       [np.random.randint(53.46, 115.84, (4, 12))], 
                       [np.random.randint(50.46, 109.35, (4, 12))],
                       [np.random.randint(47.63, 103.22, (4, 12))])
    ingresos3D = np.array(ingresos3D)
    egresos3D = np.array(egresos3D)
    return ingresos3D, egresos3D

#-------Función que imprime arreglos tridimensionales de forma entendible-----#
def imprimir3D(arreglo3D, a):
    ciudades = ["Bucaramanga  ", "Floridablanca", "Girón        ",
                         "Piedecuesta  "]
    meses = ['            Ene Feb Mar Abr May Jun Jul Ago Sep Oct Nov Dic']
    año = 2019
    for i in range(0, 5):
        print('\n' + str(a) + ' del año: ' + str(año))
        print(meses)
        for k in range(0, 4):
            print(str(ciudades[k]) + str(arreglo3D[i][0][k]))
        año -=1
        
#-Función que a partir de 2 arreglos tridimensionales calcula las ganancias en
#----------otro arreglo restando los elementos de los primeros 2--------
def calcular_ganancias(ingresos3D, egresos3D):
    resta = np.random.random((5, 1,  4, 12))
    for i in range(0, 5):
        for k in range(0, 4):
            for j in range(0, 12):
                resta[i][0][k][j] = ingresos3D[i][0][k][j] - egresos3D[i][0][k][j]
    resta = resta.astype(np.int)
    return resta

#---------------------------- Se ejecuta el algoritmo -----------------------#
a = 100
b = 180
ingresos = generador(a, b)
a = 60
b = 130
egresos = generador(a, b)
print('Ingresos:')
imprimir(ingresos)
print('\nEgresos:')
imprimir(egresos)
ganancias = restador(ingresos, egresos)
print('\nGanancias:')
imprimir(ganancias)
mejor_ciudad(ganancias)
peor_ciudad(ganancias)
mejor_mes(ganancias)
peor_mes(ganancias)
z = int(input('Ingrese el mes de inicio: '))
w = int(input('Ingrese el mes de fin: '))
imprimir_personalizado(ganancias, z, w)
promedio(ingresos, egresos, ganancias)
promedio_2(ingresos, egresos, ganancias)
extraer_proporciones(ganancias)
ingresos3D, egresos3D = generador3D(ingresos, egresos)
arreglo3D = ingresos3D
a = 'Los ingresos'
imprimir3D(arreglo3D, a)
arreglo3D = egresos3D
a = 'Los egresos'
imprimir3D(arreglo3D, a)
ganancias3D = calcular_ganancias(ingresos3D, egresos3D)
arreglo3D = ganancias3D
a = 'Las ganancias'
imprimir3D(arreglo3D, a)