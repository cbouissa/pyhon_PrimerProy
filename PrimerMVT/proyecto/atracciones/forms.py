from django import forms

class AtraccionesForm(forms.Form):
    codigoAtr = forms.IntegerField() 
    nombreAtr = forms.CharField(max_length=100)
    codigoCiudadAtr = forms.IntegerField()
    cantidadPersonas = forms.IntegerField()
    activoAtr = forms.BooleanField()