from django.urls import path

from atracciones.views import crear_atracciones, listar_atracciones
urlpatterns = [
    path('crear-atracciones/', crear_atracciones),
    path('listar-atracciones/', listar_atracciones),

   
]