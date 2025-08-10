"""
Agrega un nuevo key llamado “dni” con su respectivo valor y luego mostrar
el valor del salario y DNI en consola. También elimina el key edad de tu
diccionario, incluyendo su valor. Mostrar finalmente el diccionario
actualizado.
"""

persona = {"nombre": "Melina", "edad": 21, "salario": 3500.50}

persona["dni"] = "76146146"

print("Salario: {}".format(persona["salario"]))
print("DNI: {}".format(persona["dni"]))

del persona["edad"]

print("Diccionario actualizado: {}".format(persona))