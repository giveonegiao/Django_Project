"""Loginuser1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,re_path,include
from Django_login.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('Seller/',include("Seller.urls")),
]


from django.views.decorators.csrf import csrf_exempt

from rest_framework import routers

router=routers.DefaultRouter()
router.register("goods",GoodsViewSet)
router.register("user",UserViewSet)


urlpatterns+=[
    re_path('goods_list_api/(?P<status>[01])/(?P<page>\d+)/', goods_list_api),
    path('goods/',csrf_exempt(GoodsView.as_view())),
    re_path("^API/",include(router.urls)),
]
