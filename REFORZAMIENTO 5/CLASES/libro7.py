"""
Crear una clase Persona que contenga dos atributos: nombre y edad.
Nombre y edad se ingresarán por teclado en el constructor.
Declarar una segunda clase llamada Empleado que herede de la clase Persona
y agregue un atributo sueldo. Crearás un metodo que indicará si debe pagar
impuestos (que sería el 10% de su sueldo y si sueldo es superior a 4000 soles)
Instanciar la clase Empleado al menos para 3 empleados, mostrar el sueldo
del empleado y cuánto debe pagar de impuesto.
"""

class Persona:
    def __init__(self):
        self.nombre = input("Ingrese el nombre: ")
        self.edad = int(input("Ingrese la edad: "))


class Empleado(Persona):
    def __init__(self):
        super().__init__()
        self.sueldo = float(input("Ingrese el sueldo: "))

    def calcular_impuesto(self):
        if self.sueldo > 4000:
            impuesto = self.sueldo * 0.10
            return impuesto
        else:
            return 0.0

print("\nRegistro del Empleado 1:")
empleado1 = Empleado()

print("\nRegistro del Empleado 2:")
empleado2 = Empleado()

print("\nRegistro del Empleado 3:")
empleado3 = Empleado()

# Mostrar resultados
empleados = [empleado1, empleado2, empleado3]

print("\n--- RESULTADOS ---")
for e in empleados:
    print("Empleado: {}, Edad: {}, Sueldo: {:.2f} soles, Impuesto a pagar: {:.2f} soles".format(e.nombre, e.edad, e.sueldo, e.calcular_impuesto()
    ))