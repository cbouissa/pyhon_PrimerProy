from django.contrib import admin
from galeria.models import Galeria

@admin.register(Galeria)
class galeriaAdmin(admin.ModelAdmin):
    list_display = ('texto','foto')