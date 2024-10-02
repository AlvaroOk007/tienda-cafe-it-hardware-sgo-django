from django.shortcuts import render, HttpResponse
from .models import Producto,Categoria,Marca
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
# Create your views here.
def productos(request):
    productos = Producto.objects.all()
    categorias = Categoria.objects.all()
    marcas = Marca.objects.all()
    if productos:
        return render(request, 'productos/productos.html',{'productos':productos,
                                                           'categorias':categorias,
                                                           'marcas' : marcas
                                                           })
    else:
        return HttpResponse("No se encontraron Resultados")

@csrf_exempt # Exime la vista del control CSRF (solo para pruebas, en producción usa el token CSRF)
def aplicarFiltros(request):
    if request.method == 'POST':
        marca = request.POST.get('marca')
        categoria = request.POST.get('categoria')
        productos = Producto.objects.all()
        if categoria != "Filtrar por Categoria":
            productos = productos.filter(categoria__nombre__contains=categoria)          
        if marca != "Filtrar por Marca":
            print("Pasé por aqui")
            productos = productos.filter(marca__nombre__contains=marca)
        for producto in productos:
                print(producto.nombre)
        productos_json = list(productos.values())  # Convertir a lista de diccionarios para JSON
        return JsonResponse(productos_json, safe=False)
