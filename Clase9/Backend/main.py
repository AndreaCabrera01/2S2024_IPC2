from flask import Flask, jsonify, request
from flask_cors import CORS
import xml.etree.ElementTree as ET
import re

#  FLask App
app = Flask(__name__)
CORS(app)

listadoPizzas = []
listadoUsuarios = []

# Clases
class Usuario:
    def __init__(self, usuario, fechaCreacion, password, rol):
        self.usuario = usuario
        self.fechaCreacion = fechaCreacion
        self.password = password
        self.rol = rol

class Pizza:
    def __init__(self, nombre, precio, ingredientes, imagen):
        self.id = len(listadoPizzas) + 1
        self.nombre = nombre
        self.precio = precio
        self.ingredientes = ingredientes
        self.imagen = imagen
        self.cantidad = 0


# Routes
@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/api', methods=['GET'])
def api():
    return jsonify({'message': 'Hello, World!'})

@app.route('/config/postXML', methods=['POST'])
def postXML():
    data = request.get_data()
    root = ET.fromstring(data)

    for configListado in root:
        for config in configListado:
            if config.tag == 'Usuario':
                username = config.get('user')
                fechaCreacion = config.find('fecha_creacion').text
                password = config.find('password').text
                rol = config.find('rol').text

                patron_fecha = r'\b(\d{2}/\d{2}/\d{4})\b'
                fechaGuardar = re.search(patron_fecha, fechaCreacion)

                if fechaGuardar:
                    usuario = Usuario(username, fechaGuardar.group(), password, rol)
                    listadoUsuarios.append(usuario)
                else:
                    return jsonify({'message': 'Fecha incorrecta'})

            if config.tag == 'Pizza':
                nombre = config.find('nombre').text
                precio = config.find('precio').text
                ingredientes = config.find('ingredientes').text
                imagen = config.find('imagen').text

                pizza = Pizza(nombre, precio, ingredientes, imagen)
                listadoPizzas.append(pizza)

    return jsonify({'message': 'XML recibido'})

@app.route('/config/obtenerUsuarios', methods=['GET'])
def getUsuarios():
    usuarios = []
    for usuario in listadoUsuarios:
        usuarios.append({'usuario': usuario.usuario, 'fechaCreacion': usuario.fechaCreacion, 'rol': usuario.rol})

    return jsonify({'usuarios': usuarios})

@app.route('/config/obtenerPizzas', methods=['GET'])
def getPizzas():
    pizzas = []
    for pizza in listadoPizzas:
        pizzas.append({'id':pizza.id, 'nombre': pizza.nombre, 'precio': pizza.precio, 'ingredientes': pizza.ingredientes, 'imagen': pizza.imagen})

    return jsonify({'pizzas': pizzas})

    
@app.route('/config/obtenerPizza/<id>', methods=['GET'])
def getPizza(id):
    for pizza in listadoPizzas:
        if pizza.id == int(id):
            return jsonify({'nombre': pizza.nombre, 'precio': pizza.precio, 'ingredientes': pizza.ingredientes, 'imagen': pizza.imagen})

    return jsonify({'message': 'Pizza no encontrada'})



@app.route('/config/comprarPizza/<id>', methods=['POST'])
def comprarPizza(id):
    for pizza in listadoPizzas:
        if pizza.id == int(id):
            pizza.cantidad += 1
            return jsonify({'message': 'Pizza Comprada'})

    return jsonify({'message': 'Pizza no encontrada'})

@app.route('/config/obtenerGraficos', methods=['GET'])
def obtenerGraficos():
    pizzas = []
    cantidades = []

    for pizza in listadoPizzas:
        if pizza.id not in pizzas:
            pizzas.append(pizza.nombre)
            cantidades.append(pizza.cantidad)
        else:
            index = pizzas.index(pizza.nombre)
            cantidades[index] += pizza.cantidad

    respuesta = {}
    for i in range(len(pizzas)):
        respuesta[pizzas[i]] = cantidades[i]

    return jsonify(respuesta)

@app.route('/config/limpiarDatos', methods=['GET'])
def limpiarDatos():
    listadoPizzas.clear()
    listadoUsuarios.clear()
    return jsonify({'message': 'Datos limpiados'})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
