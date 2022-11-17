from django.shortcuts import render
from api.serializers import UserSerializer,QuestionSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django.contrib.auth.models import User

# Create your views here.

class UserView(ModelViewSet):
    serializer_class=UserSerializer
    queryset=User.objects.all()

class QuestionView(ModelViewSet):
    serializer_class=QuestionSerializer
    