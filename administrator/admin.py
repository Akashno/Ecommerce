from django.contrib import admin

# Register your models here.
from administrator.models import Product, Seller
from user.models import Cart

admin.site.register(Product)
admin.site.register(Seller)
admin.site.register(Cart)