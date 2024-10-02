from django.urls import path
from . import views


urlpatterns=[
    path('', views.productos, name='productos'),
    path('api/aplicarFiltros/', views.aplicarFiltros, name= 'aplicarFiltros')
]

