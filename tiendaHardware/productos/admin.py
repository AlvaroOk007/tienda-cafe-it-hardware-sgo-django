from django.contrib import admin
from .models import Producto,Categoria,Marca

admin.site.register([Producto,Categoria,Marca])
# Register your models here.
