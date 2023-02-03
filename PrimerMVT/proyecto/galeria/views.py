from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.shortcuts import render
from galeria.models import Galeria 
from galeria.forms import GaleriaForm
# Create your views here.

def crear(request):
    if request.method == 'GET':
        context = {
            'form': GaleriaForm()
        }

        return render(request, 'galeria/crear.html', context=context)

    elif request.method == 'POST':
        form = GaleriaForm(request.POST, request.FILES)
        if form.is_valid():
            Galeria.objects.create(
                texto=form.cleaned_data['texto'],
                foto = form.cleaned_data['foto'],
            )
            context = {
                'message': 'Creado exitosamente'
            }
            return render(request, 'galeria/crear.html', context=context)
        else:
            context = {
                'form_errors': form.errors,
                'form': GaleriaForm()
            }
            return render(request, 'galeria/crear.html', context=context)

def listar(request):
    if 'search' in request.GET:
        search = request.GET['search']
        galeria = Galeria.objects.filter(texto__icontains=search)
    else:
        galeria = Galeria.objects.all()
    context = {
        'galeria':galeria,
    }
    return render(request, 'galeria/listar.html', context=context)


# Actualiza 
def actualizar(request, pk):
    pais = Galeria.objects.get(id=pk)

    if request.method == 'GET':
        context = {
            'form': GaleriaForm(
                initial={
                    'texto':gal.texto,
                    'foto':gal.foto,                   
                }
            )
        }

        return render(request, 'galeria/actualizar.html', context=context)

    elif request.method == 'POST':
        form = GaleriaForm(request.POST, request.FILES )
        if form.is_valid():
            gal.texto = form.cleaned_data['texto']
            gal.foto =form.cleaned_data['foto'] 
            gal.save()
            
            context = {
                'message': 'Se actualizó correctamente'
            }
        else:
            context = {
                'form_errors': form.errors,
                'form': GaleriaForm()
            }
        return render(request, 'galeria/actualizar.html', context=context)




class eliminar(DeleteView):
    model = Galeria
    template_name = 'galeria/eliminar.html'
    success_url = '/galeria/listar/'  