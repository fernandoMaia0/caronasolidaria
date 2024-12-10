from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.hashers import make_password,check_password
from .forms import UsuarioForm,EdicaoUsuarioForm
from models.Usuario import Usuario
from django.contrib import messages
from django.contrib.auth import logout
from perfil.auth_manager import AuthManager


# Create your views here.

def cadastro_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.senha = make_password(form.cleaned_data["senha"])
            usuario.save()
            return redirect('perfil:login')  
    else:
        form = UsuarioForm()
    
    return render(request, 'cadastro.html', {'form': form})

def excluir_conta(request):
    if request.method == 'POST':
        usuario_id = request.session.get('usuario_id')
        if usuario_id:
            usuario = get_object_or_404(Usuario, id=usuario_id)
            usuario.delete()
            # Limpa a sessão após exclusão
            request.session.flush()
            messages.success(request, "Sua conta foi excluída com sucesso.")
            return redirect('home:index')  # Redirecione para a página inicial ou de logout
    messages.error(request, "Erro ao excluir a conta. Tente novamente.")
    return redirect('perfil:visualizar_info')  # Se não for POST, redirecione de volta

def visualizar_info(request):
    # Recupera o ID do usuário logado
    usuario_id = request.session.get('usuario_id')
    if not usuario_id:
        return redirect('perfil:login')  # Redireciona para a tela de login se não estiver logado

    # Busca o usuário no banco de dados
    usuario = get_object_or_404(Usuario, id=usuario_id)

    return render(request, 'visualizar_info.html', {'usuario': usuario})

def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        senha = request.POST.get('password')

        try:
            usuario = Usuario.objects.get(email=email)
            if check_password(senha, usuario.senha):
                # Usa o Singleton para autenticar e salvar as informações do usuário
                auth_manager = AuthManager()
                auth_manager.login(request, usuario)

                return redirect("home:index")
            else:
                return render(request, 'login.html', {'error': 'Senha incorreta'})
        except Usuario.DoesNotExist:
            return render(request, 'login.html', {'error': 'Usuário não encontrado'})
    return render(request, 'login.html')

def edicao(request):
   
    usuario_id = request.session.get('usuario_id')
    
    if not usuario_id:
        return redirect('perfil:login')

    usuario = get_object_or_404(Usuario, id=usuario_id)

    if request.method == 'POST':
        form = EdicaoUsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            usuario = form.save(commit=False)
            nova_senha = form.cleaned_data.get('senha')
            if nova_senha:
                usuario.senha = make_password(nova_senha)
                usuario.save()
            return redirect('home:index')
    else:
        form = EdicaoUsuarioForm(instance=usuario)

    # Renderizar o template
    return render(request, 'edicao.html', {'form': form})

def logoutuser(request):
    # Usa o Singleton para limpar o estado de autenticação
    auth_manager = AuthManager()
    auth_manager.logout(request)

    return redirect('home:index')

def landing_page(request):
    # Obtém informações do usuário autenticado via Singleton
    auth_manager = AuthManager()
    usuario_info = auth_manager.get_user_info(request)

    # Envia as informações para o template
    return render(request, 'landing_page.html', {'usuario': usuario_info})