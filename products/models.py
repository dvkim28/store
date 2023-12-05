from django.db import models
from users.models import User

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
    name = models.CharField(
        max_length=128
    )
    price = models.DecimalField(
        max_digits=28,
        decimal_places=2
    )
    description = models.TextField(max_length=256)
    quantity = models.IntegerField(
        default=0
    )
    img = models.ImageField(
        upload_to='products_images'
    )
    category = models.ForeignKey(
        to='ProductCategory',
        on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class BasketQuerySet(models.QuerySet):
    def total_sum(self):
        return sum(basket.sum() for basket in self)
    def total_qnt(self):
        return sum(basket.qnt for basket in self)
class Basket(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        to=Product,
        on_delete=models.CASCADE
    )
    qnt = models.PositiveSmallIntegerField(
        default=0
    )
    created_ttp = models.DateTimeField(
        auto_now_add=True
    )
    def __str__(self):
        return f'Basket for {self.user.email} | Products: {self.product.name}'
    def sum(self):
        return self.product.price * self.qnt
    objects = BasketQuerySet.as_manager()

