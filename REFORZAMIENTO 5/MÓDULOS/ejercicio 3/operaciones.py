"""
Creando un archivo principal (main.py) donde importará a un módulo
(operaciones.py) el cuál contendrá las siguientes funciones:
- Una función que genere 30 números enteros aleatorios entre 0 y
100, y muestre en pantalla esta lista de números aleatorios
- Otra función que ordene los valores de una lista y volver a mostrarla
en pantalla

- Otra función que me indicará cuál es el mayor de todos estos
números de la lista
Uso de la función random:

"""

import random

def generar_lista():
    lista = [random.randint(0, 100) for _ in range(30)]
    print("Lista generada: ")
    print(lista)
    return lista


def ordenar_lista(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]  # Intercambio
    print("\nLista ordenada (ascendente): ")
    print(lista)
    return lista


def numero_mayor(lista):
    mayor = lista[0]
    for num in lista:
        if num > mayor:
            mayor = num
    print("\nEl número mayor es:", mayor)
    return mayor