
if __name__ == '__main__':
    # Ficheros:
    # Apertura de ficheros:

    archivo = open('fichero.txt', 'w') # modo de escritura
    archivo.write('Soy Andrea, mi carnet es 6453')
    archivo.close() # Cerrar

    archivo = open('fichero.txt', 'r')
    contenido = archivo.read() # Obtener todo lo que está dentro.
    print(contenido)
    archivo.close()

    # Escritura en modo add:
    archivo = open('fichero.txt', 'a')
    archivo.write('\n Hola clase de IPC2')
    archivo.close()

    # uso del with para abrir y cerrar ficheros:
    with open('fichero.txt', 'w') as openedFile:
        openedFile.write('Desde with')