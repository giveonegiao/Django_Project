from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from django.shortcuts import render_to_response


from Article.models import *
from django.core.paginator import Paginator

#装饰器
def loginvalid(func):
    def inner(request,*args,**kwargs):
        username=request.COOKIES.get("username")
        session_username=request.session.get("username")
        if username and session_username:
            return func(request,*args,**kwargs)
        else:
            return HttpResponseRedirect("/login/")
    return inner


def set_page(page_list,page):
    """
    page_list   页码范围
    page  页码
    想要当前页码的前两页和后两页
    """
    if page-3<0:
        start=0
    else:
        start=page-3
    if page+2>49:
        end=49
    else:
        end=page+2
    return list(page_list[start:end])
def last_page(p):
    return p-1
def next_page(p):
    return p+1
def new(request,types,p):
    #半新版本
    p=int(p)
    page_size=6
    # 总文章数
    # articles=Article.objects.all().order_by("public_time")
    articles=ArticleType.objects.get(label=types).article_set.order_by("-public_time")
    # 6篇文章一页，总页数
    article_list=Paginator(articles,page_size)
    # 当前页article_list.page(p)是取你分页后的第p页<page p of 52>
    page_article=article_list.page(p)
    #页码显示
    page_range = set_page(article_list.page_range,p)
    # 上一页
    last = last_page(p)
    # 下一页
    next = next_page(p)
    return render_to_response('new.html', locals())
def newlistpic(request,p):
    p=int(p)
    page_size=8
    articles=Article.objects.order_by("-public_time")
    article_picture=Paginator(articles,page_size)
    page_picture=article_picture.page(p)
    pic_range=set_page(article_picture.page_range,p)
    last_p = last_page(p)
    next_p = next_page(p)
    return render_to_response('newlistpic.html',locals())

@loginvalid
def index(request):
    article_content=Article.objects.order_by("-public_time")[:6]
    article_recommend=Article.objects.filter(recommend=1).order_by("-public_time")[:7]
    article_click=Article.objects.order_by("-click")[:12]

    return render_to_response("index.html",locals())


def newlist(request):
    #底层版本
    template=get_template("base.html")
    result=template.render({})
    return HttpResponse(result)
def newabout(request,id):
    #当前版本
    id=int(id)
    article=Article.objects.get(id=id)
    last=id-1
    next=id+1
    return render_to_response('newabout.html',locals())



def message(request):
    return render(request,'message.html')

# def form_exam(request):
#     searchKey=request.GET.get("searchKey")
#     request_form=[]
#     if searchKey:
#         request_form = Article.objects.filter(title__contains=searchKey)
#     return render_to_response('search_form.html',locals())

def form_exam(request):
    searchKey=request.GET.get("searchKey")
    request_form=[]
    if searchKey:
        request_form = Article.objects.filter(title__contains=searchKey)
    return render(request,'search_form.html',locals())


import hashlib#md5加密
def setPassword(password):
    md5=hashlib.md5()
    md5.update(password.encode())
    result=md5.hexdigest()
    return result


from Article.forms import Register
def register(request):
    register_form = Register()
    if request.method=='POST':#判断请求方式
        data_valid=Register(request.POST)
        if data_valid.is_valid():#判断提交的数据是否合法，如果合法为True，否则为False
            clean_data=data_valid.cleaned_data
            username = clean_data.get("username")  # 获取用户名
            password = clean_data.get("password")  # 获取密码
            email=clean_data.get("email")
        # if username and password:
            u=User()#实例化模型
            u.username=username
            u.password=setPassword(password)
            u.email=email
            u.save()
        else:
            errors=data_valid.errors
            print(errors)
    return render(request,'form_exam.html',locals())

def user_valid(request):
    email=request.GET.get("email")#获取请求的email
    result={"code":"400","data":""}#定义返回的数据格式
    if email:
        user=User.objects.filter(email=email).first()
        if user:#用户已存在，邮箱不可用
            result["data"]="当前邮箱已经被注册，请登录"
        else:#用户不存在，邮箱可以用
            result["code"]='200'
            result["data"]="邮箱可以注册"
    else:
        result["data"]="邮箱不能为空"
    return JsonResponse(result)

def username_check(request):
    username=request.GET.get("username")#获取请求的username
    result={"code":"400","data":""}#定义返回的数据格式
    if username:
        user=User.objects.filter(username=username).first()
        if user:#用户已存在，用户名不可用
            result["data"]="当前用户名已经被注册，请重新输入"
        else:#用户不存在，用户名可以用
            result["code"]='200'
            result["data"]="用户名可以使用"
    else:
        result["data"]="用户名不能为空"
    return JsonResponse(result)

def jq(request):
    return render(request,'jq_exam.html')

def ajax_get_page(request):
    return render(request,'ajax_get_page.html')

from django.http import JsonResponse
def ajax_get_data(request):
    name=request.GET.get("name")
    return JsonResponse({"hello":"后台数据，你的名字是%s"%name})

def ajax_post_page(request):
    return render(request,'ajax_post_page.html')

def ajax_post_data(request):
    return JsonResponse({"hello": "这是双击后后台的数据"})


from django.http import HttpResponseRedirect
def login(request):
    if request.method=='POST':
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=User.objects.filter(username=username).first()
        if user:
            db_password=user.password
            password=setPassword(password)
            if password==db_password:
                response=HttpResponseRedirect("/index/")
                response.set_cookie("username",user.username)#这里username要与登出时的username一样
                response.set_cookie("age","18")
                request.session["username"]=user.username

                return response #这里写路由 不写页面
    return render(request,'login.html')

def logout(request):
    response=HttpResponseRedirect("/login/")
    response.delete_cookie("username")
    response.delete_cookie("age")
    del request.session["username"]
    return response




