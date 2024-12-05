from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('perfil/', include('perfil.urls')),
    path('carona/', include('carona.urls')),
]
