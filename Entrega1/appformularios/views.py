from django.shortcuts import render
from django.http import HttpResponse
from appformularios.models import *
from appformularios.forms import *

# Create your views here.
def inicio(request):
    return render(request, "appformularios/index.html")

#Aqui van las funciones para los clientes
def creacion_cliente(request):

    if request.method == "POST":
        formulario = ClienteFormulario(request.POST)

        if formulario.is_valid():
            #Recuperamos los datos del atributo cleaned_data
            data = formulario.cleaned_data

            cliente = Cliente(nombre=data["nombre"], rfc=data["rfc"], email=data["email"], sector=data["sector"])

            cliente.save()

    formulario = ClienteFormulario()

    contexto = {"formulario": formulario}

    return render(request, "appformularios/clientes_formulario.html", contexto)

def buscar_cliente(request):
    
    return render(request, "appformularios/busqueda_clientes.html")


def resultado_busqueda_clientes(request):
    nombre_cliente = request.GET["nombre_cliente"]

    clientes = Cliente.objects.filter(nombre__icontains=nombre_cliente)
    return render(request, "appformularios/resultados_busqueda_clientes.html",{"clientes":clientes})


#Aqui van las funciones para los productos

def creacion_producto(request):

    if request.method == "POST":
        formulario = ProductoFormulario(request.POST)

        if formulario.is_valid():
            #Recuperamos los datos del atributo cleaned_data
            data = formulario.cleaned_data

            producto = Producto(nombre=data["nombre"], descripcion=data["descripcion"], unidad_de_medida=data["unidad_de_medida"], familia=data["familia"])

            producto.save()

    formulario = ProductoFormulario()

    contexto = {"formulario": formulario}

    return render(request, "appformularios/productos_formulario.html", contexto)

def buscar_producto(request):
    
    return render(request, "appformularios/busqueda_productos.html")


def resultado_busqueda_productos(request):
    nombre_producto = request.GET["nombre_producto"]

    productos = Producto.objects.filter(nombre__icontains=nombre_producto)
    return render(request, "appformularios/resultados_busqueda_productos.html",{"productos":productos})



#Aqui van las funciones para las sucursales
def creacion_sucursal(request):

    if request.method == "POST":
        formulario = SucursalFormulario(request.POST)

        if formulario.is_valid():
            #Recuperamos los datos del atributo cleaned_data
            data = formulario.cleaned_data

            sucursal = Sucursal(nombre=data["nombre"], direccion=data["direccion"], colonia=data["colonia"], estado=data["estado"], pais=data["pais"], codigo_postal=data["codigo_postal"])

            sucursal.save()

    formulario = SucursalFormulario()

    contexto = {"formulario": formulario}

    return render(request, "appformularios/sucursales_formulario.html", contexto)


def buscar_sucursal(request):
    
    return render(request, "appformularios/busqueda_sucursales.html")


def resultado_busqueda_sucursales(request):
    nombre_sucursal = request.GET["nombre_sucursal"]

    sucursales = Sucursal.objects.filter(nombre__icontains=nombre_sucursal)
    return render(request, "appformularios/resultados_busqueda_sucursales.html",{"sucursales":sucursales})


