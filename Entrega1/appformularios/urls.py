from django.urls import path
from appformularios.views import *

urlpatterns = [
    path('inicio/',inicio, name="entrega-inicio"),
    path('clientes/', clientes, name="entrega-clientes"),
    path('productos/', productos, name="entrega-productos"),
    path('sucursales/', sucursales, name="entrega-sucursales"),
    
]