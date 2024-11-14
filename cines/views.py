from django.shortcuts import render, get_object_or_404, redirect
from .models import Pelicula
from django.contrib.auth.decorators import login_required
from .forms import PeliculaForm

# Página principal para agregar películas
@login_required
def registrar_pelicula(request):
    if request.method == 'POST':
        form = PeliculaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('cines:lista_peliculas')  # Redirige a la lista de películas
    else:
        form = PeliculaForm()
    return render(request, 'cine.html', {'form': form})

# Vista para editar una película
@login_required
def editar_pelicula(request, pelicula_id):
    pelicula = get_object_or_404(Pelicula, id=pelicula_id)
    if request.method == 'POST':
        form = PeliculaForm(request.POST, request.FILES, instance=pelicula)
        if form.is_valid():
            form.save()
            return redirect('cines:lista_peliculas')  # Redirige a la lista de películas después de editar
    else:
        form = PeliculaForm(instance=pelicula)
    return render(request, 'editar_pelicula.html', {'form': form, 'pelicula': pelicula})

# Vista para eliminar una película
@login_required
def eliminar_pelicula(request, pelicula_id):
    pelicula = get_object_or_404(Pelicula, id=pelicula_id)
    if request.method == 'POST':
        pelicula.delete()
        return redirect('cines:lista_peliculas')  # Redirige a la lista de películas después de eliminar
    return render(request, 'eliminar_pelicula.html', {'pelicula': pelicula})

# Vista para listar las películas
@login_required
def lista_peliculas(request):
    peliculas = Pelicula.objects.all()  # Obtén todas las películas de la base de datos
    return render(request, 'peliculas.html', {'peliculas': peliculas})
