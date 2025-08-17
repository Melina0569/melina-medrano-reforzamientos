"""
Crear una clase Alumno que tenga como atributos el nombre, edad y la
nota final del alumno. Crear los métodos para inicializar sus atributos, otro
para imprimirlos y un metodo para mostrar un mensaje con el resultado de la
nota, si ha aprobado (mayor o igual a 13) o no el alumno. Instanciar la clase
por lo menos 4 veces (4 alumnos)
"""

class Alumno:
    def __init__(self, nombre, edad, nota):
        self.nombre = nombre
        self.edad = edad
        self.nota = nota

    def imprimir_datos(self):
        print("Nombre: {}".format(self.nombre))
        print("Edad: {}".format(self.edad))
        print("Nota final: {}".format(self.nota))

    def resultado(self):
        if self.nota >= 13:
            print("El alumno {} ha aprobado el curso con una nota de {}".format(self.nombre, self.nota))
        else:
            print("El alumno {} ha desaprobado".format(self.nombre))

alumno1 = Alumno("Melina", 18, 15)
alumno1.imprimir_datos()
alumno1.resultado()

alumno2 = Alumno("Gaby", 19, 14)
alumno2.imprimir_datos()
alumno2.resultado()

alumno3 = Alumno("Angie", 21, 18)
alumno3.imprimir_datos()
alumno3.resultado()

alumno4 = Alumno("Willy", 25, 11)
alumno4.imprimir_datos()
alumno4.resultado()