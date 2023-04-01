from django.apps import AppConfig


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
    # Opciones extendidas
    # Hay que reflejar los cambios de este fichero en settings.py en INSTALLED_APPS
    # Nombre de la aplicación personalizado
    verbose_name = "Noticias"
