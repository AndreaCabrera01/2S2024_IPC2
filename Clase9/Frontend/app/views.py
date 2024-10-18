from django.shortcuts import render
from .forms import FileForm
import requests

#pip install plotly
import plotly.graph_objs as go
import plotly.offline as pyo


api = 'http://localhost:5000'

# Create your views here.
def index(request):
    return render(request, 'homepage.html')

def cardsPizza(request):
    context = {
        'pizzas': None
    }

    response = requests.get(api+'/config/obtenerPizzas')

    if response.status_code == 200:
        context['pizzas'] = response.json()['pizzas']
        return render(request, 'cardsPizza.html', context)
    else:
        context['pizzas'] = []
        return render(request, 'cardsPizza.html')

def verPizzaDetalle(request, id):
    context = {
        'pizzas': None
    }

    response = requests.get(api+'/config/obtenerPizza/'+id)
    if response.status_code == 200:
        context['pizza'] = response.json()
        return render(request, 'detailPizza.html', context)
    else:
        context['pizzas'] = []
        return render(request, 'detailPizza.html')

def configurar(request):
    xmlContent = None
    return render(request, 'configurar.html', {'xmlContent': xmlContent})


def visualizarXML(request):
    xml_content = ""
    print("AAAAA1")


    if request.method == 'POST':
        print("AAAAA")
    
        form = FileForm(request.POST, request.FILES)

        if form.is_valid():
            file = form.cleaned_data['file']
            xml_content = file.read().decode('utf-8')
            print(xml_content)
        else:
            print(form.errors)
    return render(request, 'configurar.html', {'xml_content': xml_content})

def realizarPedido(request, id):
    response = requests.post(api+'/config/comprarPizza/'+id)

    context = {
        'pizzas': None
    }

    response2 = requests.get(api+'/config/obtenerPizzas')

    if response.status_code == 200:
        context['pizzas'] = response2.json()['pizzas']
        return render(request, 'cardsPizza.html', context)
    else: 
        context['pizzas'] = []
        return render(request, 'cardsPizza.html', context)


def verEstadisticas(request):
    response = requests.get(api+'/config/obtenerGraficos')

    print(response.json())

    pizzas = []
    cantidades = []

    if response.status_code == 200:
        data = response.json()

        for pizza in data: 
            pizzas.append(pizza)
            print(pizza)

            cantidades.append(data[pizza])


        context = {
            'pizzas': pizzas,
            'cantidades': cantidades,
            'listado': []
        }

        jsondata = response.json()

        context['listado'] = jsondata

    return render(request, 'verEstadisticas.html', context) 


def plot_view(request):
    response = requests.get(api+'/config/obtenerGraficos')

    pizzas = []
    cantidades = []
    
    if response.status_code == 200:
        data = response.json()
        for pizza in data:
            pizzas.append(pizza)
            print(pizza)

            cantidades.append(data[pizza])
            print(data[pizza])

        context = {
            'pizzas': pizzas,
            'cantidades': cantidades,
        }

        trace = go.Bar(
            y=context['cantidades'],
            x=context['pizzas']
        )

        layout = go.Layout(
            title='Cantidad de Pizzas compradas',
            xaxis={'title': 'Pizza'},
            yaxis={'title': 'Compras'}
        )

        fig = go.Figure(data=[trace], layout=layout)
        plot_div = pyo.plot(fig, include_plotlyjs=False, output_type='div')

        return render(request, 'plot.html', {'plot_div': plot_div})


def subirXML(request):
    xml_content = ""

    if request.method == 'POST':
        xml_content = request.POST.get('xml', '')

        cleaned_xml_content = xml_content.encode('utf-8')
        response = requests.post(api+'/config/postXML', data=cleaned_xml_content)

        if response.status_code == 200:
            print(response.json())

    return render(request, 'configurar.html', {'xml_content': xml_content, 'response': response.json().get('message', '')})