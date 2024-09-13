class Animal ():
    def __init__(self, nombre, edad, tipo):
        self.nombre = nombre
        self.edad = edad
        self.tipo = tipo

    def __str__(self):
        return f'Nombre: {self.nombre} - Edad: {self.edad} - Tipo: {self.tipo}'