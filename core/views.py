from django.shortcuts import render, HttpResponse,get_object_or_404
from django.views.generic.detail import DetailView



# Importamos el modelo para acceder a la bd
from .models import Pagina
from .utils import obtener_paginas


# Vista pagina about
def about(request):
    return render(request, "core/about.html")

def paginas_context(request):
    return {'paginas': obtener_paginas()}

class pagina(DetailView):
    model = Pagina
    template_name = 'core/pagina.html'
    context_object_name = 'pagina'
    slug_field = 'slug'


