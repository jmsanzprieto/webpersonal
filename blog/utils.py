# en app/utils.py
from .models import Blog
from .models import Categoria


def mas_leidas():
    return Blog.objects.all().order_by('-num_visitas')[:3]

def lista_categorias():
   return Categoria.objects.all()


  
