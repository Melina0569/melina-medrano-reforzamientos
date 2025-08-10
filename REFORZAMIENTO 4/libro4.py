"""
Tienes una lista con 5 nombres de estudiantes. Crear un programa que te
pedirá ingresar el nombre de un estudiante, la cuál será eliminada de lista
inicial en caso que no exista en la lista mostrar un mensaje donde indique
que no se encuentre en la lista y luego esta será agregada a la lista.
Finalmente mostrar la lista actualizada en consola.
"""

estudiantes = ["Ana", "Luis", "María", "Pedro", "Sofia"]

print("Lista inicial de estudiantes: {}".format(estudiantes))

nombre = input("Ingrese el nombre de un estudiante: ")

if nombre in estudiantes:
    estudiantes.remove(nombre)
    print("El estudiante '{}' ha sido eliminado de la lista.".format(nombre))
else:
    estudiantes.append(nombre)
    print("El estudiante '{}' no estaba en la lista y ha sido agregado.".format(nombre))

# Mostrar lista actualizada
print("Lista actualizada de estudiantes: {}".format(estudiantes))