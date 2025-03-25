from django.contrib import admin
from .models import Product, Order , mainPicture , YourEmail

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'image')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'product', 'quantity', 'total_price', 'shipping_cost', 
        'shipping_location', 'total_with_charge', 'customer_name', 
        'customer_address', 'customer_phone'
    )

admin.site.register(mainPicture)
admin.site.register(YourEmail)