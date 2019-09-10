from rest_framework import serializers
from Django_login.models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=User
        fields=[
            "email",
            "password",
            "username",
            "phone_number",
            "photo",
            "age",
            "gender",
            "address",
        ]
class GoodsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Goods
        fields=[
            "goods_number",
            "goods_name",
            "goods_price",
            "goods_count",
            "goods_location",
            "goods_safe_date",
            "goods_pro_time",
            "goods_status",
        ]