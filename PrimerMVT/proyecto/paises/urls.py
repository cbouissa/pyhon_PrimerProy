from django.urls import path

from paises.views import crear_paises, listar_paises, actualizar_paises, eliminar_paises


urlpatterns = [
    path('crear-paises/', crear_paises),
    path('listar-paises/', listar_paises),
    path('actualizar-paises/<int:pk>/', actualizar_paises, name='actualizar_paises'),
    path('eliminar-paises/<int:pk>/', eliminar_paises.as_view(), name='eliminar_paises'),
   
]