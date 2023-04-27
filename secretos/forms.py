from django import forms
import secrets

class FormularioTexto(forms.Form):
    mensaje = forms.CharField( required=True, widget=forms.Textarea(attrs={'class': 'form-control','placeholder':'Mensaje'}))


