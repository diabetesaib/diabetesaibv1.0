#Se importa varias librerias para el formulario
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import formulario_contacto
from django.core.mail import EmailMessage

#Definimos el formulario
def formulario (request):
    formulario1= formulario_contacto()
    #Se debe de dar la condiciónd e que el formulario esté en modo post que significa que está enviando datos
    #la otra manera es get, que permite obtener un valor
    if request.method == "POST":
        formulario1=formulario_contacto(data=request.POST)
        #Si el formulario es válido se cogerán (GET) esos valores y se enviará un correo (configuramos su aspecto)
        if formulario1.is_valid():
            usuario=request.POST.get('usuario','')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            email= EmailMessage(
                "Duda enviada a Diabetes AIB",
                "De: {} con correo: {} \n \n escribió: {}".format(usuario,email,content),
                "no-contestar@diabetesaib.com",
                ["adrianidoate@diabetesaib.com"],
                reply_to=[email]

            )
            #Se prueba a enviar al correo programado en settigns.py
            try:
                email.send()
                return redirect(reverse('formulario')+"?ok")
            # Si no envía una excepción
            except:
                return redirect(reverse('formulario') + "?fail")

    #Envía estos datos al html con su diccionario correspondiente
    return render(request, 'formulario.html', {'form':formulario1})
