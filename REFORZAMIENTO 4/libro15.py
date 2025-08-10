"""
9. Una empresa desea gestionar las facturas pendientes que tiene por pagar,
para esto se creará un diccionario donde tendrá por key el número de factura
“00054” y su value será el coste de la factura. El programa tendrá la opción
de pedir nueva factura (por consola) que se agregará al diccionario. Cada vez
que el área de contabilidad pague una factura se pedirá el número de factura
que fue cancelada, si existe mostrar un mensaje donde indicará “La factura
ya está cancelada” caso contrario “El número de factura no existe”

Considerar que cada vez que se realice algún pago o ingreso de una nueva
factura se mostrará inmediatamente al diccionario actualizado.
"""

facturas = {"00054": 250.00, "00055":300.0}

while True:
    print("Gestión de Facturas Pendientes")
    print("1. Agregar nueva factura")
    print("2. Cancelar factura")
    print("3. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        num_factura = input("Ingrese el número de factura: ")
        if num_factura in facturas:
            print("Esa factura ya existe en el registro.")
        else:
            costo = float (input("Ingrese el costo de factura: "))
            facturas[num_factura] = costo
            print("Factura agregada correctamente.")
    elif opcion == "2":
        num_factura = input("Ingrese el número de factura a pagar: ")
        if num_factura in facturas:
            del facturas[num_factura]
            print("La factura ya está cancelada.")
        else:
            print("El número de factura no existe.")
    elif opcion == "3":
        print("Saliendo del programa...")
        break

    else:
        print("Opción inválida.")

    print("Facturas pendientes: {}".format(facturas))