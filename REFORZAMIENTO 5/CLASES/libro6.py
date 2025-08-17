"""
Desarrolla una clase Agenda que administrará contactos. Dentro de una
lista se debe almacenar un diccionario para cada contacto el nombre, el
teléfono, email y DNI. Deberá tener los siguientes métodos:
Añadir contacto, Mostrar contactos y Buscar contacto (Por DNI)
Estructura de la lista cada vez que vas agregando un contacto:
contactos = [
{‘nombre’: “Luis”, ‘telefono’: “997667945”, ‘email’: “luishh@gmail.com”, ‘dni’:
44234239},
{‘nombre’: “Milagros”, ‘telefono’: “997654687”, ‘email’:
“milagros19c@gmail.com”, ‘dni’: 43423211}
]
Agregar por lo menos 4 personas (instanciándolas) para poder luego realizar
la búsqueda de estas personas en la agenda y saber si existen, en caso
contrario indicar: “ ́Nombre ́ no se encuentra anotado en la agenda”
"""

class Agenda:
    def __init__(self):
        self.contactos = []

    def añadir_contacto(self, nombre, telefono, email, dni):
        contacto = {
            "nombre": nombre,
            "telefono": telefono,
            "email": email,
            "dni": dni
        }
        self.contactos.append(contacto)
        print("Contacto de {} agregado con éxito".format(nombre))

    def mostrar_contactos(self):
        print("\n Lista de contactos en la agenda:")
        if not self.contactos:
            print("La agenda está vacía.")
        else:
            for c in self.contactos:
                print("Nombre: {}, Teléfono: {}, Email: {}, DNI: {}".format(
                    c["nombre"], c["telefono"], c["email"], c["dni"]
                ))

    def buscar_contacto(self, dni):
        for c in self.contactos:
            if c["dni"] == dni:
                print("\n Contacto encontrado:")
                print("Nombre: {}, Teléfono: {}, Email: {}, DNI: {}".format(
                    c["nombre"], c["telefono"], c["email"], c["dni"]
                ))
                return
        print("\n El DNI {} no se encuentra anotado en la agenda.".format(dni))
agenda = Agenda()

# Agregar al menos 4 contactos
agenda.añadir_contacto("Luis", "997667945", "luishh@gmail.com", 44234239)
agenda.añadir_contacto("Milagros", "997654687", "milagros19c@gmail.com", 43423211)
agenda.añadir_contacto("Renzo", "923456789", "renzo.romero@gmail.com", 44556677)
agenda.añadir_contacto("Melina", "987654321", "melina.medrano@gmail.com", 55667788)

# Mostrar todos los contactos
agenda.mostrar_contactos()

# Buscar contactos
agenda.buscar_contacto(43423211)
agenda.buscar_contacto(12345678)