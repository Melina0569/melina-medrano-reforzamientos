"""
Escribir una clase Figura que debe tener un atributo de nombre de la
figura.
Habrá otra clase llamada Rectangulo que hereda de Figura. Pedirá una base y
una altura en sus parámetros. Tendrá un metodo que devuelva el área y
perímetro de este rectángulo.
También habrá otra clase llamada Circulo que hereda también de Figura,
pedirá por parámetro el radio y este tendrá los métodos que calculará el área
y otro metodo que calculará el perímetro del círculo
Realizar la instancia de la clase figura mínimo 4 veces para mostrar el uso en
ambas figuras (2 casos para ambas figuras) y resultados de todos los métodos
mediante consola.
"""

class Figura:
    def __init__(self, nombre):
        self.nombre = nombre


class Rectangulo(Figura):
    def __init__(self, nombre, base, altura):
        super().__init__(nombre)
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)


class Circulo(Figura):
    def __init__(self, nombre, radio):
        super().__init__(nombre)   # usamos super()
        self.radio = radio

    def area(self):
        return 3.1416 * (self.radio ** 2)

    def perimetro(self):
        return 2 * 3.1416 * self.radio

rect1 = Rectangulo("Rectángulo 1", 10, 5)
rect2 = Rectangulo("Rectángulo 2", 7, 3)

circ1 = Circulo("Círculo 1", 4)
circ2 = Circulo("Círculo 2", 6)

# Lista para recorrer todos los objetos
figuras = [rect1, rect2, circ1, circ2]

print("\n--- RESULTADOS ---")
for f in figuras:
    print("Figura: {}".format(f.nombre))
    print("Área: {:.2f}".format(f.area()))
    print("Perímetro: {:.2f}".format(f.perimetro()))
