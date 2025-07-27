"""
Escribe un programa que reciba dos flotantes, luego estos pasarán
a ser convertidos en enteros. Indique si el primero es múltiplo del
segundo. Usar mod para la verificación si el residuo es 0

"""

float1 = 17.46
float2 = 5.96

num1 = int(float1)
num2 = int(float2)

if num1 % num2 == 0:
    print("{} es múltiplo de {}".format(num1, num2))
if num1 % num2 != 0:
    print("{} no es múltiplo de {}".format(num1, num2))