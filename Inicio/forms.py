from django import forms
from .models import Pelicula

class CrearPelicula(forms.ModelForm):
    class Meta:
        model = Pelicula
        fields = ("pelicula", "genero", "anio")


class ImagenesPeliculaForm(forms.Form):
    imagenes = forms.FileField(
        required=False,
        widget=forms.ClearableFileInput(),   # sin multiple
        label="Subir imágenes"
    )
class BusquedaPeliculaForm(forms.Form):
    pelicula = forms.CharField(required=False, label="Buscar película")
