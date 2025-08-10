"""
8. Crear una agenda basada en un diccionario donde los key serán los nombres
de las personas y sus “values” serán los números de teléfono de c/u.
Ingresarás por consola el nombre y el número de cada persona que serán
registrados en la agenda.
El programa también te permitirá buscar por nombre en el diccionario en caso
no exista mostrar un mensaje de “No se encuentra registrado en la agenda”
"""

agenda = {}

cantidad = int(input("¿Cuantas personas quieres registrar?: "))

for i in range(cantidad):
    nombre = input("Ingrese el nombre de la persona {}: ".format(i+1))
    telefono = input("Ingrese el número de teléfono de {}: ".format(nombre))
    agenda[nombre] = telefono

print("Agenda registrada: {}".format(agenda))

buscar = input("Ingrese el nombre que desea buscar: ")

if buscar in agenda:
    print("El número de {} es: {}".format(buscar, agenda[buscar]))
else:
    print("No se encuentra registrado en la agenda")