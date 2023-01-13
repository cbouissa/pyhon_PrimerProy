from django.urls import path

from ciudades.views import crear_ciudades, listar_ciudades


urlpatterns = [
    path('crear-ciudades/', crear_ciudades),
    path('listar-ciudades/', listar_ciudades),

   
]