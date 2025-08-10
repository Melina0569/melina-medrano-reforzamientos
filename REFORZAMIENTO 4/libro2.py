"""
Crear un programa en Python donde tendrás una lista con 6 departamentos,
el programa te pedirá ingresar 2 departamentos el cual el segundo
departamento que ingreses sustituirá al primero de la lista.
"""

#Lista inicial

departamentos = ["Lima", "Ica", "Cusco", "Arequipa", "Piura", "Trujillo"]

print("Lista inicial de departamentos: {}".format(departamentos))

# Pedir los departamentos
dep1 = input("Ingrese el primer departamento (a sustituir): ")
dep2 = input("Ingrese el segundo departamento (nuevo): ")


if departamentos[0] == dep1:
    departamentos.pop(0)
    departamentos.insert(0, dep2)
    print("Lista actualizada de departamentos: {}".format(departamentos))
else:
    print("El primer elemento no es '{}'".format(dep1))
