"""
Crea un programa que calcule el Índice de masa Corporal (IMC) de una
persona.

La fórmula es:

IMC = peso (kg) / altura (m)^2

En el mensaje también indicar el nombre de la persona indicando su IMC
también
"""

nombre = 'Melina'
peso = 65
altura = 1.62

IMC = peso / pow (altura, 2)

print("Buen día estimado(a) {}, según la información que nos ha brindado, podemos llegar a la conclusión que su IMC es: {:.2f}".format(nombre, IMC))