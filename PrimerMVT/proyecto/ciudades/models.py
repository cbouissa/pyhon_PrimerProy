from django.db import models

# Create your models here.

class Ciudades(models.Model):
    codigoCiudad = models.IntegerField()
    nombre= models.CharField(max_length=100)
    departamento= models.CharField(max_length=100)
    cantidadHabitantes = models.IntegerField()
    