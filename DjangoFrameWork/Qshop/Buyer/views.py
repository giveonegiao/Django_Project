import datetime
from dateutil.relativedelta import relativedelta


from Seller.models import *
from django.shortcuts import render,HttpResponseRedirect
from Seller.views import setPassword

def loginValid(fun):
    def inner(request,*args,**kwargs):
        cookie_user=request.COOKIES.get("username")
        session_user=request.session.get("username")
        if cookie_user and session_user and cookie_user==session_user:
            return fun(request,*args,**kwargs)
        else:
            return HttpResponseRedirect("/Buyer/login/")
    return inner

def register(request):
    if request.method=="POST":
        buyer_username=request.POST.get("user_name")
        buyer_password=request.POST.get("pwd")
        buyer_email=request.POST.get("email")
        if buyer_email:
            user = User.objects.filter(email=buyer_email).first()
            if not user:
                new_user = User()
                new_user.email = buyer_email
                new_user.password = setPassword(buyer_password)
                new_user.save()
                return HttpResponseRedirect("/Buyer/login/")
            else:
                error_message = "邮箱已被注册，请登录"
        else:
            error_message = "邮箱不能为空"
    return render(request,'buyer/register.html',locals())
def login(request):
    if request.method=="POST":
        buyer_password=request.POST.get("pwd")
        buyer_email=request.POST.get("email")
        if buyer_email:
            user=User.objects.filter(email=buyer_email).first()
            db_password=user.password
            password=setPassword(buyer_password)
            if db_password==password:

                response=HttpResponseRedirect("/Buyer/index/")
                response.set_cookie("username",user.username)
                response.set_cookie("user_id",user.id)
                request.session["username"]=user.username
                return response

    return render(request,'buyer/login.html',locals())

def logout(request):
    url=request.META.get("HTTP_REFERER","/Buyer/index/")
    response = HttpResponseRedirect(url)
    for key in request.COOKIES:
        response.delete_cookie(key)
    del request.session["username"]
    return response

def index(request):
    goods_type=Goods_type.objects.all()
    result=[]
    for ty in goods_type:
        all_type_good=ty.goods_set.order_by("-goods_pro_time")
        if len(all_type_good)>=4:
            all_type_good=all_type_good[:4]
            result.append({"type":ty,"type_goods_list":all_type_good})
    return render(request,'buyer/index.html',locals())

def goods_list(request):
    """
    type 代表请求的类型
        t 按照类型查询
            keywords 必须是类型id
        k 是按照关键字查询
            keywords可以是任何东西
    keywords 代表请求的关键字

    """
    request_type=request.GET.get("type")#获取请求的类型t类型查询  k关键字查询
    keyword=request.GET.get("keywords")#查询的内容 t类型 k为类型id  k类型 k为关键字
    goods_list=[]
    if request_type=="t":
        if keyword:
            id=int(keyword)
            goods_type=Goods_type.objects.get(id=id)#先查询类型
            goods_list=goods_type.goods_set.order_by("-goods_pro_time")#在查询类型对应的商品
    elif request_type=="k":
        if keyword:
            goods_list=Goods.objects.filter(goods_name__contains=keyword).order_by("-goods_pro_time")#模糊查询商品名称含有关键字的商品
    if goods_list:#限定推荐的条数
        lenth=len(goods_list)/5
        if lenth!=int(lenth):
            lenth+=1
        lenth=int(lenth)
        recommend=goods_list[:lenth]
    return render(request,'buyer/goods_list.html',locals())

def goods_details(request,id):
    goods=Goods.objects.get(id=int(id))
    return render(request,'buyer/goods_details.html',locals())

@loginValid
def user_center_info(request):
    user_id=request.COOKIES.get("user_id")
    user=User.objects.get(id=int(user_id))
    return render(request,'buyer/user_center_info.html',locals())

