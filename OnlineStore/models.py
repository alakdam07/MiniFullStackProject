from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=40)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=3000)


class Offer(models.Model):
    code = models.CharField(max_length=10)
    discount = models.IntegerField()
