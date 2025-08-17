"""
Crear una clase llamada Circulo que contenga radio en su constructor y
que contenga un metodo área que devuelva el área de un círculo.
Adicionalmente habrá un metodo que devuelva el perímetro del círculo.
También habrá un metodo donde pedirá el radio del círculo.
Instanciar mínimo 2 veces la clase y mostrar resultados por consola.
"""

class Circulo:
    def __init__(self, radio = 0):
        self.radio = radio

    def ingreso_radio(self):
        self.radio = float(input("Ingrese el radio del círculo: "))

    def area(self):
        pi = 3.1416
        return pi * (self.radio ** 2)

    def perimetro(self):
        pi = 3.1416
        return 2 * pi * self.radio

circulo1 = Circulo()
circulo1.ingreso_radio()
print("El área del círculo 1 es: {:.2f}".format(circulo1.area()))
print("El perímetro del círculo 1: {:.2f}".format(circulo1.perimetro()))

circulo2 = Circulo()
circulo2.ingreso_radio()
print("El área del círculo 2 es: {:.2f}".format(circulo2.area()))
print("El perímetro del círculo 2 es: {:.2f}".format(circulo2.perimetro()))