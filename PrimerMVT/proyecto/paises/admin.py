from django.contrib import admin

# Register your models here.


from paises.models import Paises

# admin.site.register(Paises)

@admin.register(Paises)
class PaisesAdmin(admin.ModelAdmin):
    list_display = ('codigoPais', 'nombrePais', 'poblacionPais','bandera')
    list_filter = ('codigoPais',)
    search_fields = ('nombrePais',)
