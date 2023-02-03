
from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static

from proyecto.settings import MEDIA_ROOT, MEDIA_URL

from proyecto.views import index
urlpatterns = [
   path('', index, name='index'),  
   path('admin/', admin.site.urls),    
   path('paises/', include('paises.urls')),
   path('ciudades/', include('ciudades.urls')), 
   path('atracciones/', include('atracciones.urls')), 
   path('usuarios/', include('usuarios.urls')), 
   path('galeria/', include('galeria.urls')), 
]  

urlpatterns+= static(MEDIA_URL, document_root = MEDIA_ROOT)