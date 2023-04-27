from django.shortcuts import render,redirect, get_object_or_404
# Importamos la libreria para poder enviar correos
from django.core.mail import EmailMessage
from django.urls import reverse
from .models import Secreto
from .forms import FormularioTexto
import secrets
from django.http import Http404, HttpResponse


def secretos(request):
    form = FormularioTexto()
    return render(request, 'secretos/crear_secreto.html', {'form': form})

def confirmacion(request, hash):
    return render(request, 'secretos/enlace_secreto.html', {'hash': hash})


def ver_secreto(request, hash):
    try:
        secreto = Secreto.objects.get(hash=hash)
        mensaje = secreto.mensaje
        secreto.delete()  # Eliminar el secreto de la base de datos
        return render(request, 'secretos/ver_secreto.html', {'mensaje': mensaje})
    except Secreto.DoesNotExist:
        return render(request, 'secretos/secreto_borrado.html')

def enviar_email(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        hash_value = request.POST.get('hash')
        print('Email:', email)
        print('Hash:', hash_value)
    return render(request, 'form.html')


def procesar_secretos(request):
    if request.method == 'POST':
        form = FormularioTexto(request.POST)
        if form.is_valid():
            # Genera un hash alfanumérico aleatorio de 40 caracteres
            hash_aleatorio = secrets.token_hex(20)
            # Agrega el hash al formulario antes de guardarlo
            secreto = Secreto(
                hash=hash_aleatorio,
                mensaje=form.cleaned_data['mensaje']
            )
            secreto.save()
            # Redirige al usuario a la página de confirmación
            return redirect('confirmacion', hash=hash_aleatorio)
        else:
            # Genera un hash alfanumérico aleatorio de 40 caracteres
            hash_aleatorio = secrets.token_hex(20)
            # Crea un formulario con el hash aleatorio como valor inicial del campo hash
            form = FormularioTexto(initial={'hash': hash_aleatorio})
    else:
        # Genera un hash alfanumérico aleatorio de 40 caracteres
        hash_aleatorio = secrets.token_hex(20)
        # Crea un formulario con el hash aleatorio como valor inicial del campo hash
        form = FormularioTexto(initial={'hash': hash_aleatorio})
    return render(request, 'secretos/crear_secreto.html', {'form': form})



