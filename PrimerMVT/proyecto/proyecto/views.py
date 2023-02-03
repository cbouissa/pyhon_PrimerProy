from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render
from galeria.models import Galeria 

def index(request):
    galeria = Galeria.objects.all()
    context = {
        'galeria':galeria,
    }
    return render(request,'index.html',context=context)

