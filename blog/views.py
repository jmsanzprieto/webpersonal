from django.shortcuts import get_object_or_404,render

# Importamos el modelo para acceder a la bd
from .models import Blog

# Create your views here.

# Vista página principal
def home(request):
    # Llamamos a la lista de noticias
    noticias = Blog.objects.all()
    # Añadiendo un tercer parametro a render, añadimos la lista de campos que vamos a exportar al template (el contenido de las notiicas)
    return render(request, "blog/home.html", {'noticias':noticias})

# Vista de una noticia concreta
def noticia(request, noticia_id):
    # Obtener la noticia especifica usando el ID pasado en la URL
    noticia = get_object_or_404(Blog, id=noticia_id)
    # Pasar la noticia al contexto de la plantilla usando la clave 'noticia'
    return render(request, 'blog/noticia.html', {'noticia': noticia})