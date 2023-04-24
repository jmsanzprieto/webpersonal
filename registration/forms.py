from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Extendemos el formulario principal y le añadimos el email para que sea obligatorio al registrarse
class RegistroConMail(UserCreationForm):
    email = forms.EmailField(required=True, help_text="El correo electrónico es obligatorio y tiene que ser válido.")


    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


    # Validamos el email sea unico
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("El email ya existe.")
        return email