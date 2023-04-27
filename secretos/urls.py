from django.urls import path
from .views import secretos, procesar_secretos, confirmacion, ver_secreto, enviar_email


urlpatterns = [
    path('', secretos, name='secretos'),
    path('procesar_secretos/', procesar_secretos, name='procesar_secretos'),
    path('confirmacion/<str:hash>/', confirmacion, name='confirmacion'),
    path('<str:hash>/', ver_secreto, name='ver_secreto'),
    path('enviar_email/', enviar_email, name='enviar_email'),    
    
    ]
