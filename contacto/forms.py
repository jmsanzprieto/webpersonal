# Importamos el módulo de formularios de Django
from django import forms


# Creamos una clase para manejar el formulario

class FormContacto(forms.Form):
    nombre = forms.CharField( required=True, widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Nombre'}))
    email = forms.EmailField( required=True, widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Email'}))
    mensaje = forms.CharField( required=True, widget=forms.Textarea(attrs={'class': 'form-control','placeholder':'Mensaje'}))
