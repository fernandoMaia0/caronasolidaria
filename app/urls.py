from django.contrib import admin
from django.urls import path
from app.views import cadastro_view  # Substitua pelo nome do seu app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', cadastro_view, name='home'),  # Define a página de cadastro como a URL raiz
]
