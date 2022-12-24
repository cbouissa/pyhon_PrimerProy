from django.db import models

# Create your models here.

class Family(models.Model):
    name= models.CharField(max_length=100)
    age = models.IntegerField()
    sex = models.CharField(max_length=1)
    smoker = models.BooleanField()
   