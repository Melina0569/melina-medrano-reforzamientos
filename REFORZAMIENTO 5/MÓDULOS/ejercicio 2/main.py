from operaciones import cargar_numeros, calcular_media, numero_mayor

print("=== PROGRAMA DE OPERACIONES CON 3 NÚMEROS ===")

# Caso 1
print("\n--- Caso 1 ---")
numeros1 = cargar_numeros()
print("Los números ingresados son: {}".format(numeros1))
print("La media es: {:.2f}".format(calcular_media(numeros1)))
print("El mayor número es: {}".format(numero_mayor(numeros1)))

# Caso 2
print("\n--- Caso 2 ---")
numeros2 = cargar_numeros()
print("Los números ingresados son: {}".format(numeros2))
print("La media es: {:.2f}".format(calcular_media(numeros2)))
print("El mayor número es: {}".format(numero_mayor(numeros2)))

# Caso 3
print("\n--- Caso 3 ---")
numeros3 = cargar_numeros()
print("Los números ingresados son: {}".format(numeros3))
print("La media es: {:.2f}".format(calcular_media(numeros3)))
print("El mayor número es: {}".format(numero_mayor(numeros3)))