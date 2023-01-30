from django.urls import path

from ciudades.views import crear_ciudades, listar_ciudades, actualizar_ciudades, eliminar_ciudades


urlpatterns = [
    path('crear-ciudades/', crear_ciudades),
    path('listar-ciudades/', listar_ciudades),
    path('actualizar-ciudades/<int:pk>/', actualizar_ciudades, name='actualizar_ciudades'),
    path('eliminar-ciudades/<int:pk>/', eliminar_ciudades.as_view(), name='eliminar_ciudades'),
   
   
]