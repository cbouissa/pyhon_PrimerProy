from django.contrib.auth.models import User
from django.db import models

class UsuarioPerfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    telefono = models.CharField(max_length=25, null=True, blank=True)
    fecha_nac = models.DateField(null=True, blank=True)
    foto = models.ImageField(upload_to='profile_images', null=True, blank=True)
    

def __str__(self): 
        return f"{self.usuario} - {self.foto}"