from django.shortcuts import render
from .forms import FileForm
import requests

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


def subirXML(request):
    xml_content = ""

    if request.method == 'POST':
        xml_content = request.POST.get('xml', '')

        cleaned_xml_content = xml_content.encode('utf-8')
        response = requests.post(api+'/config/postXML', data=cleaned_xml_content)

        if response.status_code == 200:
            print(response.json())

    return render(request, 'configurar.html', {'xml_content': xml_content, 'response': response.json().get('message', '')})