from django.db import models


class User(models.Model):
    email=models.EmailField()
    password=models.CharField(max_length=32)

    username=models.CharField(max_length=32,null=True,blank=True)
    phone_number=models.CharField(max_length=11,null=True,blank=True)
    photo=models.ImageField(upload_to="seller/images",default="images/default.jpg")
    age=models.IntegerField(null=True,blank=True)
    gender=models.CharField(max_length=32,null=True,blank=True)
    address=models.TextField(null=True,blank=True)
    user_type = models.IntegerField(null=True, blank=True)  # 0为买家  1为卖家  2为管理员


class Goods_type(models.Model):
    type_label=models.CharField(max_length=32)
    type_describe=models.TextField()
    type_picture=models.ImageField(upload_to="images")

class Goods(models.Model):
    goods_number = models.CharField(max_length=11)
    goods_name = models.CharField(max_length=32)
    goods_price = models.FloatField()
    goods_count = models.IntegerField()
    goods_location = models.CharField(max_length=254)
    goods_safe_date = models.IntegerField()
    goods_pro_time = models.DateField()
    goods_status = models.IntegerField(default=1) #0为下架，1 为在售
    goods_description=models.TextField(default="真香,好吃不贵")

    picture=models.ImageField(upload_to="seller/images")
    goods_store=models.ForeignKey(to=User,on_delete=models.CASCADE,default=1)
    goods_type=models.ForeignKey(to=Goods_type,on_delete=models.CASCADE,default=1)

# Create your models here.
