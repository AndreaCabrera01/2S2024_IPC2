import re

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

    # Manejo de Excepciones:
    try:
        with open('ficheronoexistente.txt', 'r') as archivo:
            contenido = archivo.read()
            print(contenido)
    except FileNotFoundError:
        print("El fichero no existe.")
    except Exception as e:
        print("Error inesperado: ", e)

    # Tuplas:
    tupla = (1,2,3,4,5) # Creación de tuplas
    print(tupla)
    print(tupla[0])
    print(tupla[1:3])
    print(tupla[1:])
    print(tupla[:3])
    print(tupla[-1])

    # Diccionarios
    diccionario = {'nombre': 'Juan', 'edad': 25, 'cursos': ['Python', 'Java', 'JavaScript']}
    print(diccionario)
    print(diccionario['nombre'])

    # Regex
    texto = 'En esta cadena se encuentra una palabra mágica'
    patron = 'mágica'

    print(re.search(patron, texto))

    # coincidencia de dígitos:
    txt = "Yo tengo 23 años"
    x = re.findall('\d', txt)
    print(x)

    # coincidencia de letras:
    txt = "La lluvia en Sevilla es una maravilla"
    x = re.findall('a', txt)
    print(x)