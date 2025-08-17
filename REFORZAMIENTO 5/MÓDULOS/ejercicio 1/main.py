from validador import validar_usuario

usuarios = ["Ana", "SuperUsuario123", "User@2025", "Juan123", "Maria1234"]

for user in usuarios:
    resultado = validar_usuario(user)
    if resultado is True:
        print("{}: Nombre de usuario válido".format(user))
    else:
        print("{}: {}".format(user, resultado))