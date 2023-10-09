#/*
# * Crea una función que encuentre todos los triples pitagóricos
# * (ternas) menores o iguales a un número dado.
# * - Debes buscar información sobre qué es un triple pitagórico.
# * - La función únicamente recibe el número máximo que puede
# *   aparecer en el triple.
# * - Ejemplo: Los triples menores o iguales a 10 están
# *   formados por (3, 4, 5) y (6, 8, 10).
# */

import math

def dame_lista_cuadrados(maximo):
    lista_cuadrados = []
    for i in range(maximo):
        if i != 0:
            lista_cuadrados.append(i*i)
    return lista_cuadrados

def dame_triple_pitagorico(objetivo, lista):
    limite_lista = len(lista)
    for i in range(0,limite_lista):
        n1 = lista.pop()
        for n2 in lista:
            if n1 + n2 == objetivo:
                return [int(math.sqrt(n1)),int(math.sqrt(n2)), int(math.sqrt(objetivo))]
    return []

def dame_triples_pitagoricos(maximo):
    triples_pitagoricos = []
    if maximo >= 3:
        for i in range(3,maximo+1):
            cuadrado = i*i
            lista_cuadrados = dame_lista_cuadrados(i)
            lista_cuadrados.reverse()
            triple_pitagorico = dame_triple_pitagorico(cuadrado,lista_cuadrados)
            if len(triple_pitagorico) > 0:
                triples_pitagoricos.append(triple_pitagorico)
    return triples_pitagoricos

print(dame_triples_pitagoricos(10))
