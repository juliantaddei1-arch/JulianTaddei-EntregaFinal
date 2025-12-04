from django import forms
from .models import Pelicula

class CrearPelicula(forms.ModelForm):
    class Meta:
        model = Pelicula
        fields = ['pelicula', 'genero', 'anio', 'imagen']

#class CrearPelicula(forms.Form):
 #   pelicula = forms.CharField(max_length=100)
  #  genero = forms.CharField(max_length=30)
   # anio= forms.CharField(max_length=4)

class BusquedaPeliculaForm(forms.Form):
    pelicula =forms.CharField(max_length=30, required=False, label="pelicula") 
