from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.hashers import make_password,check_password
from .forms import UsuarioForm,EdicaoUsuarioForm
from models.Usuario import Usuario
from django.contrib import messages

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
        return redirect('login')  # Redireciona para a tela de login se não estiver logado

    # Busca o usuário no banco de dados
    usuario = get_object_or_404(Usuario, id=usuario_id)

    return render(request, 'visualizar_info.html', {'usuario': usuario})

def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        senha = request.POST.get('password')

        try:
            # Busca o usuário pelo email
            usuario = Usuario.objects.get(email=email)

            # Verifica se a senha corresponde
            if check_password(senha, usuario.senha):
                # Salva informações na sessão para autenticar o usuário
                request.session['usuario_id'] = usuario.id
                request.session['nome_completo']= usuario.nome_completo
                request.session['email']= usuario.email
                request.session['tipo_usuario']= usuario.tipo_usuario
                
                return redirect("perfil:visualizar_info")
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
