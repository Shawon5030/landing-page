from django.db import models
from decimal import Decimal

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    
    def __str__(self):
        return self.name

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    
    shipping_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    shipping_location = models.CharField(max_length=50, default="Outside Dhaka")
    
    total_with_charge = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    
    customer_name = models.CharField(max_length=255, blank=True, null=True)
    customer_address = models.TextField(blank=True, null=True)
    customer_phone = models.CharField(max_length=15, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.total_price = self.product.price * self.quantity
        self.total_with_charge = self.total_price + self.shipping_cost
        super().save(*args, **kwargs)

class mainPicture(models.Model):
    picture = models.ImageField(blank=True,null=True)
class YourEmail(models.Model):
    email = models.EmailField()