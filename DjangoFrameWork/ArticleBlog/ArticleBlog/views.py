from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render_to_response


from Article.models import *


def newlist(request):
    #底层版本
    template=get_template("base.html")
    result=template.render({})
    return HttpResponse(result)

def new(request):
    #半新版本
    article_list=Article.objects.order_by('-id')
    return render_to_response('new.html',locals())


def newabout(request):
    #当前版本
    username='yang'
    return render_to_response('newabout.html',locals())



def index(request):
    template = get_template('index.html')
    result = template.render({})
    return HttpResponse(result)


def req_arg(request):
    request_mothod=dir(request)
    return render_to_response('request_argument.html',locals())


def form_exam(request):
    searchKey=request.GET.get("searchKey")
    request_form=[]
    if searchKey:
        request_form = Article.objects.filter(title__contains=searchKey)
    return render_to_response('search_form.html',locals())
