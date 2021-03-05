from django.contrib.auth.models import User
from django.db import models

from administrator.models import Product


class Cart(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    count = models.IntegerField(default=1)
    total = models.IntegerField(default=0,null=True)

    def __str__(self):
        return self.product.name

    def get_total(self):
        self.total = self.count * self.product.price
        return self.total

    def update_count(self):
        self.count = self.count + 1


class Order(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    count = models.IntegerField(default=1)
    total = models.IntegerField(default=0, null=True)
    delivered = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def get_total(self):
        self.total = self.count * self.product.price
        return self.total

    def update_count(self):
        self.count = self.count + 1


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    text = models.CharField(max_length=300, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    success = models.BooleanField(null=True)
    seen = models.BooleanField(default=False, null=True)

    def __str__(self):
        return str(self.user)+"  "+str(self.text)


