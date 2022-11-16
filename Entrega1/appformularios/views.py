from django.shortcuts import render
from django.http import HttpResponse
from appformularios.models import *


# Create your views here.
def inicio(request):
    return render(request, "appformularios/index.html")

def clientes(request):
    return render(request, "appformularios/clientes.html")

def productos(request):
    return render(request, "appformularios/productos.html")

def sucursales(request):
    return render(request, "appformularios/sucursales.html")
