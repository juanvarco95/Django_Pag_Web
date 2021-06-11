from django.shortcuts import render, HttpResponse
from django.conf import settings
from django.core.mail import send_mail



def home(request):

    return render(request, 'gestionProyecto/home.html')

def base(request):

    return render(request, 'gestionProyecto/base.html')


def blog(request):

    return render(request, 'gestionProyecto/blog.html')

def tienda(request):

    return render(request, 'gestionProyecto/tienda.html')

def buscar(request):
    if request.GET["pro"]:
        producto =  request.GET["pro"]
        if len (producto) > 20:
            mensaje = "Texto de busqueda demasiado largo"
        




