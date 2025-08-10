"""
Convertir tu diccionario a una lista y mostrar en consola el tipo de datos
final que tienes.
"""

persona = {"nombre": "Melina", "salario": 3500.50, "dni": "76146146"}

lista_persona = list(persona.values())

print("Lista: {}".format(lista_persona))
print("Tipo de dato final: {}".format(type(lista_persona)))
