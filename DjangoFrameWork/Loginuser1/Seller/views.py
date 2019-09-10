import hashlib

from Django_login.models import *

from django.core.paginator import Paginator
from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from django.http import JsonResponse
from django.views import View


def loginvalid(fun):
    def inner(request,*args,**kwargs):
        cookie_email=request.COOKIES.get("email")
        session_email=request.session.get("email")
        if cookie_email and session_email and cookie_email==session_email:
            return fun(request,*args,**kwargs)
        else:
            return HttpResponseRedirect("/login/")
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
    return render(request,'Seller/login.html',locals())
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
            else:
                error_message="邮箱已被注册，请登录"
        else:
            error_message="邮箱不能为空"
    return render(request,'Seller/register.html',locals())
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
    return render(request,'Seller/index.html',locals())
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
    return render(request,'Seller/goods_list.html',locals())
def goods_status(request,state,id):
    id=int(id)
    goods=Goods.objects.get(id=id)
    if state=="up":
        goods.goods_status=1
    elif state=="down":
        goods.goods_status=0
    goods.save()
    url=request.META.get("HTTP_REFERER","/goods_list/1/1")
    return HttpResponseRedirect(url)
def person_info(request):
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
        elif Age!=None:
            user.age=Age
        elif Gender!=None:
            user.gender=Gender
        elif Phone_number!=None:
            user.phone_number=Phone_number
        elif Address!=None:
            user.address=Address
        Photo=request.FILES.get("photo")
        if Photo:
            user.photo=Photo
        user.save()


    return render(request,'Seller/person_info.html',locals())
