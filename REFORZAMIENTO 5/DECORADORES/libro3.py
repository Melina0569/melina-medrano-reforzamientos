"""
Crear un decorador conteo_parametros(funcion) donde imprimirá la
cantidad de argumentos que tiene la función a decorar usando *args y
**kwargs.
Mensaje previo “La cantidad de argumentos que tiene la función es”
mensaje post “La función decoradora terminó de ejecutarse
correctamente”
Ejemplo: Al usar una función suma que creamos:
suma(4, 1, 10, 2, 50, 64)
Salida:
“La cantidad de argumentos que tiene la función es 5”
“La función decoradora terminó de ejecutarse correctamente”
Consideración:
Todos los parámetros ingresados deben ser enteros, caso sean String
alguno de ellos indicar al usuario: “Solo está admitido datos enteros,
no se podrá realizar la suma”
Usar la función al menos 3 veces

"""
def conteo_parametros(funcion):
    def wrapper(*args, **kwargs):
        for valor in list(args) + list(kwargs.values()):
            if not isinstance(valor, int):
                print("Solo está admitido datos enteros, no se podrá realizar la operación")
                return None

        total_parametros = len(args) + len(kwargs)
        print("La cantidad de argumentos que tiene la función es {}".format(total_parametros))

        resultado = funcion(*args, **kwargs)
        print("La función decoradora terminó de ejecutarse correctamente\n")
        return resultado

    return wrapper

@conteo_parametros
def suma(*args, **kwargs):
    return sum(args) + sum(kwargs.values())

print("Resultado de la suma:", suma(4, 1, 10, 2, 50, 64))
print("Resultado de la suma:", suma(5, 15, a=20, b=30))
print("Resultado de la suma:", suma(3, "hola", 7, c=2))
