"""
Crea correctamente un diccionario con los campos de: nombre, edad, salario
y edad.
Convierte tu diccionario finalmente a una lista y muestra el resultado en la
terminal.
"""

persona = {"nombre": "Melina", "edad": 21, "salario": 3500.50}
lista_persona = list(persona.values())

print("Diccionario: {}".format(persona))
print("Lista: {}".format(lista_persona))