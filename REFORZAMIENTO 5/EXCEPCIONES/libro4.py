"""
Crear una función saluda_fecha(nombre, dia, mes, anio) que
contendrá una excepción para el siguiente bloque de código y tu
programa no se bloquee. Además, imprime un mensaje al usuario la
causa y/o solución (Pedir nombre, día, mes, año por consola):
Nombre: No debe recibir un dato numérico, sino decírselo al usuario
Día, mes y año: No debe recibir un dato string, sino decírselo al usuario
cadena = "Hello NOMBRE, hoy estamos DÍA de MES del AÑO"
# Hello Leonardo, hoy estamos 04 de agosto del 2025
Independientemente del resultado, debe imprimir “Operación
finalizada” al final

- Usar try, except, finally
Usar la función al menos 3 veces, incluyendo casos de error

"""

def saluda_fecha(nombre, dia, mes, anio):
    try:
        if nombre.isdigit():
            raise ValueError("El nombre no debe ser un número. Ingrese un texto válido.")
        if not isinstance(dia, int) or not isinstance(mes, int) or not isinstance(anio, int):
            raise TypeError("Día, mes y año deben ser números enteros.")

        # Diccionario de meses en español
        meses = {
            1: "enero", 2: "febrero", 3: "marzo", 4: "abril",
            5: "mayo", 6: "junio", 7: "julio", 8: "agosto",
            9: "septiembre", 10: "octubre", 11: "noviembre", 12: "diciembre"
        }

        if mes not in meses:
            raise ValueError("El mes debe estar entre 1 y 12.")
        cadena = "Hello {}, hoy estamos {} de {} del {}".format(
            nombre, str(dia).zfill(2), meses[mes], anio
        )
        print(cadena)

    except ValueError as ve:
        print(ve)
        print("Solución: asegúrese de ingresar un nombre válido o un mes correcto.")

    except TypeError as te:
        print(te)
        print("Solución: ingrese día, mes y año como números enteros.")

    finally:
        print("Operación finalizada.\n")


saluda_fecha("Leonardo", 4, 8, 2025)
saluda_fecha("1234", 4, 8, 2025)
saluda_fecha("Ana", "cinco", 12, 2024)