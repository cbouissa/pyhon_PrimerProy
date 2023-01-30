from django.views.generic import ListView, CreateView, DeleteView, UpdateView
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


# Actualiza 
def actualizar_ciudades(request, pk):
    ciudad = Ciudades.objects.get(id=pk)

    if request.method == 'GET':
        context = {
            'form': CiudadesForm(
                initial={
                    'codigoCiudad':ciudad.codigoCiudad,
                    'nombre':ciudad.nombre,
                    'departamento':ciudad.departamento,   
                    'cantidadHabitantes':ciudad.cantidadHabitantes,                
                }
            )
        }

        return render(request, 'ciudades/actualizar_ciudades.html', context=context)

    elif request.method == 'POST':
        form = CiudadesForm(request.POST)
        if form.is_valid():
            ciudad.codigoCiudad = form.cleaned_data['codigoCiudad']
            ciudad.nombre = form.cleaned_data['nombre']
            ciudad.departamento = form.cleaned_data['departamento']
            ciudad.cantidadHabitantes = form.cleaned_data['cantidadHabitantes']
            ciudad.save()
            
            context = {
                'message': 'Se actualizó correctamente la ciudad'
            }
        else:
            context = {
                'form_errors': form.errors,
                'form': CiudadesForm()
            }
        return render(request, 'ciudades/actualizar_ciudades.html', context=context)




class eliminar_ciudades(DeleteView):
    model = Ciudades
    template_name = 'ciudades/eliminar_ciudades.html'
    success_url = '/ciudades/listar-ciudades/'  