"""
Crear una clase llamada Soldado para un juego sobre un mapa la cual
deberá tener como atributos en el constructor posición X y posición Y las
cuales iniciarán en 0, agregar un nombre a este soldado dentro de estos
atributos.
La clase debe tener los siguientes métodos. Caminar hacia el eje X en donde
se indicará cuántos pasos dará y otra clase que le permitirá caminar por el
eje Y, en caso se indique un número negativo indicar que solo puede llegar
hasta el 0 si es menor a los pasos ya dados.
Crear finalmente un metodo adicional que irá guardando los pasos que ha dado
dentro de una lista para que finalmente al usar este metodo me muestre el
historial de movimientos del Soldado, tanto en el eje X y en eje Y
Instanciar un mínimo de 5 movimientos para que muestre finalmente el
historial de pasos de tu soldado

"""

class Soldado:
    def __init__(self, nombre):
        self.nombre = nombre
        self.x = 0
        self.y = 0
        self.historial = []

    def caminar_x(self, pasos):
        nueva_pos = self.x + pasos
        if nueva_pos < 0:
            nueva_pos = 0
        self.x = nueva_pos
        self.historial.append("Se movió en X a la posición {}".format(self.x))

    def caminar_y(self, pasos):
        nueva_pos = self.y + pasos
        if nueva_pos < 0:
            nueva_pos = 0
        self.y = nueva_pos
        self.historial.append("Se movió en Y a la posición {}".format(self.y))

    def mostrar_historial(self):
        print("\nHistorial de movimientos del soldado {}:".format(self.nombre))
        for h in self.historial:
            print(" - {}".format(h))
        print("Posición final: (X={}, Y={})".format(self.x, self.y))


soldado1 = Soldado("Leónidas")

# 5 movimientos mínimos
soldado1.caminar_x(5)
soldado1.caminar_y(3)
soldado1.caminar_x(-2)
soldado1.caminar_y(-10)
soldado1.caminar_x(7)

# Mostrar historial
soldado1.mostrar_historial()