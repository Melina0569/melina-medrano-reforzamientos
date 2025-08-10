"""
Crear un diccionario con 6 departamentos del país.
- Borrar cualquier departamento, usando la palabra reservada del.
- Actualizar el penúltimo departamento por otro.

- Comprobar que no existe este departamento borrado dentro del
diccionario.
"""

departamentos = {1: "Lima", 2: "Ica", 3: "Cusco", 4:"Arequipa", 5:"Piura", 6: "Junin"}

print("Diccionario inicial: {}".format(departamentos))

del departamentos[3]

print("Diccionario después de borrar Arequipa: ", departamentos)

departamentos[5] = "Tacna"

print("Diccionario actualizado: {}".format(departamentos))

if "Cusco" not in departamentos.values():
    print("El departamento borrado no se encuentra en el diccionario")

else:
    print("El departamento borrado aun está en el diccionario")