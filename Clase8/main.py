from flask import Flask, render_template, request, url_for, redirect
app = Flask(__name__)
import xml.etree.ElementTree as ET


@app.route('/')
def index():
    return "Hello World!"

@app.route('/lecturaXML', methods=['POST'])
def lecturaXML():
    textoXML = request.data

    try:
        xml = ET.fromstring(textoXML)

        for curso_elem in xml.findall('curso'): # Iterar
            nombreCurso = curso_elem.get('nombre') # Obtener el atributo nombre del nodo curso
            seccionCurso = curso_elem.find('seccion').text # Obtener el texto del nodo seccion
            aulaCurso = curso_elem.find('aula').text

            print("Nombre: ", nombreCurso)
            print("Seccion: ", seccionCurso)
            print("Aula: ", aulaCurso)

    except Exception as e:
        return str(e)

    return "Se leyó correctamente el XML"

if __name__ == '__main__':
    app.run(debug=True)