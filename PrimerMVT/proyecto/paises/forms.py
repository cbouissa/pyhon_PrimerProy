from django import forms

class PaisesForm(forms.Form):
    codigoPais = forms.IntegerField() 
    nombrePais = forms.CharField(max_length=100)
    poblacionPais = forms.IntegerField()
    bandera = forms.ImageField() 