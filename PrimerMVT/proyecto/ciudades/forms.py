from django import forms

class CiudadesForm(forms.Form):
    codigoCiudad = forms.IntegerField() 
    nombre = forms.CharField(max_length=100)
    departamento = forms.CharField(max_length=100)
    cantidadHabitantes = forms.IntegerField()