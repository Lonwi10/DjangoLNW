from __future__ import unicode_literals

from django.db import models
from datetime import date
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=16)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categories'


class Product(models.Model):
    nom = models.CharField(max_length=32)
    description = models.TextField()
    price = models.IntegerField()
    category = models.ForeignKey(Category)

    def __str__(self):
        return self.nom

class Carrito(models.Model):
    nom = models.CharField(max_length=200,default=str(date.today()))
    obert = models.BooleanField(default=True)
    user = models.ForeignKey(User, blank=True, null=True)
    data = models.DateField(default=date.today())

    def __str__(self):
        return self.nom


class Detall(models.Model):
    producte = models.ForeignKey(Product)
    carrito = models.ForeignKey(Carrito)
    quantitat = models.FloatField()
    def __str__(self):
        return str(self.carrito.nom)+str(self.producte.nom)