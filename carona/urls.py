from  django.urls import path
from . import views

app_name = 'carona'

urlpatterns = [
    path('criar/', views.criar_carona, name='criar_carona'),
    path('editar/', views.editar_carona, name='editar_carona'),
    path('excluir/', views.excluir_carona, name='excluir_carona'),
    path('entrar/<int:id>/', views.entrar_carona, name='entrar_carona'),
]
