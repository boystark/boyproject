from django.shortcuts import render,HttpResponse

# Create your views here
def index(request):
    #return HttpResponse("欢迎访问我的博客首页！")
    return render(request, 'myblog/index.html', context={
        'title': '我的博客首页',
        'welcome': '欢迎访问杨康的博客首页'
    })