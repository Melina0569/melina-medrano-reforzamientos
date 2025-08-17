"""
Crear una clase Empleado que contenga los siguientes métodos, uno que
pida ingresar un nombre, apellido y edad, un metodo para pedir su sueldo
actual y otro metodo que lo imprima ambos resultados, pero estarán
contenidos en un diccionario. Comprobar los métodos instanciado la clase
respectivamente al menos para 3 empleados. Considerar en el constructor los
valores necesarios.
"""

class Empleado:
    def __init__(self, nombre="", apellido="", edad=0, sueldo=0.0):
         self.nombre = nombre
         self.apellido = apellido
         self.edad = edad
         self.sueldo = sueldo

    def ingreso_datos(self):
        self.nombre = input("Nombre: ")
        self.apellido = input("Apellido: ")
        self.edad = int(input("Edad: "))

    def ingresar_sueldo(self):
        self.sueldo = float(input("Sueldo: "))

    def mostrar_datos(self):
        print({"Nombre": self.nombre, "Apellido": self.apellido, "Edad": self.edad, "Sueldo": self.sueldo})


empleado1 = Empleado()
empleado1.ingreso_datos()
empleado1.ingresar_sueldo()
empleado1.mostrar_datos()

empleado2 = Empleado()
empleado2.ingreso_datos()
empleado2.ingresar_sueldo()
empleado2.mostrar_datos()

empleado3 = Empleado()
empleado3.ingreso_datos()
empleado3.ingresar_sueldo()
empleado3.mostrar_datos()

