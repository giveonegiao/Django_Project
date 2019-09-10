from Qshop.urls import *
from Buyer.views import *
urlpatterns = [
    path('login/',login),
    path('register/',register),
    path('logout/',logout),
    path('index/',index),
    path('goods_list/',goods_list),
    re_path('goods_details/(?P<id>\d+)/',goods_details),
    path('user_center_info/',user_center_info)


]