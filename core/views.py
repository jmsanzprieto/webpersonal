from django.shortcuts import render, HttpResponse

# Importamos los metodos que sean necesarios

# Create your views here.


# Vista página principal
def home(request):
    return render(request, "core/home.html")

# Vista pagina about
def about(request):
    return HttpResponse("<h2>Sobre mi</h2>")

# Vista pagina contacto
def contacto(request):
    return HttpResponse("<h2>contacto</h2>")

