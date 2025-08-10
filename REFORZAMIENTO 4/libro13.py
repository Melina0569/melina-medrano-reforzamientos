"""
Realizar un programa donde se ingresarán por consola los nombres de los
alumnos (indicar previamente la cantidad de alumnos a ingresar) de un curso
y las notas de c/u. Guardarás la información en un diccionario donde las claves
serán los nombres de c/u de estos alumnos y sus valores serán las notas de
esto alumnos.
Finalmente mostrarás los alumnos con sus notas en un mensaje similar a
“Pedro tiene la nota de 15” y también la media de todas las notas.
"""

cantidad = int (input("Ingrese la cantidad de alumnos: "))

alumnos = {}

for i in range(cantidad):
    nombre = input("Ingrese el nombre del alumno {}: ".format(i+1))
    nota = float(input("Ingrese la nota de {}: ".format(nombre)))
    alumnos[nombre] = nota

print("Lista de alumnos con sus notas")
for nombre in alumnos:
    print(nombre, "tiene la nota de {}".format(alumnos[nombre]))

suma_notas = 0
for nombre in alumnos:
    suma_notas += alumnos[nombre]

media = suma_notas/cantidad
print("La media de todas las notas es: {}".format(media))
