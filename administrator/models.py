from django.db import models


class Seller(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    CATOGORY = (
        ('kids','kids'),
        ('mens','mens'),
        ('womens','womens'),
    )

    name = models.CharField(max_length=100,null=True)
    image = models.ImageField(upload_to='pics',null=True)
    price = models.FloatField()
    catogory = models.CharField(max_length=100, null=True, choices=CATOGORY)
    seller = models.ForeignKey(Seller,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.name


class Messages(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=30)
    message = models.TextField()

    def __str__(self):
        return self.name