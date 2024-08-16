class Animal:
    def __init__(self, nombre, raza, edad):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad

    def __str__(self):
        return f' nombre: {self.nombre} | raza: {self.raza} | edad: {self.edad}'