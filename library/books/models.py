from enum import auto
from turtle import title
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Questions:
    title=models.CharField()
    description=models.CharField()
    image=models.ImageField(null=True)
    created_date=models.DateField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

class Answers(models.Model):
    question=models.ForeignKey(Questions)
    answer=models.CharField()
    user=models.ForeignKey()
    created_date=models.DateField(auto_now_add=True)
    up_vote=models.ManyToManyField(user)