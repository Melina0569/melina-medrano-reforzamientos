"""
Creando un archivo principal (main.py) donde llamará a un módulo
(operaciones.py) el cuál contendrá las siguientes funciones:
- La primera función cargará a 3 números enteros que pedirá al
usuario que ingrese por consola un valor.
- La segunda función solamente obtendrá la media de estos valores.
- La última función te indicará cuál es el mayor de los 3 números
- Desde el archivo principal importar al módulo y las funciones
correspondiente usando las funciones anteriormente creadas en el
módulo.
- Usarlo al menos para 3 casos distintos.

"""

def cargar_numeros():
    numeros = []
    for i in range(1, 4):
        while True:
            try:
                num = int(input("Ingrese el número {}: ".format(i)))
                numeros.append(num)
                break
            except ValueError:
                print("Error: Debe ingresar un número entero.")
    return numeros


def calcular_media(numeros):
    return sum(numeros) / len(numeros)

def numero_mayor(numeros):
    return max(numeros)