from django.urls import path

from galeria.views import crear, listar, actualizar, eliminar


urlpatterns = [
    path('crear/', crear),
    path('listar/', listar),
    path('actualizar/<int:pk>/', actualizar, name='actualizar'),
    path('eliminar/<int:pk>/', eliminar.as_view(), name='eliminar'),
   
]