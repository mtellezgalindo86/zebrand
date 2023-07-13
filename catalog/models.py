from django.db import models
from django.contrib.auth.models import AbstractUser


class Product(models.Model):
    sku = models.CharField(max_length=100)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    brand = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_anonymous = models.BooleanField(default=False)
