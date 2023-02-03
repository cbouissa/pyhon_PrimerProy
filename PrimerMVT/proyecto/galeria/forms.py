from django import forms

class GaleriaForm(forms.Form):
    texto = forms.CharField(max_length=100)
    foto = forms.ImageField() 