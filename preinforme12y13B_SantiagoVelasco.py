# -*- coding: utf-8 -*-
"""
Created on Thu May  7 10:26:26 2020

@author: david
"""

import random

ponderado = {'A' : 1, '2': 2, '3': 3, '4': 4, '5':5, '6':6, '7':7, '8':8,
             '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}

simbolos = ['(C)', '(D)', '(T)', '(P)']

# Se crea la función que combine los valores con los palos #
def combinar(ponderado, simbolos):
    baraja = {}
    for cartas in ponderado:
        for palos in simbolos:
            baraja[cartas,palos] = ponderado[cartas]
    return baraja

# Se crea la función que revuelva la baraja #
def revolver(baraja):
    desorden = {}
    lista = [cartas for cartas in baraja]
    random.shuffle(lista)
    for cartas in lista:
        desorden[cartas] = baraja[cartas]
    return desorden
        
# Definición de contadores #
gano = 0
empate = 0
perdio = 0
juegos = 0

def juego(baraja, gano, empate, perdio, juegos):
    # Se crea la lista con los aces para un futuro calculo (1 u 11) #
    aces = [('A', '(C)'), ('A', '(D)'), ('A', '(T)'), ('A', '(P)'),]
    # Listas de las cartas del jugador y tallador #
    cartas_jugador = []
    cartas_tallador = []
    # Lista que contenga las llaves del diccionario baraja ya mezclada #
    llaves = list(baraja.keys())
  # Se entregan las cartas del juego ya mezcladas, se eliminan de la lista #
    # Y se suman estas cartas #
    cartas_jugador.append(llaves[0])
    suma_jugador = baraja[cartas_jugador[-1]]
    llaves.pop(0)
    cartas_tallador.append(llaves[0])
    suma_tallador = baraja[cartas_tallador[-1]]
    llaves.pop(0)
    cartas_jugador.append(llaves[0])
    suma_jugador = suma_jugador + baraja[cartas_jugador[-1]]
    llaves.pop(0)
    cartas_tallador.append(llaves[0])
    suma_tallador = suma_tallador + baraja[cartas_tallador[-1]]
    llaves.pop(0)
    # Un condicional para saber cuando tomar a AZ como 11 #
    for cartas in cartas_jugador:
        for az in aces:
            if az == cartas:
                if suma_jugador <=11:
                    suma_jugador = suma_jugador + 10
    for cartas in cartas_tallador:
        for az in aces:
            if az == cartas:
                if suma_tallador <=11:
                    suma_tallador = suma_tallador + 10
    print('Sus cartas:', cartas_jugador,'=', suma_jugador)
    if suma_jugador == 21:
        print('Felicidades, ganó el juego.')
        gano +=1
        juegos +=1
    else:
        # Se pregunta si el jugador desea tomar otra carta #
        while suma_jugador <=21:
            a = int(input('Tecleé 1 si quiere otra carta, '
                          'cualquier otro número si no lo desea: '))
            if a==1:
                cartas_jugador.append(llaves[0])
                # Condicional para el valor de AZ #
                for cartas in cartas_jugador:
                    for az in aces:
                        if az == cartas:
                            if suma_jugador <=11:
                                suma_jugador = suma_jugador + 10
                suma_jugador = suma_jugador + baraja[cartas_jugador[-1]]
                llaves.pop(0)
                print('Sus cartas:', cartas_jugador,'=', suma_jugador)
            else:
                # Else por si el jugador desea plantar #
                print('Plantó.\n')
                break
            if suma_jugador >21:
                print('Ha perdido.')
                perdio +=1
                juegos +=1
                break
    # Se crea el condicional para entregar cartas al tallador #
        if suma_jugador <= 21:
            print('Cartas tallador: ', cartas_tallador,'=', suma_tallador)
            while suma_tallador < suma_jugador:
                cartas_tallador.append(llaves[0])
                for cartas in cartas_tallador:
                    for az in aces:
                        if az == cartas:
                            if suma_tallador <=11:
                                suma_tallador = suma_tallador + 10
                suma_tallador = suma_tallador + baraja[cartas_tallador[-1]]
                llaves.pop(0)
                print('Cartas tallador: ', cartas_tallador,'=', suma_tallador)
    # Se notifica cuando se gana, pierde o empata #
            if suma_tallador > 21:
                print('Felicidades, ganó el juego.')
                gano +=1
                juegos +=1
            if suma_tallador == suma_jugador:
                print('Empate.')
                empate +=1
                juegos +=1
            if (suma_tallador > suma_jugador)&(suma_tallador<=21):
                print('Ha perdido.')
                perdio +=1
                juegos +=1
    return gano, perdio, empate, juegos
# Se ejecuta por 1ra vez el juego #
baraja = combinar(ponderado, simbolos)
baraja = revolver(baraja)
gano, perdio, empate, juegos = juego(baraja, gano, empate, perdio, juegos)

def correr(gano, perdio, empate, juegos):
    # Condicional para correr el juego hasta que el jugador lo decida #
    a = input('Si desea volver a jugar escriba YES, de lo contrario escriba NO: ')
    while a == 'YES':
        baraja = combinar(ponderado, simbolos)
        baraja = revolver(baraja)
        gano, perdio, empate, juegos = juego(baraja, gano, empate, perdio, juegos)
        # Se pregunta si desea volver a jugar #
        a = input('Si desea volver a jugar escriba YES, '
                  'de lo contrario escriba NO: ')
    if a == 'NO':
        #Si no desea jugar de nuevo se imprime sus estadísticas #
        print('\nHa terminado la partida')
        print('Ganó en', gano, 'ocasiones.')
        print('Perdió en', perdio, 'ocasiones')
        print('Ha empatado en', empate, 'ocasiones')
        print('Ha jugado', juegos, 'veces')
    
        # Se ejecuta el juego hasta que el jugador lo decida #
correr(gano, perdio, empate, juegos)