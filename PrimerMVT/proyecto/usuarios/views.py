from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from usuarios.models import UsuarioPerfil
from usuarios.forms import RegistroForm, UsuarioActualizarForm, UsuarioPerfilForm

def login_ver(request):
    if request.method == 'GET':
        form = AuthenticationForm()
        context = {
            'form':form
        }
        return render(request, 'usuarios/login.html', context=context)
    
    elif request.method == 'POST':
        form = AuthenticationForm(request = request, data = request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=password)

            if user is not None:
                login(request, user)
                context = {
                    'message':f'Bienvenido {usuario}!!!'
                }
                return render(request, 'index.html', context=context)

        form = AuthenticationForm()
        context ={
            'form':form,
            'errors':'Usuario o contraseña incorrectos!'
        }
        return render(request, 'usuarios/login.html', context=context)

def registro(request):
    if request.method == 'GET':
        form = RegistroForm()
        context ={
            'form':form
        }
        return render(request, 'usuarios/registro.html', context=context)

    elif request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save() #crea el usuario
            UsuarioPerfil.objects.create(user=user)
            return redirect('login')
        
        context = {
            'errors':form.errors,
            'form':RegistroForm()
        }
        return render(request, 'usuarios/registro.html', context=context)

@login_required
def actualizar_usuario(request):
    user = request.user
    if request.method == 'GET':
        form = UsuarioActualizarForm(initial = {
            'usuario':user.username,
            'nombre':user.first_name,
            'apellido':user.last_name
        })
        context ={
            'form':form
        }
        return render(request, 'usuarios/actualizar_usuarios.html', context=context)

    elif request.method == 'POST':
        form = UsuarioActualizarForm(request.POST)
        if form.is_valid():
            user.username = form.cleaned_data.get('username')
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.save()
            return redirect('index')
        
        context = {
            'errors':form.errors,
            'form':RegistroForm()
        }
        return render(request, 'usuarios/actualizar_usuario.html', context=context)

def actualizar_usuario_perfil(request):
    user = request.user
    if request.method == 'GET':
        form = UsuarioPerfilForm(initial={
            'telefono':request.user.profile.phone,
            'fecha_nac':request.user.profile.birth_date,
            'foto':request.user.profile.profile_picture
        })
        context ={
            'form':form
        }
        return render(request, 'usuarios/actualizar_perfil.html', context=context)

    elif request.method == 'POST':
        form = UsuarioPerfilForm(request.POST, request.FILES)
        if form.is_valid():
            user.profile.phone = form.cleaned_data.get('phone')
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.profile.profile_picture = form.cleaned_data.get('profile_picture')
            user.profile.save()
            return redirect('index')
        
        context = {
            'errors':form.errors,
            'form':UsuarioPerfilForm()
        }
        return render(request, 'usuarios/registro.html', context=context)
