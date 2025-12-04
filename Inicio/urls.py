from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path, include




urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nueva/', views.nueva, name='nueva'),
    path('crear_pelicula/', views.crear_pelicula, name='crear'),
    path('listar_peliculas/', views.listar_peliculas, name='listado'),
    path('pelicula/<int:id>/', views.ver_pelicula, name='ver'),
    path('actualizar/<int:id>/', views.actualizar_pelicula, name='actualizar'), 
    path('eliminar/<int:id>/', views.eliminar_pelicula, name='eliminar'),
    path("usuarios/", include("usuarios.urls")),


    
]