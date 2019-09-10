import hashlib

from Seller.models import *

from django.core.paginator import Paginator
from django.shortcuts import render,HttpResponseRedirect



def loginvalid(fun):
    def inner(request,*args,**kwargs):
        cookie_email=request.COOKIES.get("email")
        session_email=request.session.get("email")
        if cookie_email and session_email and cookie_email==session_email:
            return fun(request,*args,**kwargs)
        else:
            return HttpResponseRedirect("/Seller/login/")
    return inner
def setPassword(password):
    md5=hashlib.md5()
    md5.update(password.encode())
    result=md5.hexdigest()
    return result
def login(request):
    error_message=""
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        if email:
            #首先检测email有没有
            user = User.objects.filter(email=email).first()
            if user:
                db_password=user.password
                password=setPassword(password)
                if password==db_password:
                    response=HttpResponseRedirect("/Seller/index/")
                    response.set_cookie("email",user.email)
                    response.set_cookie("user_id",user.id)
                    request.session["email"]=user.email
                    return response
                else:
                    error_message="密码错误"
            else:
                error_message="用户名不存在"
        else:
            error_message="邮箱不能为空"
    return render(request,'seller/login.html',locals())
def register(request):
    error_message=""
    if request.method=="POST":
        email=request.POST.get("email")
        password=request.POST.get("password")
        if email:
            user=User.objects.filter(email=email).first()
            if not user:
                new_user=User()
                new_user.email=email
                # new_user.username=email
                new_user.password=setPassword(password)
                new_user.save()
                return HttpResponseRedirect("/Seller/login/")
            else:
                error_message="邮箱已被注册，请登录"
        else:
            error_message="邮箱不能为空"
    return render(request,'seller/register.html',locals())
def logout(request):
    response=HttpResponseRedirect("/Seller/login/")
    keys=request.COOKIES.keys()
    for key in keys:
        response.delete_cookie(key)
    del request.session["email"]
    return response
@loginvalid
def index(request):
    user_id = request.COOKIES.get("user_id")
    user = User.objects.get(id=int(user_id))
    return render(request,'seller/index.html',locals())
@loginvalid
def goods_list(request,status,page=1):
    user_id = request.COOKIES.get("user_id")
    user = User.objects.get(id=int(user_id))
    page=int(page)
    if status=="1":
        goodses = Goods.objects.filter(goods_status=1)
    elif status=="0":
        goodses=Goods.objects.filter(goods_status=0)
    else:
        goodses = Goods.objects.all()
    all_goods=Paginator(goodses,10)
    goods_list=all_goods.page(page)
    return render(request,'seller/goods_list.html',locals())
def goods_status(request,state,id):
    id=int(id)
    goods=Goods.objects.get(id=id)
    if state=="up":
        goods.goods_status=1
    elif state=="down":
        goods.goods_status=0
    goods.save()
    url=request.META.get("HTTP_REFERER","/Seller/goods_list/1/1")
    return HttpResponseRedirect(url)
def person_info(request):
    error_meg=""
    user_id=request.COOKIES.get("user_id")
    user=User.objects.get(id=int(user_id))
    if request.method=="POST":
        Username=request.POST.get("username")
        Age = request.POST.get("age")
        Gender = request.POST.get("gender")
        Phone_number = request.POST.get("phone_number")
        Address = request.POST.get("address")
        if Username!=None:
            user.username=Username
        if Age!=None:
            user.age=Age
        if Gender!=None:
            user.gender=Gender
        if Phone_number!=None:
            user.phone_number=Phone_number
        if Address!=None:
            user.address=Address
        Photo=request.FILES.get("photo")
        if Photo:
            user.photo=Photo
        user.save()
    return render(request,'seller/person_info.html',locals())
def goods_add(request):
    user_id = request.COOKIES.get("user_id")
    user = User.objects.get(id=int(user_id))
    goods_type_list=Goods_type.objects.all()
    if request.method=="POST":
        goods=Goods()
        goods.goods_number=request.POST.get("goods_number")
        goods.goods_name=request.POST.get("goods_name")
        goods.goods_price=request.POST.get("goods_price")
        goods.goods_count=request.POST.get("goods_count")
        goods.goods_location=request.POST.get("goods_location")
        goods.goods_safe_date=request.POST.get("goods_safe_date")
        goods.goods_pro_time=request.POST.get("goods_pro_time")

        #保存商品类型的id
        goods_type_id=int(request.POST.get("goods_type"))
        goods.goods_type=Goods_type.objects.get(id=goods_type_id)

        #保存图片
        goods.picture=request.FILES.get("picture")

        #保存对应的卖家id
        seller_id=int(request.COOKIES.get("user_id"))
        goods.goods_store=User.objects.get(id=seller_id)
        goods.save()
    return render(request,'seller/goods_add.html',locals())

