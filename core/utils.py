# en app/utils.py
from .models import Pagina

def obtener_paginas():
    return Pagina.objects.all()
