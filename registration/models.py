from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="perfil", null=True, blank=True) # Es un campo optativo
    bio = models.TextField(null=True, blank=True) # Es un campo optativo
    link = models.URLField(max_length=200, null=True, blank=True) # Es un campo optativo