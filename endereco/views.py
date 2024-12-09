from django.shortcuts import render,redirect,get_object_or_404
from .forms import  enderecoForm
from models.Endereco import Endereco

# Create your views here.
def criar_endereco(request):
    if request.method == 'POST':
        form = enderecoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('carona:listar_caronas')
    else:
        form = enderecoForm()
    return render(request, 'criar_carona.html', {'form': form})

def editar_endereco(request,id):
    endereco= get_object_or_404(Endereco,id=id)
    if request.method =='POST':
        form=enderecoForm(request.POST, instance=endereco)
        if form.is_valid():
            form.save()
        return redirect('listar_enderecos')
    else:
        form = enderecoForm(instance=endereco)
        return render(request,'endereco:editar_endereco',{'endereco': endereco})