from django.db import models

# Create your models here.

class Products(models.Model):
    title = models.CharField(max_length=120, verbose_name="Ürün Adı")
    image = models.ImageField(null=True, blank=True)
    brand = models.CharField(max_length = 120,verbose_name = "Marka")
    price = models.IntegerField(verbose_name = "Fiyat")
    countInStock = models.IntegerField(verbose_name = "Stok Adet")


    def __str__(self):
        return self.title