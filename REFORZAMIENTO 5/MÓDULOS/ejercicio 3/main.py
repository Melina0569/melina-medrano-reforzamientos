from operaciones import generar_lista, ordenar_lista, numero_mayor

print("=== PROGRAMA CON LISTAS ALEATORIAS ===")

# Generar lista
numeros = generar_lista()

# Ordenar lista sin sorted
ordenados = ordenar_lista(numeros.copy())

# Número mayor sin max()
mayor = numero_mayor(numeros)