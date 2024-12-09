from  django.urls import path
from . import views

app_name = 'carona'

urlpatterns = [
   path('listar/', views.listar_caronas, name='listar_caronas'),
    path('criar/', views.criar_carona, name='criar_carona'),
    path('editar/', views.editar_carona, name='editar_carona'),
    path('excluir/', views.excluir_carona, name='excluir_carona'),
]
