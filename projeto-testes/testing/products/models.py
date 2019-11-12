from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    quantity = models.IntegerField()
    created = models.DateField()

    @property
    def has_stock(self):
        return self.quantity > 0
