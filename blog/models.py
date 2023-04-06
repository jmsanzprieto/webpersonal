from django.db import models
from django.utils.text import slugify


# Create your models here.

# Creamos la clase con la definición de los campos
class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=250)
    slug = models.SlugField(unique=True, default=0)
    subtitulo = models.CharField(max_length=250)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to='blog')
    fecha_creacion = models.DateTimeField(auto_now_add=True) # Se añade la hora de forma automática cuando se crea el registro
    fecha_actualizacion = models.DateTimeField(auto_now=True) # Se añade la hora de forma automática al actualizarse el campo

    # Algunas definiciones extra
    def save(self, *args, **kwargs):
        self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)
        
    class Meta:
        verbose_name = "noticia"
        verbose_name_plural = "noticias"
        ordering = ["-fecha_creacion"] # Ordena por defecto de mas antiguo a mas nuevo, con (-NombreCampo), cambia a la inversa
    
    def __str__(self):
        num_comentarios = self.comentarios.count()
        return f'{self.titulo} ({self.fecha_creacion}) - {num_comentarios} comentarios'




    

# Gestion de comentarios
class Comentario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    aprobado = models.BooleanField(default=False)
    blog = models.ManyToManyField(Blog, related_name='comentarios')
    
    class Meta:
        ordering = ["fecha_creacion"]
        
def __str__(self):
    blog_titulos = ', '.join([blog.titulo for blog in self.comentarios.all()])
    return f'Comentario de {self.nombre} en {blog_titulos}'
