from django.db import models

# Create your models here.

class Paises(models.Model):
    codigoPais= models.IntegerField()
    nombrePais= models.CharField(max_length=100)  
    poblacionPais = models.IntegerField()


def __str__(self):
    return self.nombrePais