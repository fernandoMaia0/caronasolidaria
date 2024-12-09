from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, get_object_or_404, redirect
from models.Carona import Carona  # Ajuste o caminho para o modelo
from .forms import CaronaForm

# CREATE
def criar_carona(request):
    if request.method == 'POST':
        form = CaronaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('carona:listar_caronas')
    else:
        form = CaronaForm()
    return render(request, 'criar_carona.html', {'form': form})

# READ (Listar Caronas)
def listar_caronas(request):
    caronas = Carona.objects.all()
    return render(request, 'listar_caronas.html', {'caronas': caronas})

# UPDATE
def editar_carona(request, id):
    carona = get_object_or_404(Carona, id=id)
    if request.method == 'POST':
        form = CaronaForm(request.POST, instance=carona)
        if form.is_valid():
            form.save()
            return redirect('listar_caronas')
    else:
        form = CaronaForm(instance=carona)
    return render(request, 'carona:editar_carona.html', {'form': form})

# DELETE
def excluir_carona(request, id):
    carona = get_object_or_404(Carona, id=id)
    if request.method == 'POST':
        carona.delete()
        return redirect('listar_caronas')
    return render(request, 'carona:excluir_carona.html', {'carona': carona})

