"""ArticleBlog URL Configuration

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
from Article.views import *
#from ArticleBlog.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$',index),
    re_path(r'new/(?P<types>\w+)/(?P<p>\d{1,2})',new),
    re_path('newabout/(?P<id>\d{1,10})',newabout),
    path('index/',index),
    re_path('newlistpic/(?P<p>\d{1,10})',newlistpic),
    path('ckeditor/',include('ckeditor_uploader.urls')),
    # path('req_arg/',req_arg),
    path('form_exam/',form_exam),

    path('register/',register),
    path('user_valid/',user_valid),
    path('username_check/',username_check),

    path('message/',message),

    path('jq/',jq),

    path('agp/',ajax_get_page),
    path('agd/',ajax_get_data),

    path('app/',ajax_post_page),
    path('apd/',ajax_post_data),

    path('login/',login),
    path('logout/',logout),
]
