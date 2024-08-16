from .NodoLD import NodoLD
class ListaDEnlazada:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.size = 0

    def insertar(self, dato):
        nuevo = NodoLD(dato)
        if self.primero == None:
            self.primero = nuevo
            self.ultimo = nuevo
        else:
            self.ultimo.siguiente = nuevo # el Nodo siguiente del nodo actual es el nuevo nodo
            nuevo.anterior = self.ultimo # el nodo anterior del nuevo nodo es el actual
            self.ultimo = nuevo # el nuevo nodo es el último

        self.size += 1

    def imprimir(self):
        actual = self.primero
        while actual != None:
            print(actual.dato)
            actual = actual.siguiente
        

    def imprimirReversa(self):
        actual = self.ultimo
        while actual != None:
            print(actual.dato)
            actual = actual.anterior