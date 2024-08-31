class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class listaCircular:
    def __init__(self):
        self.primero = None
        self.size = 0

    def insertar(self, dato):
        nuevo = Nodo(dato) # Creamos el nuevo nodo

        if self.primero == None: # Si la lista está vacía
            self.primero = nuevo
            self.primero.siguiente = self.primero

        else: # Si no está vacía
            actual = self.primero
            while actual.siguiente != self.primero:
                actual = actual.siguiente # se va actualizando
            actual.siguiente = nuevo # se agrega
            nuevo.siguiente = self.primero # apunta a la cabeza
        
        self.size += 1

    def imprimir(self):
        actual = self.primero
        for elemento in range(self.size):
            print(actual.dato)
            actual = actual.siguiente
            elemento += 1

    def deepCopy(self):
        nuevaLista = listaCircular()
        actual = self.primero
        for elemento in range(self.size):
            nuevaLista.insertar(actual.dato)
            actual = actual.siguiente
            elemento += 1
        return nuevaLista


if __name__ == "__main__":
    lista = listaCircular()
    lista.insertar("Hola")
    lista.insertar("Mundo")
    lista.insertar("Prueba")
    lista2 = lista.deepCopy()
    lista2.insertar("Adios")
    lista.imprimir()
    lista2.imprimir()
    print("Tamaño de lista 1: ", lista.size)
    print("Tamaño de lista 2: ", lista2.size)

    