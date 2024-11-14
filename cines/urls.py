"""
URL configuration for CinePredict project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from usuarios_cine.views import home, exit
from .views import registrar_pelicula, editar_pelicula, eliminar_pelicula, lista_peliculas

app_name = 'cines'  # Establece el namespace

urlpatterns = [
    path("", home, name='home'),
    path("registrar_pelicula/", registrar_pelicula, name='registrar_pelicula'),
    path("lista/", lista_peliculas, name='lista_peliculas'),
    path('editar/<int:pelicula_id>/', editar_pelicula, name='editar_pelicula'),
    path('eliminar/<int:pelicula_id>/', eliminar_pelicula, name='eliminar_pelicula'),
    path('logout/', exit, name='exit'),
]
