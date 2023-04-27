from django.contrib import admin
from .models import Secreto


# Register your models here.
@admin.register(Secreto)
class SecretoAdmin(admin.ModelAdmin):
    list_display = ('hash', 'mensaje','fecha_creacion')


