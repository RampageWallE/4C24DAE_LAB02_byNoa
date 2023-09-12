from django.shortcuts import render
import math

def index (request):
    context = {
        'titulo' : "Calcular el volumen del cilindro",
    }
    return render( request, 'volumencilindro/formulario.html', context)

def enviar_vol (request):
    diametro = float(request.POST['diametro'])
    altura =  float(request.POST['altura'])
    resultado = (math.pi*(diametro/2)**2)*(altura)
    context = {        
        'titulo': "Respuesta",
        'diametro': diametro, 
        'altura': altura,
        'resultado' : resultado,
    }
    return render(request, 'volumencilindro/respuesta.html', context)

