from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render

def hola_mundo(request):
    return HttpResponse('Hola mundo')

def fecha_actual(request):
    hoy = datetime.now().date
    return HttpResponse(f'La fecha de hoy es {hoy}')    

def vista_con_edad(request,edad):   
    return HttpResponse(f'La edad es {edad}') 

def vista_con_template(request):   
    return render(request,'templates.html',context={}) 

def saludo_desde_template(request):   
    nombre = 'Clau'
    context = {
        'nombre' : 'Clau',
        'edad' : 47,
        'usa lentes?': True,
        'lista': [1,2,3,4]

    }
    return render(request,'saludo.html',context=context)     

 