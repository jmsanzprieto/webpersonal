from django.shortcuts import get_object_or_404,render

# Importamos el modelo para acceder a la bd
from .models import Pagina



def pagina(request, pagina_id):
    # Obtener la noticia especifica usando el ID pasado en la URL
    pagina = get_object_or_404(Pagina, id=pagina_id)
    # Pasar la pagina al contexto de la plantilla usando la clave 'pagina'
    return render(request, 'paginas/pagina.html', {'pagina': pagina})
