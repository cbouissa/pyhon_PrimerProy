from django.urls import path

from atracciones.views import crear_atracciones, listar_atracciones, actualizar_atracciones, eliminar_atracciones
urlpatterns = [
    path('crear-atracciones/', crear_atracciones),
    path('listar-atracciones/', listar_atracciones),
    path('actualizar-atracciones/<int:pk>/', actualizar_atracciones, name='actualizar_atracciones'),
    path('eliminar-atracciones/<int:pk>/', eliminar_atracciones.as_view(), name='eliminar_atracciones'),
   
   
]