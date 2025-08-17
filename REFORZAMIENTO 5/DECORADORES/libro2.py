"""
Haciendo el uso de *args y **kwargs aplicarlo debidamente para
decorar una función que recibirá 6 argumentos los cuales se
multiplicarán entre ellos (3 de ellos serán usado con **kwargs)
Mensaje previo al usar el decorador “Está por ejecutarse la función” y
mensaje luego de usar el decorador “La función ha sido ejecutado
correctamente”
Usar la función decorada al menos 3 veces

"""
def decorador_multiplicar(funcion):
    def wrapper(*args, **kwargs):
        print("Está por ejecutarse la función")

        # Ejecuta la función con los parámetros
        resultado = funcion(*args, **kwargs)
        print("Resultado de la multiplicación: {}".format(resultado))

        print("La función ha sido ejecutada correctamente\n")
        return resultado

    return wrapper

@decorador_multiplicar
def multiplicar(*args, **kwargs):
    total = 1
    for valor in args:
        total *= valor
    for valor in kwargs.values():
        total *= valor
    return total

multiplicar(2, 3, 4, a=5, b=6, c=7)
multiplicar(1, 10, 2, x=3, y=4, z=5)
multiplicar(5, 2, 1, d=2, e=3, f=4)