from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(
        max_length=256,
        blank=True,
        null=True
    )
    def __str__(self):
        return self.name
class Product(models.Model):
    name = models.CharField(max_length=128)
    price = models.DecimalField(
        max_digits=28,
        decimal_places=2
    )
    description = models.TextField(max_length=256)
    quantity = models.IntegerField(
        default=0
    )
    img = models.ImageField(upload_to='products_images')
    category = models.ForeignKey(
        to='ProductCategory',
        on_delete=models.CASCADE)
    def __str__(self):
        return self.name


