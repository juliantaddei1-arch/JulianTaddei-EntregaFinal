from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("registrarse", views.registro_view, name="registrarse"),
    path("perfil/", views.profile_view, name="perfil"),
]


