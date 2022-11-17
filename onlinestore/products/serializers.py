from dataclasses import fields
from unicodedata import name
from  rest_framework import serializers
from products.models import Mobiles

class ProductSerializer(serializers.Serializer):
    id=serializers.CharField(read_only=True)
    name=serializers.CharField()
    brand=serializers.CharField()
    price=serializers.IntegerField()
    specs=serializers.CharField()
    band=serializers.CharField()

class MobileSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    class Meta:
        model=Mobiles
        fields="__all__"
        #     "id",
        #     "name",
        # "brand",
        # "price",
        # "specs",
        # "band"
        


