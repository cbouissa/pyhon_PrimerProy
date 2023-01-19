from django.shortcuts import render
from paises.models import Paises 
from paises.forms import PaisesForm
# Create your views here.

def crear_paises(request):
    if request.method == 'GET':
        context = {
            'form': PaisesForm()
        }

        return render(request, 'paises/crear_paises.html', context=context)

    elif request.method == 'POST':
        form = PaisesForm(request.POST)
        if form.is_valid():
            Paises.objects.create(
                codigoPais=form.cleaned_data['codigoPais'],
                nombrePais=form.cleaned_data['nombrePais'],
                poblacionPais=form.cleaned_data['poblacionPais'],
            )
            context = {
                'message': 'Pais creado exitosamente'
            }
            return render(request, 'paises/crear_paises.html', context=context)
        else:
            context = {
                'form_errors': form.errors,
                'form': PaisesForm()
            }
            return render(request, 'paises/crear_paises.html', context=context)

def listar_paises(request):
    if 'search' in request.GET:
        search = request.GET['search']
        paises = Paises.objects.filter(nombrePais__icontains=search)
    else:
        paises = Paises.objects.all()
    context = {
        'paises':paises,
    }
    return render(request, 'paises/listar_paises.html', context=context)

  