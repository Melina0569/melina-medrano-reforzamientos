"""
Creando un archivo principal (main.py) donde importará a un módulo
(operaciones.py) el cuál contendrá las siguientes funciones:
- Una función que realizará la carga de un valor entero y que verifique
que solamente tiene que ser numérico
- Una función que mostrará por pantalla la raíz cuadrada de dicho
valor
- Y otra función que calculará el valor elevado al cuadrado y al cubo
de dicho número, puedes devolver un diccionario o una lista
- Utilizar el módulo math de python.

"""

import math

def cargar_entero():
    while True:
        try:
            valor = int(input("Ingrese un número entero: "))
            return valor
        except ValueError:
            print("Error: Debe ingresar solo valores numéricos enteros.")


def calcular_raiz(valor):
    if valor < 0:
        print("No se puede calcular la raíz cuadrada de un número negativo en reales.")
        return None
    raiz = math.sqrt(valor)
    print("La raíz cuadrada de {} es: {:.4f}".format(valor, raiz))
    return raiz


def calcular_potencias(valor):
    resultados = {
        "cuadrado": math.pow(valor, 2),
        "cubo": math.pow(valor, 3)
    }
    print("El número {} al cuadrado es: {}".format(valor, resultados["cuadrado"]))
    print("El número {} al cubo es: {}".format(valor, resultados["cubo"]))
    return resultados