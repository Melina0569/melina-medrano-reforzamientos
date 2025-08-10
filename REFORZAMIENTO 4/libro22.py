"""
Crear una función que aceptará por parámetro dos valores que serán
ingresados por el usuario, una lista donde los valores serán llenados por el
usuario también y un segundo parámetro que eliminará de la lista que fue
ingresada a la función, finalmente el output de la función será la lista
actualizada sin el valor que se sacará de la lista. Mostrar también la lista
original y el número que fue eliminado.
"""

def eliminar_valor(lista, valor_eliminar):
    lista_original = lista.copy()

    if valor_eliminar in lista:
        lista.remove(valor_eliminar)
        print("Lista original: {}".format(lista_original))
        print("Valor eliminado: {}".format(valor_eliminar))
        print("Lista actualizada: {}".format(lista))
    else:
        print("El valor {} no se encontró en la lista.".format(valor_eliminar))
        print("Lista original: {}".format(lista_original))

# Entrada de datos
n = int(input("¿Cuántos elementos tendrá la lista?: "))
mi_lista = []
for i in range(n):
    valor = input("Ingrese el elemento {}: ".format(i+1))
    mi_lista.append(valor)

valor_a_eliminar = input("Ingrese el valor a eliminar: ")

# Llamar a la función
eliminar_valor(mi_lista, valor_a_eliminar)
