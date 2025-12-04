from django.shortcuts import render, redirect
from django.http import HttpResponse
from Inicio.models import Pelicula
from .forms import BusquedaPeliculaForm
from Inicio.forms import CrearPelicula
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import UpdateView, DeleteView

def actualizar_pelicula(request, id):
    pelicula = get_object_or_404(Pelicula, id=id)

    if request.method == "POST":
        formulario = CrearPelicula(request.POST, request.FILES, instance=pelicula)

        if formulario.is_valid():
            formulario.save()
            return redirect("listado")

    else:
        formulario = CrearPelicula(instance=pelicula)

    return render(request, "Inicio/actualizar_pelicula.html", {"formulario": formulario})


from django.shortcuts import render
from .forms import CrearPelicula
from .models import Pelicula

def crear_pelicula(request):
    if request.method == "POST":
        form = CrearPelicula(request.POST, request.FILES)
        if form.is_valid():
            pelicula_guardada = form.save()
            return render(request, "Inicio/crear_pelicula.html", {"form": CrearPelicula(), "pelicula_guardada": pelicula_guardada})
    else:
        form = CrearPelicula()

    return render(request, "Inicio/crear_pelicula.html", {"form": form})


def listar_peliculas(request):

    formulario = BusquedaPeliculaForm(request.GET or None)

    if formulario.is_valid():
        pelicula= formulario.cleaned_data.get("pelicula")
        if pelicula:
            peliculas = Pelicula.objects.filter(pelicula__icontains=pelicula)
        else:
            peliculas = Pelicula.objects.all()
    else:
        peliculas = Pelicula.objects.all()

    return render(
        request,
        "Inicio/listar_peliculas.html",
        {
            "formulario": formulario,   "listado_de_peliculas": peliculas}
    )



def nueva(request):
    return render(request, "Inicio/nueva.html")



def inicio(request):
    return render(request, "Inicio/inicio.html")

from django.shortcuts import render, get_object_or_404
from .models import Pelicula

def ver_pelicula(request, id):
    pelicula = get_object_or_404(Pelicula, id=id)
    return render(request, 'Inicio/ver_pelicula.html', {'pelicula': pelicula})



def eliminar_pelicula(request, id):
    pelicula = get_object_or_404(Pelicula, id=id)
    pelicula.delete()
    return redirect('listar_peliculas')