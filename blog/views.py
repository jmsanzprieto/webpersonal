from django.shortcuts import get_object_or_404,render,redirect
from django.views.generic.detail import DetailView
#from django.http import HttpResponseRedirect
from django.urls import reverse

# Importamos el modelo para acceder a la bd
from .models import Blog,Comentario


# Importamos el formulario que hemos creado
from .forms import FormComentario

# Create your views here.

# Vista página principal
def home(request):
    # Llamamos a la lista de noticias
    noticias = Blog.objects.all()
    # Añadiendo un tercer parametro a render, añadimos la lista de campos que vamos a exportar al template (el contenido de las notiicas)
    return render(request, "blog/home.html", {'noticias':noticias})


class noticia(DetailView):
    model = Blog
    template_name = 'blog/noticia.html'
    context_object_name = 'noticia'
    slug_field = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_comentario'] = FormComentario()
        return context


# Guardar comentarios
def agregar_comentario(request):
    if request.method == 'POST':
        # Crear una instancia de Comentario
        comentario = Comentario()

        # Asignar los valores ingresados en el formulario a los campos correspondientes del modelo Comentario
        comentario.nombre = request.POST.get('nombre')
        comentario.email = request.POST.get('email')
        comentario.contenido = request.POST.get('mensaje')
        nombre_pagina = request.POST.get('pagina')

        # Guardar el comentario en la base de datos
        try:
            comentario.save()
            return redirect('/blog/'+nombre_pagina+"?OK")
        except:
            return redirect('/blog/'+nombre_pagina+"?KO")
            


