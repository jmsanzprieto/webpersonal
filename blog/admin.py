from django.contrib import admin

#Importamos el modelo
from .models import Blog
from .models import Comentario
from .models import Autor

# Register your models here.
# Extendiendo las funcionalidades del admin

# Añadimos al admin la gestión de las noticias
class BlogAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_creacion', 'fecha_actualizacion')

admin.site.register(Blog,BlogAdmin)

# Añadimos al admin la gestión de los comentarios
class ComentarioAdmin(admin.ModelAdmin):
  list_display = ('nombre', 'email', 'contenido', 'fecha_creacion', 'aprobado')
  list_filter = ('aprobado', 'fecha_creacion')
  search_fields = ('nombre', 'email', 'contenido')
  actions = ['aprobar_comentarios', 'desaprobar_comentarios']
  
  def aprobar_comentarios(self, request, queryset):
    queryset.update(aprobado=True)
    
  aprobar_comentarios.short_description = "Aprobar comentarios seleccionados"
  
  def desaprobar_comentarios(self, request, queryset):
    queryset.update(aprobado=False)
    
  desaprobar_comentarios.short_description = "Desaprobar comentarios seleccionados"

admin.site.register(Comentario, ComentarioAdmin)


# Añadimos al admin la gestión de los usuarios
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'biografia')  # Campos a mostrar en la lista de objetos de Autor
    verbose_name_plural = 'Autores'


admin.site.register(Autor, AutorAdmin)  # Registra la clase Autor en el panel de administración y le aplica la personalización de AutorAdmin
