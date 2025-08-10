"""
Tiene una lista de invitados que llegaron a una boda de acuerdo a su orden
de llegada:
guests = [“Ana”, “Katherine”, “Pedro”, “Luis”, “Raúl”, “Fiorella”, “Miguel”]
Se requiere reorganizar esta lista.
Primero los que tienen número impar y en el orden que fueron llegando
Segundo las personas que tienen número par de letras
Input: [“Ana”, “Pedro”, “Raúl”, “Fiorella”, “Katherine”, “Miguel”, “Luis”]
Output: [“Ana”, “Pedro”, ”Katherine”, “Raúl”, “Fiorella”, “Miguel”, “Luis”]
"""

guests = ["Ana", "Pedro", "Raúl", "Fiorella", "Katherine", "Miguel", "Luis"]

impares = []
pares = []

for nombre in guests:
    if len(nombre) % 2 != 0:  # impar
        impares.append(nombre)
    else:  # par
        pares.append(nombre)

# Unir listas
nueva_lista = impares + pares

# Mostrar resultados
print("Lista reorganizada:", nueva_lista)