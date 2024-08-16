from .Nodo import Nodo

class ListaEnlazada:
    def __init__(self):
        self.primero = None
        self.size = 0

    def insertar(self, dato):
        nuevo = Nodo(dato) # Creamos el nuevo nodo
        if self.primero == None: # Si no hay nada en la lista
            self.primero = nuevo
        else: # Si ya hay algo 
            actual = self.primero # Obtener el primero de la lista
            while actual.siguiente != None:
                actual = actual.siguiente
            actual.siguiente = nuevo
        self.size += 1

    def imprimir(self):
        actual = self.primero
        while actual.siguiente != None:
            print(actual.dato)
            actual = actual.siguiente
        print(actual.dato)

    def imprimirObjeto(self):
        actual = self.primero
        while actual.siguiente != None:
            print(actual.dato.nombre)
            actual = actual.siguiente
        print(actual.dato.nombre)

    