from django.contrib import admin
from atracciones.models import Atracciones

@admin.register(Atracciones)
class atraccionesAdmin(admin.ModelAdmin):
    list_display = ('nombreAtr', 'activoAtr')