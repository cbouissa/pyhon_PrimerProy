from django.db import models

# Create your models here.

class Atracciones(models.Model):
    codigoAtr = models.IntegerField()
    nombreAtr  = models.CharField(max_length=100)
    codigoCiudadAtr = models.IntegerField()
    cantidadPersonas = models.IntegerField()
    activoAtr = models.BooleanField()

    