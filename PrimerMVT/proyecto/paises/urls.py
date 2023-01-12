from django.urls import path

from paises.views import crear_paises, listar_paises


urlpatterns = [
    path('crear-paises/', crear_paises),
    path('listar-paises/', listar_paises),

   
]