from django.shortcuts import get_object_or_404,render,redirect
from django.views.generic.detail import DetailView
#from django.http import HttpResponseRedirect
from django.urls import reverse
from registration.models import Perfil
from django.core.mail import send_mail
from django.conf import settings

# Importamos el modelo para acceder a la bd
from .models import Blog,Comentario,Categoria


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
    
        # Obtener comentarios aprobados de la noticia
        comentarios_aprobados = self.object.comentarios.filter(aprobado=True)
        context['comentarios_aprobados'] = comentarios_aprobados

        # Llamar al método aumentar_visitas() del modelo Blog
        self.object.aumentar_visitas()

        return context

# Mostramos las noticias de una categoria concreta 
class categoria(DetailView):
    model = Categoria
    template_name = 'blog/categoria.html'
    context_object_name = 'categoria'
    slug_field = 'slug'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Obtener la categoría actual
        categoria_actual = self.get_object()

        # Obtener todas las noticias relacionadas con la categoría actual
        noticias = categoria_actual.get_noticias()

        context['noticias'] = noticias
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
        # Obtener el objeto Blog correspondiente
        try:
            blog = Blog.objects.get(slug=nombre_pagina)
        except Blog.DoesNotExist:
            return redirect('/blog/'+nombre_pagina+"?KO#comentario")

        # Agregar el objeto Blog al campo de ManyToManyField del modelo Comentario
        comentario.save() # Guardar el comentario para obtener un ID
        comentario.blog.add(blog) # Agregar el objeto Blog

        # Obtener el perfil del usuario que creó el comentario si existe
        perfil = None
        try:
            perfil = Perfil.objects.get(user__email=comentario.email)
        except Perfil.DoesNotExist:
            pass

        # Asignar el avatar correspondiente al comentario
        if perfil:
            comentario.avatar = perfil.avatar
        else:
            # Asignar una imagen predeterminada
            default_avatar = '/media/perfil/img_avatar_default.jpg'
            comentario.avatar = default_avatar
        
        # Enviar un correo al superusuario con la información del comentario
        subject = 'Nuevo comentario en el blog'
        message = f'Nombre: {comentario.nombre}\nEmail: {comentario.email}\nContenido: {comentario.contenido}'
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [settings.DEFAULT_FROM_EMAIL])


        return redirect('/blog/'+nombre_pagina+"?OK#comentario")
    
# Buscar resultados
def buscar_noticias(request):
    query = request.POST.get('cadena')
    resultado = Blog.buscar(query)
    return render(request, 'blog/resultado.html', {'resultados': resultado})
            


