from django.contrib.auth.views import LogoutView
from django.urls import path
from usuarios.views import login_ver, actualizar_usuario, actualizar_usuario_perfil, registro
 
urlpatterns = [
    path('login/', login_ver),
    path('logout/', LogoutView.as_view(template_name = 'usuarios/logout.html')),
    path('signup/', registro),
    path('actualizar/', actualizar_usuario),
    path('actualizar/perfil/', actualizar_usuario_perfil),
]