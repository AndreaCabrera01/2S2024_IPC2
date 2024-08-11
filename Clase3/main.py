import xml.etree.ElementTree as ET # Importar librería ElementTree
from xml.dom import minidom # Importar librería minidom
from Cliente import Cliente # Importar la clase Cliente
from Banco import Banco # Importar la clase Banco

listaBancos = []
def Menu():
    print(' ------------- Menu Principal -------------')
    print('1. Leer archivo XML (ElementTree)')
    print('2. Leer archivo XML (minidom)')
    print('3. Escribir archivo XML (ElementTree - XML con información del Banco y promedio de saldo de los clientes)')
    print('4. Escribir archivo XML (minidom -  XML con información del Banco y promedio de saldo de los clientes)')
    print('5. LIMPIAR DATOS ')
    print('6. Salir')
    print(' ------------------------------------------')

    opc = int(input('Ingrese una opción: '))
    return opc

def LeerArchivoET(rutaArchivo):
    tree = ET.parse(rutaArchivo) #Parsear el archivo XML
    root = tree.getroot() # Obtenemos la raíz, en este caso <listado>

    # Revisar cuál es la raíz del archivo XML:
    # print(root.tag)

    for banco_elem in root.findall('Banco'): #iterar
        nombreBanco = banco_elem.get('nombre') # Obtener el atributo nombre
        direccionBanco = banco_elem.get('direccion') # Obtener el atributo direccion
        ant = int(banco_elem.find('Antiguedad').text) # Obtener el texto de la etiqueta Antiguedad
        sucursales = int(banco_elem.find('sucursales').text)
        
        bancoObj = Banco(nombreBanco, direccionBanco, ant, sucursales, [])

        for cliente_elem in banco_elem.find('Clientes').findall('Cliente'):
            nombreCliente = cliente_elem.find('Nombre').text
            cuiCliente = int(cliente_elem.find('CUI').text)
            saldoCliente = float(cliente_elem.find('Saldo').text)
            edadCliente = int(cliente_elem.find('edad').text)

            clienteObj = Cliente(nombreCliente, cuiCliente, saldoCliente, edadCliente)
            bancoObj.clientes.append(clienteObj)

        listaBancos.append(bancoObj)

    print('Datos leídos con éxito con ElementTree')
    for b in listaBancos:
        print('\n', b)
        for c in b.clientes:
            print('\t >>', c.nombre, " | ", c.cui," | ", c.saldo," | ", c.edad)

def LeerArchivoMD(rutaArchivo):
    doc = minidom.parse(rutaArchivo) # Parsear el archivo XML
    root = doc.documentElement # Obtener la raíz del archivo XML

    bancos = root.getElementsByTagName('Banco') # Obtener todos los nodos Banco
    for banco in bancos:
        nombreBanco = banco.getAttribute('nombre')
        direccionBanco = banco.getAttribute('direccion')
        ant = int(banco.getElementsByTagName('Antiguedad')[0].firstChild.data)
        sucursales = int(banco.getElementsByTagName('sucursales')[0].firstChild.data)

        bancoObj = Banco(nombreBanco, direccionBanco, ant, sucursales, [])

        clientes = banco.getElementsByTagName('Cliente')
        for cliente in clientes:
            nombreCliente = cliente.getElementsByTagName('Nombre')[0].firstChild.data
            cuiCliente = int(cliente.getElementsByTagName('CUI')[0].firstChild.data)
            saldoCliente = float(cliente.getElementsByTagName('Saldo')[0].firstChild.data)
            edadCliente = int(cliente.getElementsByTagName('edad')[0].firstChild.data)

            clienteObj = Cliente(nombreCliente, cuiCliente, saldoCliente, edadCliente)
            bancoObj.clientes.append(clienteObj)

        listaBancos.append(bancoObj)
    print('Datos leídos con éxito con minidom')

    for b in listaBancos:
        print('\n', b)
        for c in b.clientes:
            print('\t >>', c.nombre, " | ", c.cui," | ", c.saldo," | ", c.edad)

def EscribirArchivoET():
    # CREAR EL ELEMENTO RAIZ:
    root = ET.Element('listadoReporte')

    for banco in listaBancos:
        banco_elem = ET.SubElement(root, 'Banco')
        banco_elem.set('nombre', banco.nombre)

        direccion_elem = ET.SubElement(banco_elem, 'direccion')
        direccion_elem.text = banco.direccion

        promedio_elem = ET.SubElement(banco_elem, 'promedioSaldo')
        promedio_elem.text = str(banco.promedio())

    tree = ET.ElementTree(root) # Crear el árbol
    tree.write('promedioPorBanco_ET.xml', encoding='UTF-8', xml_declaration=True) # Guardar el archivo
    
def EscribirArchivoMD():
    doc = minidom.Document() # Crear el documento
    root = doc.createElement('listadoReporte') # Crear el elemento raíz
    doc.appendChild(root) # Agregar el elemento raíz al documento

    for banco in listaBancos:
        banco_elem = doc.createElement('Banco')
        banco_elem.setAttribute('nombre', banco.nombre)

        direccion_elem = doc.createElement('direccion')
        direccion_elem.appendChild(doc.createTextNode(banco.direccion))
        banco_elem.appendChild(direccion_elem)

        promedio_elem = doc.createElement('promedioSaldo')
        promedio_elem.appendChild(doc.createTextNode(str(banco.promedio())))
        banco_elem.appendChild(promedio_elem)

        root.appendChild(banco_elem)
    
    with open('promedioPorBanco_MD.xml', 'w', encoding='UTF-8') as file:
        file.write(doc.toprettyxml(indent='    ')) # Guardar el archivo y que se vea bonito

if __name__ == '__main__':
    opc = 0
    rutaArchivo = input("Ingrese la ruta del archivo: ")
    while opc != 6:
        opc = Menu()

        if opc == 1:
            print('')
            LeerArchivoET(rutaArchivo)
            
        elif opc == 2:
            print('')
            LeerArchivoMD(rutaArchivo)
        elif opc == 3:
            print('')
            EscribirArchivoET()

        elif opc == 4:
            print('')
            EscribirArchivoMD()

        elif opc == 5:
            print('')
            listaBancos = []
        elif opc == 6:
            print('Adios')
            break
        else:
            print('Opción no válida')
            continue
        print('')    