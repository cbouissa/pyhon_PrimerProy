from django.contrib import admin
from ciudades.models import Ciudades

@admin.register(Ciudades)
class ciudadesAdmin(admin.ModelAdmin):
    list_display = ('nombre','departamento')
