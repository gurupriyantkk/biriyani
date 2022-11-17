"""onlinestore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from operator import imod
from django.contrib import admin
from django.urls import path
from products.views import Productsviews,ProductDetailview


from products.views import Productsviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/',Productsviews.as_view()),
    path('products/<int:id>/',ProductDetailview.as_view())
]


