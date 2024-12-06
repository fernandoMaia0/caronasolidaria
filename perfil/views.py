from django.shortcuts import render
from django.contrib.auth.hashers import make_password,check_password

# Create your views here.

from django.shortcuts import render, redirect
from .forms import UsuarioForm

def cadastro_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.senha = make_password(form.cleaned_data["senha"])
            usuario.save()
            return redirect('login')  # Substitua pelo nome da URL do login
    else:
        form = UsuarioForm()
    
    return render(request, 'cadastro.html', {'form': form})
