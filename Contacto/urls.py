from django.urls import path
from . import views as v
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [ 
    path('', v.contacto),
]

