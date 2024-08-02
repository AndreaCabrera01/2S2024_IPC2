class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    #def __str__(self):
    #    return f'Persona\nNombre: {self.nombre}, edad: {self.edad}'
        #return 'Persona\nNombre: '+self.nombre+', edad: '+{self.edad}
    # Métodos:
    def saludar(self):
        return f'Hola, yo soy {self.nombre}, tengo {self.edad} años'
    
    def despedirse(self):
        return 'Adiós'