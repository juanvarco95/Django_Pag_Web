from django.shortcuts import render
from Contacto.forms import FormularioContacto
from django.conf import settings
from django.core.mail import send_mail


def contacto(request):
   
    if request.method == "POST":
        miForm = FormularioContacto(request.POST)

        if miForm.is_valid(): 
            infoForm = miForm.cleaned_data
            message = infoForm['mensaje'] + " " + infoForm['email']
            send_mail(infoForm['nombre'], message , infoForm.get('email', ''), ['juanvarco3d@gmail.com'],)

            return render(request, "Contacto/gracias.html")
    else:
        miForm = FormularioContacto() 
    ctx = {"form": miForm} 
    

    return render(request, "Contacto/contacto.html", ctx)
