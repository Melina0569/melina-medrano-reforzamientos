"""
Ingresar el nombre de tu carrera dentro de los valores que tienes en tu
diccionario.
- Mostrar en consola los valores de tu carrera y nombre agregándolos a
una variable c/u
"""

datos = {"nombre": "Melina", "edad":22, "universidad":"UNMSM"}

datos["carrera"] = "Investigación Operativa"

nombre_var = datos["nombre"]
carrera_var = datos["carrera"]

print("Nombre: {}".format(nombre_var))
print("Carrera: {}".format(carrera_var))
