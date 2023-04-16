from django.shortcuts import render, HttpResponse, get_object_or_404
from django.views.generic.detail import DetailView
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import redirect
from django.utils.translation import activate, gettext as _
from django.views.i18n import set_language


# Importamos el modelo para acceder a la bd
from .models import Pagina
from blog.models import Blog, Categoria
from .utils import obtener_paginas
from blog.utils import mas_leidas,lista_categorias


def paginas_context(request):
    return {'paginas': obtener_paginas()}

def noticias_context(request):
    return {'mas_leidas': mas_leidas()}

def categorias_context(request):
    return {'categorias': lista_categorias()}



class pagina(DetailView):
    model = Pagina
    template_name = 'core/pagina.html'
    context_object_name = 'pagina'
    slug_field = 'slug'


def change_language(request, language):
    activate(language)
    set_language(request)
    response = redirect(request.META.get('HTTP_REFERER', '/'))
    response.set_cookie('django_language', language)
    messages.success(request, _('Idioma cambiado con éxito.'))
    return response