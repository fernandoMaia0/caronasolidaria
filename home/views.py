from django.shortcuts import render
from models.Carona import Carona
from models.Usuario import Usuario
from perfil.auth_manager import AuthManager

# Create your views here.

def index(request):
    
    caronas = Carona.objects.prefetch_related('passageiros').all()       
    auth_manager = AuthManager()
    usuario_info = auth_manager.get_user_info(request)

   
    context = {
        'caronas': caronas,
        'usuario': usuario_info,  
    }
    return render(request, 'landing-page.html', context)



