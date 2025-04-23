class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

if __name__ == '__main__':
    oPersona = Persona("Juan", "Perez")
    print(oPersona.nombre)
    print(oPersona.apellido)