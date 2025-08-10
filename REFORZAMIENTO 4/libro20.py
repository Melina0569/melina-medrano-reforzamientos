"""
Crear una función que sume los dígitos del número ingresado y muestre
por consola la suma de todos estos dígitos.
"""

def suma_digitos(numero):
    total = 0
    for digito in str(numero):
        total += int(digito)
    return total

num = int(input("Ingrese un número: "))
resultado = suma_digitos(num)

print("La suma de los dígitos es: {}".format(resultado))