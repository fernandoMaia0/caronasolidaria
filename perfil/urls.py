from  django.urls import path
from . import views

app_name = 'perfil'

urlpatterns = [
    path('cadastro/',views.cadastro_usuario, name='cadastro'),  
    path('',views.login, name='login'),
    path('excluir/',views.excluir_conta,name='excluir'),
    path('visualiza_info/',views.visualizar_info, name='visualiza_info'),
    path('edicao/', views.edicao,name='edicao'),
    path('logout/',views.logoutuser,name='logoutuser'),


]
