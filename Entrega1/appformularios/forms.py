from django import forms

#Aqui creo los formularios a utilizar

class ClienteFormulario(forms.Form):
    nombre = forms.CharField()
    rfc = forms.CharField()
    email = forms.EmailField()
    sector = forms.CharField()

class ProductoFormulario(forms.Form):
    nombre = forms.CharField()
    descripcion = forms.CharField()
    unidad_de_medida = forms.CharField()
    familia = forms.CharField()

class SucursalFormulario(forms.Form):
    nombre = forms.CharField()
    direccion = forms.CharField()
    colonia = forms.CharField()
    estado = forms.CharField()
    pais = forms.CharField()
    codigo_postal = forms.IntegerField()