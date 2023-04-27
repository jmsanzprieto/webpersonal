from django.db import models

# Create your models here.
class Secreto(models.Model):
    hash = models.CharField(max_length=250)
    mensaje = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.hash