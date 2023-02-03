from django.db import models

# Create your models here.

class Galeria(models.Model):
    texto= models.CharField(max_length=100)  
    foto = models.ImageField(upload_to='foto_images', null=True, blank=True)


def __str__(self):
    return self.texto