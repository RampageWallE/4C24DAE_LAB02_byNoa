from django.shortcuts import render

def index (request):
    context = {
        'titulo' : "Operaciones basicas",
    }
    return render( request, 'operaciones/formulario.html', context)

def enviar_op (request):
    operacion = request.POST['operacion']
    numero1 = float(request.POST['numero1'])
    numero2 =  float(request.POST['numero2'])
    match operacion:
        case "suma":
            resultado = numero1 + numero2
        case "resta":
            resultado = numero1 - numero2
        case "multiplicacion": 
            resultado = numero1 * numero2 
        case _:
            resultado = 0
    context = {        
        'titulo': "Respuesta",
        'operacion' : operacion,
        'numero1': numero1, 
        'numero2': numero2,
        'resultado' : resultado,
    }
    return render(request, 'operaciones/respuesta.html', context)
