"""
Ingresar por consola el tamaño de una lista, luego empezarás a ingresar los
datos mediante consola también (5 compañías relacionadas con al mundo de
TI) y harás una copia donde adrede agregarás nombres que estarán
repetidos (mediante consola) para que finalmente muestres otra lista donde
solo se mostrará los nombres no repetidos y también te mostrará la lista
inicial
"""

tamanio = int(input("Ingrese la cantidad de compañías de TI: "))

companias = []

for _ in range(tamanio):
    nombre = input("Ingrese el nombre de la compañía : ")
    companias.append(nombre)

companias_copia = companias.copy()
cantidad_duplicados = int(input("¿Cuántos nombres duplicados quiere agregar?: "))

for i in range(cantidad_duplicados):
    nombre_dup = input("Ingrese un nombre que será duplicado: ")
    companias_copia.append(nombre_dup)

# Quitar repetidos usando set y volver a lista
companias_sin_repetidos = list(set(companias_copia))

# Mostrar resultados
print("Lista inicial de compañías: {}".format(companias))

print("Lista con duplicados: {}".format(companias_copia))

print("Lista sin nombres repetidos: {}".format(companias_sin_repetidos))