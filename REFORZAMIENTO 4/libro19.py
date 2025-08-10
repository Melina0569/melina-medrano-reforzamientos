"""
Pedir dos números positivos mediante terminal al usuario. Mostrar
como salida el número cuya sumatoria de dígitos es el mayor y los números
cuya sumatoria de dígitos es menor que 10. Utilizar una o más funciones, según
sea conveniente.
"""

def suma_digitos(n):
    return sum(int(d) for d in str(n))

num1 = int(input("Ingrese el primer número positivo: "))
num2 = int(input("Ingrese el segundo número positivo: "))

suma1 = suma_digitos(num1)
suma2 = suma_digitos(num2)

if suma1 > suma2:
    print("El número con mayor suma de dígitos es: {}".format(num1))

elif suma2 < suma1:
    print("El número con mayor suma de dígitos es: {}".format(num2))

else:
    print("Ambos tienen la misma suma de dígitos: {}".format(suma1))

if suma1 < 10:
    print("{} tiene suma de dígitos menor que 10 ({})".format(num1, suma1))
if suma2 < 10:
    print("{} tiene suma de dígitos menor que 10 ({})".format(num2, suma2))
