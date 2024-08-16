from Estructuras.ListaEnlazada.ListaEnlazada import ListaEnlazada
from Estructuras.ListaDEnlazada.ListaDEnlazada import ListaDEnlazada

from Animal import Animal

if __name__ == "__main__":
    print("LISTA ENLAZADA -----------------")

    lista1 = ListaEnlazada() # inicialización de la lista
    lista1.insertar("Andrea")
    lista1.insertar("María")
    lista1.insertar("Luna")
    lista1.insertar(23)

    animal1 = Animal("Kiara", "gato cálico", 1)
    lista1.imprimir()

    listaObjetos = ListaEnlazada()
    animal1 = Animal("Kiara1", "gato cálico", 1)
    animal2 = Animal("Kiara2", "gato cálico", 1)
    animal3 = Animal("Kiara3", "gato cálico", 1)
    listaObjetos.insertar(animal1)
    listaObjetos.insertar(animal2)
    listaObjetos.insertar(animal3)

    listaObjetos.imprimirObjeto()

    print("Lista Doblemente Enlazada ---------------------")
    listaDEn = ListaDEnlazada()
    listaDEn.insertar(8)
    listaDEn.insertar(3)
    listaDEn.insertar("Pepito")
    listaDEn.insertar(-4)

    listaDEn.imprimir()
    print(" REVERSA: ")
    listaDEn.imprimirReversa()