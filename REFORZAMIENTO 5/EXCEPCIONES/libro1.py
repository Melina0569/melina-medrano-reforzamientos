"""
Crear una función llamada division_segura(a, b) que recibirá dos
números e intentará devolver la división de a entre b
Si b es cero, debe capturar la excepción y mostrar mensaje “Error: no
puedes dividir entre cero”
Si ambos valores son válidos deben imprimir el resultado
Independientemente del resultado, debe imprimir “Operación
finalizada” al final
- Usar try, except, finally

- Valida que los datos ingresados sean numéricos de lo contrario
mostrar “Error: Entrada no numérica”
- Usarás la función al menos 3 veces incluyendo un caso de error

"""

def division_segura(a, b):
    try:
        a = float(a)
        b = float(b)

        # Intentar la división
        resultado = a / b
        print("El resultado de {} / {} es: {}".format(a, b, resultado))

    except ValueError:
        print("Error: Entrada no numérica")
    except ZeroDivisionError:
        print("Error: no puedes dividir entre cero")
    finally:
        print("Operación finalizada\n")


# ---- Usos de prueba ----
division_segura(10, 2)
division_segura(5, 0)
division_segura("hola", 3)