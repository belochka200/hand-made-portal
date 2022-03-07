from statistics import mode
from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=255)
    describe = models.CharField(max_length=255)
    price = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
