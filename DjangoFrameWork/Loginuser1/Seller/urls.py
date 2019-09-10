from django.contrib import admin
from django.urls import path,re_path,include
from Seller.views import *


urlpatterns = [
    path('login/',login),
    path('logout/',logout),
    path('register/',register),
    path('index/',index),
    re_path('goods_list/(?P<status>[01])/(?P<page>\d+)/',goods_list),
    re_path('goods_status/(?P<state>\w+)/(?P<id>\d+)/',goods_status),
    path('person_info/',person_info)
    # path('add_goods/',add_goods),

]