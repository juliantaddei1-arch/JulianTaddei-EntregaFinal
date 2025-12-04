from django.db import models

class Pelicula(models.Model):
    pelicula = models.CharField(max_length=100)
    genero = models.CharField(max_length=30)
    anio = models.CharField(max_length=4)
    imagen = models.ImageField(upload_to="peliculas", null=True, blank=True)
    imagen= models.ImageField(upload_to='fotos/', null=True, blank=True)


   
    def __str__(self):
        return f'Pelicula({self.id}): {self.pelicula} - {self.genero} - {self.anio} - {self.imagen}'    
    