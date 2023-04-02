from django.shortcuts import render, HttpResponse

# Importamos los metodos que sean necesarios

# Create your views here.




# Vista pagina about
def about(request):
    return render(request, "core/about.html")

# Vista pagina contacto
def contacto(request):
  return render(request, "core/contacto.html")
