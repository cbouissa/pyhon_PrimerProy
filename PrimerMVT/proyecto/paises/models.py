from django.db import models

# Create your models here.

class Paises(models.Model):
    codigoPais= models.IntegerField()
    nombrePais= models.CharField(max_length=100)  
    poblacionPais = models.IntegerField()
    bandera = models.ImageField(upload_to='bandera_images', null=True, blank=True)


def __str__(self):
    return self.nombrePais