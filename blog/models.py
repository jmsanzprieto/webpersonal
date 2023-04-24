from django.db import models
from django.db.models import Q
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User



# Create your models here.


# Control de los autores de las noticias
class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    biografia = models.TextField()
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nombre
    
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, default=0)

    # Algunas definiciones extra
    def save(self, *args, **kwargs):
        self.slug = slugify(self.nombre)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nombre
    
    def get_noticias(self):
        return self.categorias.all()


# Creamos la clase con la definición de los campos
class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=250)
    slug = models.SlugField(unique=True, default=0)
    subtitulo = models.CharField(max_length=250)
    contenido = RichTextField()
    imagen = models.ImageField(upload_to='blog')
    fecha_creacion = models.DateTimeField(auto_now_add=True) # Se añade la hora de forma automática cuando se crea el registro
    fecha_actualizacion = models.DateTimeField(auto_now=True) # Se añade la hora de forma automática al actualizarse el campo
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='blogs')
    num_visitas = models.PositiveIntegerField(default=0) # Nuevo campo para contabilizar el número de visitas
    categorias = models.ManyToManyField(Categoria, related_name=_('categorias'))
  
    
    # Algunas definiciones extra
    def save(self, *args, **kwargs):
        self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)

       
    class Meta:
        verbose_name = "noticia"
        verbose_name_plural = "noticias"
        ordering = ["-fecha_creacion"] # Ordena por defecto de mas antiguo a mas nuevo, con (-NombreCampo), cambia a la inversa
    
    def aumentar_visitas(self):
        self.num_visitas += 1
        self.save(update_fields=['num_visitas'])
    
    def __str__(self):
        num_comentarios = self.comentarios.count()
        return f'{self.titulo} ({self.fecha_creacion}) - {num_comentarios} comentarios'
    
    @staticmethod
    def buscar(query):
        if query is not None:
            return Blog.objects.filter(
            Q(titulo__icontains=query) | Q(subtitulo__icontains=query) | Q(contenido__icontains=query)
        )
        else:
            return Blog.objects.none()



# Gestion de comentarios
class Comentario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    contenido = RichTextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    aprobado = models.BooleanField(default=False)
    blog = models.ManyToManyField(Blog, related_name='comentarios')
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    avatar = models.ImageField(upload_to='avatar', null=True, blank=True)
    
    
    class Meta:
        ordering = ["fecha_creacion"]
        
def __str__(self):
    blog_titulos = ', '.join([blog.titulo for blog in self.comentarios.all()])
    return f'Comentario de {self.nombre} en {blog_titulos}'








