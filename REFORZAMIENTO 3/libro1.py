"""
Ejercicio 1
Escribe un programa que convierta cierta cantidad de soles a dólares,
usando un tipo de cambio que se proporciona en el programa.

Estos valores estarán dentro de sus variables respectivamente.

La salida mostrará tres cambios que hagas respectivamente de tres montos
a convertir.
"""

#Monto de soles a dolares

dolar = 3.80

soles1 = 1450
soles2 = 300
soles3 = 380

conversion1 = soles1/dolar
conversion2 = soles2/dolar
conversion3 = soles3/dolar

#Imprimimos los resultados de la conversión
print("La conversión de {} soles es la cantidad de {:.2f} dólares.".format(soles1, conversion1))
print("La conversión de {} soles es la cantidad de {:.2f} dólares.".format(soles2, conversion2))
print("La conversión de {} soles es la cantidad de {:.2f} dólares.".format(soles3, conversion3))