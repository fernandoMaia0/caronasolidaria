from django.shortcuts import render
from models.Carona import Carona
from models.Usuario import Usuario

# Create your views here.

def index(request):
    
    caronas = Carona.objects.prefetch_related('passageiros').all()       
    context = {
        'caronas': caronas,
    }
    return render(request, 'landing-page.html', context)

