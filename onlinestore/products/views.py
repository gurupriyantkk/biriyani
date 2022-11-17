from ast import Delete
from pickle import OBJ
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from products.models import Mobiles
from products.serializers import MobileSerializer, ProductSerializer


# Create your views here.
class Productsviews(APIView):
    def get(self,request,*args,**kw):
        qs=Mobiles.objects.all()
        if "brand" in request.query_params:
            qs=qs.filter(brand=request.query_params.get("brand"))
            
        if "band" in request.query_params:
            qs=qs.filter(band=request.query_params.get("band"))

        if "price_lt" in request.query_params:
            qs=qs.filter(price_lt=request.query_params.get("price_lt"))
        

        serializer=ProductSerializer(qs,many=True)
        return Response(data=serializer.data)
    def post(self,request,*args,**kw):
        serializer=MobileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        # serializer=ProductSerializer(data=request.data)
        # if serializer.is_valid():
        #     Mobiles.objects.create(**serializer.validated_data)
        #     return Response(data=serializer.data)
        # else:
        #     return Response(data=serializer.errors)

class ProductDetailview(APIView):
    def get(self,request,*args,**kw):
        id=kw.get("id")
        qs=Mobiles.objects.get(id=id)
        serializer=ProductSerializer(qs)
        return Response(data=serializer.data)
    
    def delete(self,request,*args,**kw):
        id=kw.get("id")
        Mobiles.objects.filter(id=id).delete()
        return Response(data="deleted")
        
    def put(self,request,*args,**kw):
        id=kw.get("id")
        obj=Mobiles.objects.get(id=id)
        serializer=MobileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
            
        # id=kw.get("id")
        # serializer=ProductSerializer(data=request.data)
        # if serializer.is_valid():
        #     Mobiles.objects.filter(id=id).update(**serializer.validated_data)
        #     return Response(data=serializer.data)
        # else:
        #     return Response(data=serializer.errors)