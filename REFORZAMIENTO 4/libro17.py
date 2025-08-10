"""
Crear un programa que cuente cuántas veces aparece cada vocal en la
oración. Ignorar mayúsculas/minúsculas
Input: “Programación en Python”
Output:
a: 2
e: 1
i: 1
o: 2
u: 0
Métodos útiles: lower() y count()
"""

oracion = "Programación en Python"

oracion = oracion.lower()

vocales = ["a", "e", "i", "o", "u"]

for vocal in vocales:
    cantidad = oracion.count(vocal)
    print("{} : {}".format(vocal, cantidad))

