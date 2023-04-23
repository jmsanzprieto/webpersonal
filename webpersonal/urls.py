"""webpersonal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from core import views as core_views
from blog import views as blog_views
from core.views import pagina
from blog.views import noticia
from blog.views import categoria
from blog.views import agregar_comentario
from blog.views import buscar_noticias
from core import views
# Para poder ver todas las opciones en desarrollo, debemos hacer algunas importaciones
from django.conf import settings
from django.conf.urls.static import static
from blog.views import Categoria
from django.views import i18n

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',blog_views.home, name="home"),
    # Mostramos una noticia concreta
    path('blog/<slug:slug>/', noticia.as_view(), name='noticia'),
    # Mostramos una noticia concreta
    # Mostramos una pagina concreta
    path('pagina/<slug:slug>/', pagina.as_view(), name='pagina-detalle'),
    # Mostramos una pagina concreta
    # Mostramos una categoria concreta
    path('categoria/<slug:slug>/', categoria.as_view(), name='categoria_detail'),
    # Mostramos una categoria concreta
    path('contacto', include('contacto.urls')),   
    # otras URLs existentes...
    path('procesar-comentario/', blog_views.agregar_comentario, name='procesar_comentario'),
    path('buscar-noticia/', blog_views.buscar_noticias, name='buscar_noticias'),
    path('change_language/<str:language>/', views.change_language, name='change_language'),
    # Path del Auth
    path('accounts/', include('django.contrib.auth.urls')),
    # Cambiamos el path para que el login esté en el modal del home
    path('login/', auth_views.LoginView.as_view(template_name='base.html'), name='login'),

]




# Comprueba de DEBUG esta como True
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)