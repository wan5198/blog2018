from django.shortcuts import render,reverse,redirect
from django.http import HttpResponse
# Create your views here.
from .form import LoginFrom #引入
from django.contrib import auth #引入用户模块

def index(request):

    return HttpResponse ("这是成绩查询")


def login(request):
    if request.method == 'POST': #如走POST请求
        login_form = LoginFrom(request.POST) #绑定验证表单，并将POST内容提交去验证
        if login_form.is_valid(): #如果验证通过
            user = login_form.cleaned_data['user'] #把表单验证好的user取出来
            auth.login(request,user)  #  就让这个用户登陆
            # return render(request.GET.get('from',reverse('cjcx2018_index')))
            return redirect(reverse('cjcx2018_index'))
                #跳转回来登陆的页面，如果未传入from=就回首页（每个登陆链接处：
            # <a href="{% url 'blog_login' %}?from={{ request.get_full_path }}">还没有账号？点此注册</a>
    else:
        login_form = LoginFrom() # 绑定验证表单
    context={
            'login_form':login_form
        }
    return render(request,'cjcx2018/cjcx2018_login.html',context)