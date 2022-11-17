from django.db import models
from django.contrib.auth.models import User


class Posts(models.Model):
    title=models.CharField(max_length=250)
    image=models.ImageField(upload_to="images",null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_date=models.DateField(auto_now_add=True)
    liked_by=models.ManyToManyField(User,related_name="likes")

    def __str__(self):
        return self.title

class Comment(models.Model):
    Comment=models.CharField(max_length=250)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_date=models.DateField(auto_now_add=True)
    post=models.ForeignKey(Posts,on_delete=models.CASCADE)

    def __str__(self):
        return self.Comment+


