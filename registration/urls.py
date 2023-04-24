from django.urls import path
from .views import RegistroView,PerfilUpdate

urlpatterns = [
    path('registro/', RegistroView.as_view(), name="registro"),
    path('perfil/', PerfilUpdate.as_view(), name="perfil"),
]