from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# Importamos el formulario extendido
from .forms import RegistroConMail
# from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django import forms
from .models import Perfil

# Vista del formulario de login
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
            return redirect('login')
    else:
        return render(request, 'core/base.html')
    

# Vista del formulario de registro
class RegistroView(CreateView):
    form_class = RegistroConMail
    template_name = 'registration/registro.html'

    # Si el registro a sido OK, mostramos la info
    def get_success_url(self):
        return reverse_lazy('login') + '?OK_registro'
    

    def get_form(self, form_class=None):
        form = super(RegistroView, self).get_form()
        # Modificar en tiempo real
        form.fields['username'].widget = forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre de usuario'})
        form.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Dirección email'})
        form.fields['password1'].widget = forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Contraseña'})
        form.fields['password2'].widget = forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Repite la contraseña'})
        return form


# Vista del perfil, solo visible a usuarios registrados
@method_decorator(login_required,name="dispatch")
class PerfilUpdate(UpdateView):
    model = Perfil
    fields = ["avatar","bio","link"]
    success_url = reverse_lazy('perfil')
    template_name = 'registration/perfil_usuario.html'

    def get_form(self, form_class=None):
        form = super(PerfilUpdate, self).get_form()
        # Modificar en tiempo real
        form.fields['avatar'].widget.attrs.update({'class':'form-control', 'placeholder':'Avatar'})
        form.fields['bio'].widget.attrs.update({'class':'form-control', 'placeholder':'BIO'})
        form.fields['link'].widget.attrs.update({'class':'form-control', 'placeholder':'URL'})
  
        return form    

    def get_object(self):
        # recuperamos el objeto a editar (en este caso el usuario contectado)
        perfil, create = Perfil.objects.get_or_create(user=self.request.user)
        return perfil