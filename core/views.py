from django.shortcuts import render, HttpResponse

# Importamos el modelo para acceder a la bd
# Create your views here.


# Vista pagina about
def about(request):
    return render(request, "core/about.html")
