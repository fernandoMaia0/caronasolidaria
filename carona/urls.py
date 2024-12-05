from  django.urls import path
from . import views

app_name = 'carona'

urlpatterns = [
    path('',views.carona, name='carona'),    
]
