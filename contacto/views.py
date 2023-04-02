from django.shortcuts import render,redirect
from django.urls import reverse
# Importamos la libreria para poder enviar correos
from django.core.mail import EmailMessage

# Importamos el formulario que hemos creado
from .forms import FormContacto

# Create your views here.


# Vista pagina contacto
def contacto(request):
  contacto = FormContacto() # Instanciamos el formulario y para enviarlo al template
  
  # Procesamos el formulario, solamente si se recibe un post
  if request.method == "POST":
    # Relleanmos la plantilla con los datos enviados
    contacto = FormContacto(data=request.POST)
    # Comprobamos si todos los datos están completados y son válidos
    if contacto.is_valid():
      nombre = request.POST.get('nombre','')
      email = request.POST.get('email','')
      mensaje = request.POST.get('mensaje','')
      # Si está todo OK, redireccionamos. Con el reverse('nombre) no tenemos que preocuparnos por la url
      # real, ya que estamos redirigiendo a path y enviamos el correo
      correo = EmailMessage(
        "Mensaje desde el formulario de contacto", # Asunto del correo
        "De {} <{}>\n\nEscribió:\n\n{}".format(nombre, email, mensaje), # Contenido del correo
        "no_contestar@inbox.mailtrap.io", # Remitente del correo
        ["contacto@josemanuelsanz.es"], # Lista de los destinatarios del correo
        reply_to = [email] 
      )
      # Probamos el envio del correo y sus opciones por si falla o está OK
      try:
        correo.send()
        return redirect(reverse('contacto')+"?OK")
      except:
        return redirect(reverse('contacto')+"?KO")
      

  return render(request, "contacto/contacto.html",{'contacto':contacto})
