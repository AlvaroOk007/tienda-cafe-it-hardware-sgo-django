"""
URL configuration for tiendaHardware project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from . import views
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.inicio,name='inicio'),
    path('', lambda request : redirect('inicio')), #Lambda es una funcion anonima que toma el request como argumento y redirecciona a inicio
    path('home/productos/', include('productos.urls')),
    path('home/marcas/', include('marcas.urls')),
    path('home/soporte/',include('soporte.urls'))
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
