from django.shortcuts import render
from ciudades.models import Ciudades 
from ciudades.forms import CiudadesForm
# Create your views here.

def crear_ciudades(request):
    if request.method == 'GET':
        context = {
            'form': CiudadesForm()
        }

        return render(request, 'ciudades/crear_ciudades.html', context=context)

    elif request.method == 'POST':
        form = CiudadesForm(request.POST)
        if form.is_valid():
            Ciudades.objects.create(
                codigoCiudad=form.cleaned_data['codigoCiudad'],
                nombre=form.cleaned_data['nombre'],
                departamento=form.cleaned_data['departamento'],
                cantidadHabitantes=form.cleaned_data['cantidadHabitantes'],
            )
            context = {
                'message': 'Ciudad creada exitosamente'
            }
            return render(request, 'ciudades/crear_ciudades.html', context=context)
        else:
            context = {
                'form_errors': form.errors,
                'form': CiudadesForm()
            }
            return render(request, 'ciudades/crear_ciudades.html', context=context)

def listar_ciudades(request):
    if 'search' in request.GET:
        search = request.GET['search']
        ciudades = Ciudades.objects.filter(name__icontains=search)
    else:
        ciudades = Ciudades.objects.all()
    context = {
        'ciudades':ciudades,
    }
    return render(request, 'ciudades/listar_ciudades.html', context=context)
