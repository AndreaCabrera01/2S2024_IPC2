from .Nodo import Nodo

class ListaDCircular:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.size = 0

    def insertar(self, dato):
        nuevo = Nodo(dato)
        if self.primero == None:
            self.primero = nuevo
            self.ultimo = nuevo

            # Actualizar los punteros:
            self.ultimo.siguiente = self.primero
            self.primero.anterior = self.ultimo
        else:
            self.ultimo.siguiente = nuevo # El nodo siguiente del nodo actual es el nuevo nodo
            nuevo.anterior = self.ultimo
            nuevo.siguiente = self.primero
            self.primero.anterior = nuevo
            self.ultimo = nuevo
        self.size +=1

    def imprimir(self):
        actual = self.primero
        for i in range(self.size):
            print(actual.dato)
            actual = actual.siguiente
            i += 1