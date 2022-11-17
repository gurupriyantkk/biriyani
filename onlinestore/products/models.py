
from django.db import models

class Mobiles(models.Model):
    name=models.CharField(max_length=200,unique=True)
    brand=models.CharField(max_length=140)
    price=models.PositiveIntegerField()
    specs=models.CharField(max_length=160)
    band=models.CharField(max_length=300)

    def __str__(self):
        return self.name