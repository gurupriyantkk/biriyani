from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.

class Products(models.Model):
    name=models.CharField(max_length=200)
    description=models.CharField(max_length=250)
    brand=models.CharField(max_length=200)
    price=models.PositiveIntegerField()
    image=models.ImageField(null=True,upload_to="images")
    category=models.CharField(max_length=200)

    @property
    def product_reviews(self):
        return self.reviews_set.all()

    def __str__(self) -> str:
        return self.name

class Reviews(models.Model):
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    comment=models.CharField(max_length=250)
    rating=models.PositiveIntegerField(validators=(MinValueValidator(1),MaxValueValidator(5)))


class Carts(models.Model):
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
    options=(
        ("in-cart","in-cart"),
        ("order-placed","order-placed"),
        ("removed","removed")
    )
    status=models.CharField(max_length=200,choices=options,default="in-cart")
