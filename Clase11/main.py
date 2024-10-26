from flask import Flask, jsonify, request
from flask_cors import CORS
import xml.etree.ElementTree as ET
import re
from xml.dom import minidom

app = Flask(__name__)
CORS(app)

mensaje = ""
listadoPositivas = []
listadoNegativas = []
listadoEmpresas = []

posiblesEstados = {0: "Positivo", 1: "Negativo", 2: "Neutro"}

# Clases:
class Empresa:
    def __init__(self, nombre):
        self.nombre = nombre
        self.servicios = []

    def __str__(self):
        return f'Empresa: {self.nombre}, Servicios: {self.servicios}'
    
    def to_dict(self):
        return {
            'nombre': self.nombre,
            'servicios': [servicio.__dict__ for servicio in self.servicios]
        }

class Servicio:
    def __init__(self, nombre):
        self.nombre = nombre
        self.alias = []

    def  __str__(self):
        return f'Servicio: {self.nombre}, Alias: {self.alias}'

    def to_dict(self):
        return {
            'nombre': self.nombre,
            'alias': self.alias
        }


@app.route('/')
def index():
    return 'HOLA, SI FUNCIONA :D'

@app.route('/config/leerDiccionario', methods=['POST'])
def postConfiguracion():
    data = request.get_data()
    root = ET.fromstring(data)

    # Leyendo pos.
    for palabra in root.find('sentimientos_positivos'):
        listadoPositivas.append(palabra.text.strip())

    # Leyendo neg.
    for palabra in root.find('sentimientos_negativos'):
        listadoNegativas.append(palabra.text.strip())

    # empresas:
    for empresa in root.find('empresas_analizar'):
        nombreE = empresa.find('nombre').text.strip().lower()
        empresaObj = Empresa(nombreE)
        print(nombreE)
        #servicios
        servicios = empresa.find('servicios')
        for servicio in servicios.findall('servicio'):
            nombreS = servicio.get('nombre').strip().lower()

            servicioObj = Servicio(nombreS)

            # alias:
            for alias in servicio.findall('alias'):
                servicioObj.alias.append(alias.text.strip().lower())

            empresaObj.servicios.append(servicioObj)


        listadoEmpresas.append(empresaObj)

    
    return jsonify({
        'mensaje': 'si se guardó todo',
        'positivas': listadoPositivas,
        'negativas': listadoNegativas,
        'empresas': [empresa.to_dict() for empresa in listadoEmpresas]
    }), 200
    

@app.route('/analisis/analizarMU', methods=['POST'])
def analizarMU():
    data = request.get_data()
    root = ET.fromstring(data)


    
    mensaje_texto = root.text.strip()
    
    fecha = re.search(r'(\d{2}/\d{2}/\d{4})', mensaje_texto).group(1)
    usuario = re.search(r'Usuario: ([^\s]+)', mensaje_texto).group(1)
    red_social = re.search(r'Red social: ([^\s]+)', mensaje_texto).group(1)



    palabras = re.findall(r'\b\w+\b', mensaje_texto.lower())
    contador_positivas = sum(1 for palabra in palabras if palabra in listadoPositivas)
    contador_negativas = sum(1 for palabra in palabras if palabra in listadoNegativas)


    total_palabras = contador_positivas + contador_negativas
    sentimiento_positivo = (contador_positivas / total_palabras * 100) if total_palabras > 0 else 0
    sentimiento_negativo = (contador_negativas / total_palabras * 100) if total_palabras > 0 else 0

    sentimiento_analizado = "neutro"

    if sentimiento_positivo > sentimiento_negativo:
        sentimiento_analizado = 'positivo'
    elif sentimiento_positivo == sentimiento_negativo:
        sentimiento_analizado = 'neutro'
    else:
        sentimiento_analizado = 'negativo'
    # Generar respuesta XML:
    respuesta = ET.Element("respuesta")
    ET.SubElement(respuesta, "fecha").text = fecha
    ET.SubElement(respuesta, "red_social").text = red_social
    ET.SubElement(respuesta, "usuario").text = usuario

    empresas = ET.SubElement(respuesta, "empresas")
    '''
     1. Ver qué empresas se encuentran en el listado de palabras obtenido del mensaje
     2. Ver qué alias se encuentra del servicio de la empresa encontrada en el mensaje
     3. ponerlo como salida del XML
    '''

    for empresa in listadoEmpresas:
        if empresa.nombre in palabras:
            empresa_elem = ET.SubElement(empresas, "empresa", nombre=empresa.nombre)
            for servicio in empresa.servicios:
                if servicio.nombre in palabras or any(alias in palabras for alias in servicio.alias):
                    ET.SubElement(empresa_elem, "servicio").text = servicio.nombre

    ET.SubElement(respuesta, "palabras_positivas").text = str(contador_positivas)
    ET.SubElement(respuesta, "palabras_negativas").text = str(contador_negativas)
    ET.SubElement(respuesta, "sentimiento_positivo").text = f"{sentimiento_positivo:.2f}%"
    ET.SubElement(respuesta, "sentimiento_negativo").text = f"{sentimiento_negativo:.2f}%"
    ET.SubElement(respuesta, "sentimiento_analizado").text = sentimiento_analizado

    # Convertir a XML
    respuesta_xml = ET.tostring(respuesta, encoding='UTF-8')

    # minidom:
    respuesta_xml = minidom.parseString(respuesta_xml).toprettyxml()

    #print(respuesta_xml)

    return respuesta_xml, 200

if __name__ == "__main__":
    app.run(debug=True, port=5000)