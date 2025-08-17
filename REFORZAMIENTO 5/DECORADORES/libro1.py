"""
Crear una función decoradora que dará los buenos días antes de
ejecutar una función llamada saludo_inicial(nombre) a ser decorada
“Buenos días NOMBRE son las HORA horas con MINUTOS minutos” y
luego de ser ejecutada lanzará un mensaje diciendo “Hasta luego
NOMBRE que tenga buen día”.
La función a decorar pedirá el nombre de una persona y retornará el
mensaje.
Usar la función decorada al menos 3 veces

"""

import datetime
def buenos_dias(funcion):
    def wrapper(nombre):
        ahora = datetime.datetime.now()
        hora = ahora.hour
        minutos = ahora.minute
        print("Buenos días {} son las {} horas con {} minutos".format(nombre, hora, minutos))
        mensaje = funcion(nombre)
        print(mensaje)
        print("Hasta luego {}, que tenga buen día\n".format(nombre))

    return wrapper

@buenos_dias
def saludo_inicial(nombre):
    return "Encantado de saludarte, {}!".format(nombre)

saludo_inicial("Luis")
saludo_inicial("María")
saludo_inicial("Andrés")