from django.http import HttpResponse
from django.template.loader import get_template

# def index(request):
#     template=get_template("index.html")#加载页面
#     result=template.render({"name":"老李"})
#     return HttpResponse(result)

def page_list(request,page,day,age):
    page=int(page)
    day=int(day)
    age=int(age)
    template=get_template("index.html")
    result=template.render({"page":page,"day":day,"age":age})
    return HttpResponse(result)
def day_list(request,years):
    years=int(years)
    template=get_template("page_list.html")
    result=template.render({"years":years})
    return HttpResponse(result)
def money_list(request,number):
    number=int(number)
    template=get_template('page_list.html')
    result=template.render({"number":number})
    return HttpResponse(result)

def person(request):
    data={
        "name":"汉尼拔",
        "age":"25",
        "story":"打破了罗马不可战胜的神话"
    }
    temp=get_template("template_variable.html")
    result=temp.render(data)
    return HttpResponse(result)

def person1(request):
    data={
        "people":[
            {"name":"汉尼拔","age":"24","story":"打破了罗马不可战胜的神话"},
            {"name":"亚历山大","age":"22","story":"打败了波斯帝国"}
        ],
        "outer":"abc",
        "login_valid":0,
        "commit":"<script>alert('hello world')</script>"
    }
    temp=get_template("template_variable.html")
    result=temp.render(data)
    return HttpResponse(result)


books=[
    {"id":1,"title":"三国演义","author":"罗贯中","public_time":"1956-3-2","content":"魏蜀吴三国争霸","image":"images/sgyy.jpg"},
    {"id":2,"title":"西游记","author":"吴承恩","public_time":"1934-3-2","content":"唐僧孙悟空猪八戒沙僧师徒四人西天取经","image":"images/xyj.jpg"},
    {"id":3,"title":"水浒传","author":"施耐庵","public_time":"1943-3-2","content":"梁山一百零八好汉","image":"images/shz.jpg"},
    {"id":4,"title":"红楼梦","author":"曹雪芹","public_time":"1953-3-2","content":"贾宝玉的爱恨情仇","image":"images/hlm.jpg"},
    {"id":5,"title":"天才在左疯子在右","author":"高铭","public_time":"1967-3-2","content":"精神病人对世界的看法","image":"images/tczzfzzy.jpg"},
    {"id":6,"title":"丰乳肥臀","author":"莫言","public_time":"1953-3-2","content":"莫言的成长史","image":"images/frft.jpg"},
]
def book_list(request):
    temp=get_template("page_list.html")
    result=temp.render({"books":books})
    return HttpResponse(result)

def book(request,id):
    id=int(id)
    article=""
    for art in books:
        if art["id"]==id:
            article=art
            break
    temp=get_template("page.html")
    result=temp.render({"article":article})
    return HttpResponse(result)
