from django.contrib import admin

#Importamos el modelo
from .models import Blog

# Register your models here.
# Extendiendo las funcionalidades del admin
class BlogAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_creacion', 'fecha_actualizacion')

admin.site.register(Blog,BlogAdmin)
