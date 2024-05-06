from django.db import models
from app_auth.models import Credentials


class Product(models.Model):
    image =models.ImageField(upload_to='product_images/', blank=True, null=True)
    name = models.CharField(max_length=255 , default = "name",)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.OneToOneField(Credentials, on_delete=models.CASCADE)
    items = models.ManyToManyField(Product, through='CartItem')

    def __str__(self):
        return f"{self.user.username}'s Cart"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"
