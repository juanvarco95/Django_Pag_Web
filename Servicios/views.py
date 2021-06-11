from django.shortcuts import render
from Servicios.models import Servicio

# Create your views here.
def servicios(request):
    ser = Servicio.objects.all()
    ctx = {"servicios": ser}
    
    return render(request, 'Servicios/servicios.html', ctx)