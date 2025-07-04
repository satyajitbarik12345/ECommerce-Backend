from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(blank=True)
    stock = models.BooleanField(default=False)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name