"""
Pedir al usuario que ingrese un nombre y apellidos el cual será usada
por un parámetro para una función que se creará e indicará cuantas letras
tiene el nombre solamente. Usar la función un mínimo de dos veces para dos
personas e indicar quien tiene el nombre con mayor número de caracteres
(condicional)

"""

def contar_letras_nombre(nombre_completo):
    nombre = nombre_completo.split()[0]
    return len(nombre)

persona1 = input("Ingrese el nombre y apellidos de la primera persona: ")
persona2 = input("Ingrese el nombre y apellidos de la segunda persona: ")

longitud1 = contar_letras_nombre(persona1)
longitud2 = contar_letras_nombre(persona2)

print("El nombre de {} tiene {} letras.".format(persona1.split()[0], longitud1))
print("El nombre de {} tiene {} letras.".format(persona2.split()[0], longitud2))

if longitud1 > longitud2:
    print(f"{persona1.split()[0]} tiene el nombre más largo.")
elif longitud2 > longitud1:
    print(f"{persona2.split()[0]} tiene el nombre más largo.")
else:
    print("Ambos nombres tienen la misma cantidad de letras.")
