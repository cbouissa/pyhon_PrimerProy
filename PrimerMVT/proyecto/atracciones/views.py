from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.shortcuts import render
from atracciones.models import Atracciones 
from atracciones.forms import AtraccionesForm
# Create your views here.

def crear_atracciones(request):
    if request.method == 'GET':
        context = {
            'form': AtraccionesForm()
        }

        return render(request, 'atracciones/crear_atracciones.html', context=context)

    elif request.method == 'POST':
        form = AtraccionesForm(request.POST)
        if form.is_valid():
            Atracciones.objects.create(
                codigoAtr=form.cleaned_data['codigoAtr'],
                nombreAtr=form.cleaned_data['nombreAtr'],
                precioAtr=form.cleaned_data['precioAtr'],
                cantidadPersonas=form.cleaned_data['cantidadPersonas'],
                activoAtr=form.cleaned_data['activoAtr'],
            )
            context = {
                'message': 'Atracción creada exitosamente'
            }
            return render(request, 'atracciones/crear_atracciones.html', context=context)
        else:
            context = {
                'form_errors': form.errors,
                'form': AtraccionesForm()
            }
            return render(request, 'atracciones/crear_atracciones.html', context=context)


def listar_atracciones(request):
    if 'search' in request.GET:
        search = request.GET['search']
        atraciones = Atracciones.objects.filter(name__icontains=search)
    else:
        atracciones = Atracciones.objects.all()
    context = {
        'atracciones':atracciones,
    }
    return render(request, 'atracciones/listar_atracciones.html', context=context)


# Actualiza 
def actualizar_atracciones(request, pk):
    atraccion = Atracciones.objects.get(id=pk)

    if request.method == 'GET':
        context = {
            'form': AtraccionesForm(
                initial={
                    'codigoAtr':atraccion.codigoAtr,
                    'nombreAtr':atraccion.nombreAtr,
                    'precioAtr':atraccion.precioAtr,
                    'cantidadPersonas':atraccion.cantidadPersonas,
                    'activoAtr':atraccion.activoAtr,
                }
            )
        }

        return render(request, 'atracciones/actualizar_atracciones.html', context=context)

    elif request.method == 'POST':
        form = AtraccionesForm(request.POST)
        if form.is_valid():
            atraccion.codigoAtr = form.cleaned_data['codigoAtr']
            atraccion.nombreAtr = form.cleaned_data['nombreAtr']
            atraccion.precioAtr = form.cleaned_data['precioAtr']
            atraccion.cantidadPersonas = form.cleaned_data['cantidadPersonas']
            atraccion.activoAtr = form.cleaned_data['activoAtr']
            atraccion.save()
            
            context = {
                'message': 'Se actualizó correctamente '
            }
        else:
            context = {
                'form_errors': form.errors,
                'form': AtraccionesForm()
            }
        return render(request, 'atracciones/actualizar_atracciones.html', context=context)




class eliminar_atracciones(DeleteView):
    model = Atracciones
    template_name = 'ciudades/eliminar_ciudades.html'
    success_url = '/ciudades/listar-ciudades/'  