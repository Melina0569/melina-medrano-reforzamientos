"""
Crear una función funciona_indice(persona, indice) y dentro la
respectiva excepción para el siguiente bloque de código para que tu
programa no se bloquee y además imprime un mensaje al usuario: “El
índice “nombre_indice” ingresado no existe en el diccionario”, tipo de
datos, etc que más pueden incurrir para este caso (los datos se pedirán
por consola):
persona= {'nombre':'Xavier', 'apellido':'Rodriguez', 'dni':'63325345'}
persona['profesion'] #El índice en este caso no existe
Usar la función al menos 2 veces incluyendo un caso de error

"""

def funciona_indice(persona, indice):
    try:
        if not isinstance(indice, str):
            raise TypeError("El índice debe ser de tipo string.")
        valor = persona[indice]
        print("El valor del índice '{}' es: {}".format(indice, valor))

    except KeyError:
        print("El índice '{}' ingresado no existe en el diccionario.".format(indice))
        print("Solución: use una de las claves válidas:", list(persona.keys()))

    except TypeError as e:
        print(e)
        print("Solución: ingrese el índice como texto (string).")

    finally:
        print("Operación finalizada.\n")
persona = {'nombre': 'Xavier', 'apellido': 'Rodriguez', 'dni': '63325345'}
funciona_indice(persona, 'nombre')
funciona_indice(persona, 'profesion')