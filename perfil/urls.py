from  django.urls import path
from . import views

app_name = 'perfil'

urlpatterns = [
    path('cadastro/',views.cadastro_usuario, name='cadastro'),  
    #path('login/',views.login, name='login'),

]
