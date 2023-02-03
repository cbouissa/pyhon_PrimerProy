from django.views.generic import ListView, CreateView, DeleteView, UpdateView
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
        form = PaisesForm(request.POST, request.FILES)
        if form.is_valid():
            Paises.objects.create(
                codigoPais=form.cleaned_data['codigoPais'],
                nombrePais=form.cleaned_data['nombrePais'],
                poblacionPais=form.cleaned_data['poblacionPais'],
                bandera = form.cleaned_data['bandera'],
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


# Actualiza paises
def actualizar_paises(request, pk):
    pais = Paises.objects.get(id=pk)

    if request.method == 'GET':
        context = {
            'form': PaisesForm(
                initial={
                    'codigoPais':pais.codigoPais,
                    'nombrePais':pais.nombrePais,
                    'poblacionPais':pais.poblacionPais,  
                    'bandera':pais.bandera,                   
                }
            )
        }

        return render(request, 'paises/actualizar_paises.html', context=context)

    elif request.method == 'POST':
        form = PaisesForm(request.POST, request.FILES )
        if form.is_valid():
            pais.codigoPais = form.cleaned_data['codigoPais']
            pais.nombrePais = form.cleaned_data['nombrePais']
            pais.poblacionPais = form.cleaned_data['poblacionPais']
            pais.bandera =form.cleaned_data['bandera'] 
            pais.save()
            
            context = {
                'message': 'Se actualizó correctamente el país'
            }
        else:
            context = {
                'form_errors': form.errors,
                'form': PaisesForm()
            }
        return render(request, 'paises/actualizar_paises.html', context=context)




class eliminar_paises(DeleteView):
    model = Paises
    template_name = 'paises/eliminar_paises.html'
    success_url = '/paises/listar-paises/'  