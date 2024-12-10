from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, get_object_or_404, redirect
from models.Carona import Carona  # Ajuste o caminho para o modelo
from .forms import CaronaForm
from models.carona_factory import CaronaFactory

# CREATE
def criar_carona(request):
    if request.method == 'POST':
        form = CaronaForm(request.POST)
        if form.is_valid():
            carona_data = form.cleaned_data  # Dados validados do formulário
            # Usando a Factory para criar a instância
            nova_carona = CaronaFactory.criar_carona(
                nome=carona_data['nome'],
                horario=carona_data['horario'],
                data=carona_data['data'],
                descricao=carona_data.get('descricao'),
                motorista=carona_data['motorista'],
                endereco_saida=carona_data['endereco_saida'],
                endereco_destino=carona_data['endereco_destino'],
                status=carona_data.get('status', 'A')
            )
            nova_carona.save()  # Salva a carona no banco
            return redirect('carona:listar_caronas')  # Redireciona após a criação
    else:
        form = CaronaForm()
    return render(request, 'criar_carona.html', {'form': form})

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

def entrar_carona(request, id):
    print(f"carona {id}")
