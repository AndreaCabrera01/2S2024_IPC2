from flask import Flask, render_template, request, url_for, redirect
# importando clase Animal
from animal import Animal

app = Flask(__name__)

animales = []


@app.route('/ping')
def ping():
    return 'pong'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/Agregar')
def agregar():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    #OBTENER VALORES DEL FORMS
    nombre = request.form['nombre']
    edad = request.form['edad']
    tipo = request.form['tipo']

    animalCreado = Animal(nombre, edad, tipo)
    animales.append(animalCreado)

    print(animalCreado)

    return redirect(url_for('agregar'))

@app.route('/listar')
def listar():
    return render_template('listar.html', listado=animales)



if __name__ == '__main__':
    app.run(debug=True)