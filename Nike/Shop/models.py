from django.db import models


class Clothes(models.Model):
    name = models.CharField(max_length = 100, verbose_name = 'Nombre')
    type = models.CharField(max_length = 100, verbose_name = 'Tipo')
    price = models.FloatField(verbose_name = 'Precio')
    stock = models.BooleanField(default=True ,verbose_name = 'En stock')
    product_image = models.ImageField(upload_to='product_images', null=True, blank=True, verbose_name= 'Imagen')
    size = models.CharField(max_length = 10, verbose_name = 'tamaño')

    def __str__(self):
        return self.name

