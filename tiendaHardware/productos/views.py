from django.shortcuts import render, HttpResponse
from .models import Producto,Categoria
# Create your views here.
def productos(request):
    productos = Producto.objects.all()
    categorias = Categoria.objects.all()
    if productos:
        return render(request, 'productos/productos.html',{'productos':productos,'categorias':categorias})
    else:
        return HttpResponse("No se encontraron Resultados")