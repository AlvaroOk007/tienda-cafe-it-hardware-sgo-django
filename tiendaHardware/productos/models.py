from django.db import models
from django.utils.html import format_html
# Create your models here.
class Marca(models.Model):
    nombre = models.CharField(max_length=50,default="Sin especificar")
    logo = models.ImageField(upload_to='marcas/',default="Sin logo")
    def __str__(self) -> str:
        return self.nombre
class Categoria(models.Model):
    nombre = models.CharField(max_length=50,null=False)
    def __str__(self) -> str:
        return self.nombre
class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.FloatField(default=0)
    descripcion = models.CharField(max_length=255)
    imagen = models.ImageField(upload_to='productos/',null=True)
    stock = models.IntegerField(default=10)
    #Claves foraneas
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE,default=1)
    marca = models.ForeignKey(Marca,on_delete=models.CASCADE,default=1)


    def __str__(self) -> str:
        return self.nombre
    def haySrock(self):
        return self.stock>0
    def mostrarImagen(self):
        if self.imagen:
            return format_html('<img src = {} width= "100" heigth  = "100" />'.format(self.imagen.url))
        else:
            return ''