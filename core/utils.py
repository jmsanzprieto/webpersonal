# en app/utils.py
from .models import Pagina

def obtener_paginas():
    return Pagina.objects.all()

def agregar_lenguajes_al_contexto(request):
    LANGUAGES = [
        ('en', 'English'),
        ('es', 'Español'),
    ]
    return {
        'LANGUAGES': LANGUAGES
    }

  
