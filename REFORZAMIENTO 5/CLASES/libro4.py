"""
Crear una clase Persona con los siguientes requerimientos.
La clase tendrá como atributos el nombre, edad y sueldo de una persona.
Implementar los métodos necesarios para inicializar los atributos
(constructor), un metodo para mostrar los datos e indicar si la persona es
mayor de edad o no y otro metodo que bonificación que retornará el 20%
adicional de su sueldo, en caso sea mayor de edad. Un metodo para saber
cuántos meses ha estado trabajando en la empresa
"""

class Persona:
    def __init__(self, nombre, edad, sueldo, meses_trabajados):
        self.nombre = nombre
        self.edad = edad
        self.sueldo = sueldo
        self.meses_trabajados = meses_trabajados

    def mostrar_datos(self):
        print("Nombre: {}".format(self.nombre))
        print("Edad: {}".format(self.edad))
        print("Sueldo: {}".format(self.sueldo))
        if self.edad >= 18:
            print("Es mayor de edad")
        else:
            print("Es menor de edad")

    def bonificacion(self):
        if self.edad >= 18:
            return self.sueldo * 0.20
        else:
            return 0

    def meses_trabajados(self):
        return self.meses_trabajados

persona1 = Persona("Melina Medrano", 21, 2500, 12)
persona2 = Persona("Renzo Romero", 25, 3000, 16)
persona3 = Persona("Olga Urbano", 20, 2800, 17)

persona1.mostrar_datos()
print("Bonificación: {}".format(persona1.bonificacion()))
print("Meses trabajados: {}".format(persona1.meses_trabajados))

persona2.mostrar_datos()
print("Bonificación: {}".format(persona2.bonificacion()))
print("Meses trabajados: {}".format(persona2.meses_trabajados))

persona3.mostrar_datos()
print("Bonificación: {}".format(persona3.bonificacion()))
print("Meses trabajados: {}".format(persona3.meses_trabajados))