"""
Crea una lista vacía, luego ingresa sus valores (10 valores numéricos) y
finalmente muestra la suma y la media de los números ingresado
insertados en la terminal
"""

numeros = []

for _ in range(10):
    valor = float(input("Ingrese el número: "))
    numeros.append(valor)

suma = sum(numeros)
media = suma / len(numeros)
print("Suma de los números: {}".format(suma))
print("Media de los números: {}".format(media))