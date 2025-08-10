"""
Escribir un programa donde ingresarás el tamaño de la lista mediante consola,
este tamaño servirá para ingresar una cantidad X de nombres de alumnos. Ingresarás
los nombres mediante consola también.

Se quiere mostrar finalmente el tamaño de la lista y todos los nombres de la lista que fueron ingresados.
"""

tam = int (input("Ingrese la cantidad de alumnos: "))
alumnos = []

for _ in range (tam):
    nombre = input("Ingrese el nombre del alumno: ")
    alumnos.append(nombre)

print("La cantidad de alumnos ingresados es: {}".format(len(alumnos)))
print("Lista de alumnos ingresados: {}".format(alumnos))