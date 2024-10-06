from django.shortcuts import render, HttpResponse,redirect
from django.urls import reverse
from django.utils.text import slugify
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
            productos = productos.filter(marca__nombre__contains=marca)
        productos_json = list(productos.values())  # Convertir a lista de diccionarios para JSON
        return JsonResponse(productos_json, safe=False)


@csrf_exempt
def producto(request,id,nombre):
    try:
        producto = Producto.objects.get(id = id)#Retorna el elemento si existe, y sino devuelve una excepcion DoesNotExist
        productosRelacionados = Producto.objects.filter(categoria = producto.categoria)
        if (producto.nombre != nombre):
            return redirect(reverse('producto_detalle',kwargs={'id': id, 'nombre': producto.nombre}))
        return render(request,'productos/producto.html', {'producto':producto , "productos" : productosRelacionados})
    except Producto.DoesNotExist:
        return redirect('productos')
    
