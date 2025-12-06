from django.shortcuts import render, redirect
from django.http import HttpResponse
from Inicio.models import Pelicula
from .forms import BusquedaPeliculaForm
from Inicio.forms import CrearPelicula
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import UpdateView, DeleteView
from django.shortcuts import render, redirect
from .models import Pelicula, ImagenPelicula
from .forms import CrearPelicula, ImagenesPeliculaForm

def actualizar_pelicula(request, id):
    pelicula = Pelicula.objects.get(id=id)

    if request.method == "POST":
        form_pelicula = CrearPelicula(request.POST, instance=pelicula)
        form_imagenes = ImagenesPeliculaForm(request.POST, request.FILES)

        if form_pelicula.is_valid() and form_imagenes.is_valid():
            pelicula_actualizada = form_pelicula.save()

            # Guardar imágenes nuevas (si se subieron)
            nuevas_imagenes = request.FILES.getlist("imagenes")
            for img in nuevas_imagenes:
                ImagenPelicula.objects.create(
                    pelicula=pelicula_actualizada,
                    imagen=img
                )

            return redirect("listar_peliculas")

    else:
        form_pelicula = CrearPelicula(instance=pelicula)
        form_imagenes = ImagenesPeliculaForm()

    return render(
        request,
        "Inicio/actualizar_pelicula.html",
        {
            "form_pelicula": form_pelicula,
            "form_imagenes": form_imagenes,
            "pelicula": pelicula,
        }
    )
def crear_pelicula(request):
    if request.method == "POST":
        form_pelicula = CrearPelicula(request.POST)
        form_imagenes = ImagenesPeliculaForm(request.POST, request.FILES)

        if form_pelicula.is_valid() and form_imagenes.is_valid():
            pelicula = form_pelicula.save()

            # Guardar varias imágenes
            imagenes = request.FILES.getlist("imagenes")
            for img in imagenes:
                ImagenPelicula.objects.create(pelicula=pelicula, imagen=img)

            return redirect("listar_peliculas")

    else:
        form_pelicula = CrearPelicula()
        form_imagenes = ImagenesPeliculaForm()

    return render(request, "Inicio/crear_pelicula.html", {
        "form_pelicula": form_pelicula,
        "form_imagenes": form_imagenes
    })


def listar_peliculas(request):
    peliculas = Pelicula.objects.all()
    return render(request, "Inicio/listar_peliculas.html", {"peliculas": peliculas})

def nueva(request):
    return render(request, "Inicio/nueva.html")


def inicio(request):
    return render(request, "Inicio/inicio.html")


def ver_pelicula(request, id):
    pelicula = get_object_or_404(Pelicula, id=id)
    return render(request, 'Inicio/ver_pelicula.html', {'pelicula': pelicula})


def eliminar_pelicula(request, id):
    pelicula = get_object_or_404(Pelicula, id=id)
    pelicula.delete()
    return redirect("listar_peliculas")
