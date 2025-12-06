from django.db import models

from django.db import models

class Pelicula(models.Model):
    pelicula = models.CharField(max_length=100)
    genero = models.CharField(max_length=30)
    anio = models.CharField(max_length=4)
    imagen = models.ImageField(upload_to="peliculas/", null=True, blank=True)

    def __str__(self):
        return f'{self.pelicula} - {self.genero} - {self.anio}'


class ImagenPelicula(models.Model):
    pelicula = models.ForeignKey(Pelicula, related_name="imagenes", on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="imagenes_peliculas/")


    def __str__(self):
        return f"Imagen de {self.pelicula.pelicula}"
