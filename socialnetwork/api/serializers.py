from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Posts
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["email","username","password"]
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class Post(serializers.ModelSerializer):
    user=serializers.CharField(read_only=True)
    created_date=serializers.CharField(read_only=True)
    class Meta:
        model = Q
        