from django.contrib import admin
from usuarios.models import UsuarioPerfil

@admin.register(UsuarioPerfil)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('telefono', 'fecha_nac')