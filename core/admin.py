from django.contrib import admin

# Register your models here.
#Importamos el modelo
from .models import Pagina

# Register your models here.
# Extendiendo las funcionalidades del admin
class PaginaAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_creacion', 'fecha_actualizacion')

admin.site.register(Pagina,PaginaAdmin)
