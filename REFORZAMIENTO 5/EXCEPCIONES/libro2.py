"""
Crear una función y dentro la respectiva excepción o excepciones para
el siguiente bloque de código para que tu programa no se bloquee, ya
que solo aceptará datos tipos entero y además imprimir un mensaje
al usuario la causa y/o solución. También debe indicar el índice donde
ingresarás este nuevo dato, si el índice está fuera de rango indicárselo
al usuario:
lista = [2, 6, 10, 4, 5, 23, 1]
lista[10]: No es posible ingresar el dato, índice fuera de rango
- Usarás dos tipos diferentes de excepciones (IndexError
TypeError) y
- Usarás la función al menos 3 veces incluyendo un caso de error

"""

def insertar_dato(lista, indice, dato):
    try:
        if not isinstance(dato, int):
            raise TypeError("Solo se permiten datos de tipo entero. ")

        lista[indice] = dato
        print("Se insertó el valor {} en la posición {}".format(dato, indice))
        print("Lista actualizada:", lista)

    except IndexError:
        print("No es posible ingresar el dato, índice {} fuera de rango.".format(indice))
        print("Solución: use un índice entre 0 y {}.".format(len(lista)-1))

    except TypeError as e:
        print(e)
        print("Solución: asegúrate de ingresar solo números enteros.")

    finally:
        print("Operación finalizada.\n")



lista = [2, 6, 10, 4, 5, 23, 1]

insertar_dato(lista, 2, 99)
insertar_dato(lista, 10, 50)
insertar_dato(lista, 3, "hola")