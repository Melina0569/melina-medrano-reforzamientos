"""
Crear una clase PersonaPrestamo que hereda de la clase anterior
(problema 5) donde tendrá los métodos: Uno, que indicará si la persona está
apta para un préstamo solo si ha estado más de 12 meses trabajando en la
empresa en caso contrario se le informa que no es posible darle el préstamo
y la otra condición adicional es si su edad es mayor de 25 años.
Agregar un segundo metodo a esta nueva clase que te indicará si estás
aprobado recibirás 10 veces tu sueldo de préstamo, el total de préstamo
otorgado es {cantidad_prestamo}.
Instanciar 3 veces la clase para mostrar diferentes resultados.

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
        print("Meses trabajados: {}".format(self.meses_trabajados))
        if self.edad >= 18:
            print("Es mayor de edad")
        else:
            print("Es menor de edad")

    def bonificacion(self):
        if self.edad >= 18:
            return self.sueldo * 0.20
        else:
            return 0

class PersonaPrestamo(Persona):
    def __init__(self, nombre, edad, sueldo, meses_trabajados):
        Persona.__init__(self, nombre, edad, sueldo, meses_trabajados)

    def apto_prestamo(self):
        if self.meses_trabajados > 12 and self.edad > 25:
            print("{} sí está apto para un préstamo".format(self.nombre))
            return True
        else:
            print("{} no está apto para un préstamo".format(self.nombre))
            return False

    def calcular_prestamo(self):
        if self.apto_prestamo():
            cantidad_prestamo = self.sueldo * 10
            print("El total de préstamo otorgado es: {}".format(cantidad_prestamo))

        else:
            print("No es posible otorgar un préstamo a {}".format(self.nombre))

persona1 = PersonaPrestamo("Melina Medrano", 21, 2500, 12)
persona2 = PersonaPrestamo("Renzo Romero", 30, 3000, 16)
persona3 = PersonaPrestamo("Olga Urbano", 28, 2800, 10)

persona1.mostrar_datos()
persona1.calcular_prestamo()

persona2.mostrar_datos()
persona2.calcular_prestamo()

persona3.mostrar_datos()
persona3.calcular_prestamo()