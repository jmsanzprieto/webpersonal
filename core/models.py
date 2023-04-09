from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

# Create your models here.
class Pagina(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=250)
    slug = models.SlugField(unique=True, default=0)
    subtitulo = models.CharField(max_length=250)
    contenido = RichTextField()
    imagen = models.ImageField(upload_to='paginas')
    fecha_creacion = models.DateTimeField(auto_now_add=True) # Se añade la hora de forma automática cuando se crea el registro
    fecha_actualizacion = models.DateTimeField(auto_now=True) # Se añade la hora de forma automática al actualizarse el campo

    # Algunas definiciones extra
    def save(self, *args, **kwargs):
        self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "pagina"
        verbose_name_plural = "paginas"
        ordering = ["-fecha_creacion"] # Ordena por defecto de mas antiguo a mas nuevo, con (-NombreCampo), cambia a la inversa

    # De esta forma, podemos visualizar el nombre de las paginas correctamente en el admin
    def __str__(self):
        return self.titulo