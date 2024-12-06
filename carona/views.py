from django.shortcuts import render

# Create your views here.

def carona(request):
    return render(request,'visualizar_carona.html')