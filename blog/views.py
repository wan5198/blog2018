import json
from django.shortcuts import render,get_object_or_404,redirect,reverse
from .models import Blogwenzhang,Recommended,Classify,Pinlun,IMG,Lunbotu,Guanggaoimg,Good_url,User_EX,DianzanModel
from django.core.paginator import Paginator
from blog2018.up_qiniu import qiniu_up
from django.http import HttpResponse
from django.contrib.auth.models import User
from .forms import LoginFrom,RegForm
import os
from django.db.models import Count,Sum
from django.contrib import auth #导入用户模块
from django import forms
def index(request):
    #获取全部文章
    wenzhangs = Blogwenzhang.objects.all()
    recommended = Recommended.objects.all()
    classify = Classify.objects.all()
    pingluns = Pinlun.objects.all()
    index_lunbotu = Lunbotu.objects.all()
    weixindashangimg = Guanggaoimg.objects.all()
    goodurls=Good_url.objects.all()
    # 分页
    page_num = request.GET.get('page', 1)  # 获取url上 ？page= 的分页参数，GET请求,默认取1
    blogs_all_list = Blogwenzhang.objects.all()  # 全部文章获取
    paginator = Paginator(blogs_all_list, 8)  # 8篇分一次页
    page_of_blogs = paginator.get_page(page_num)  # get_page处理URL传来的参数，就算传来不合格参数，就自动使用默认值
    #（开始做分页缩显）获取当前页码，通过number方法
    dangqianye = page_of_blogs.number
    #当前页-2，当前页-1，当前页0，当前页+1，当前页+2，组成一个列表
    page_range = list(range(max(dangqianye-2,1),dangqianye)) + list(range(dangqianye,min(dangqianye+2,paginator.num_pages)+1))
    #加上省略号标记
    #如果当前页页码范围第一页减去1大于等于2，就添加一个“...”
    if page_range[0] - 1 >= 2:
        page_range.insert(0,'....')
    # 如果最后页-当前页页码范围最后也大于等于2，就添加一个“...”
    if paginator.num_pages - page_range[-1] >= 2:
        page_range.append("....")
    #加上首页和尾页
    if page_range[0] != 1:
        page_range.insert(0,1)
    if page_range[-1] != paginator.num_pages:
        page_range.append(paginator.num_pages)
    content = {}
    content['wenzhangs'] = wenzhangs
    content['recommended'] = recommended
    content['classifys'] = classify
    content['pages'] = page_of_blogs
    content['page_num'] = page_num
    content['pingluns'] = pingluns
    content['index_lunbotus'] = index_lunbotu
    content['wexindashangimg'] = weixindashangimg
    content['page_range'] = page_range
    content['goodurls'] = goodurls
    content['blog_dates'] = Blogwenzhang.objects.dates('release_time','month',order='DESC')
    #博客文章类.objects.dates 这个方法获取时间处理（“需要处理的模型字段：发布时间”，“月”，order=排序方式DESC倒叙，ASC正序
    return render(request,'blog/index.html',content)

def login(request):
    if request.method == 'POST':
        login_form = LoginFrom(request.POST)
        if login_form.is_valid():
            user = login_form.cleaned_data['user']
            auth.login(request,user)
            return redirect(reverse('blog_index'))
        
    else:
        login_form = LoginFrom()
    context = {
        'login_form': login_form
    }
    return render(request, 'blog/login.html', context)

def logout(request):
    auth.logout(request)
    return redirect(reverse('blog_index'))

def blog_register(request):
    if request.method == 'POST':
        regform =RegForm(request.POST)  #提交内容去表单验证
        if regform.is_valid(): #如果验证通过，就从表单里取回数据
            username = regform.cleaned_data['username']
            password = regform.cleaned_data['password1']
            email = regform.cleaned_data['email']
            user=User.objects.create_user(username=username,password=password,email=email)
            user.save()
            user_ex = User_EX()
            user_ex.user = User.objects.filter(username=username).first()
            user_ex.bj = 'blog_2018'
            user_ex.save()
            user = auth.authenticate(username=username, password=password)  # 去用户模型里比对
            auth.login(request, user)
            # 重定向
            p_url = reverse('blog_index')
            # 反转
            return redirect(p_url)
    else:
        regform = RegForm()
    context = {
        'regform': regform
              }
    return render(request, 'blog/blog_register.html', context)


def details(request,wenzhang_id):
    wenzhang =get_object_or_404(Blogwenzhang,pk=wenzhang_id)
    #统计阅读量
    wenzhang.reads += 1
    wenzhang.save()
    #评论展示
    pingluns = Pinlun.objects.filter(wenzhang_id=wenzhang.id)
    #获取分类标签
    classify = Classify.objects.all()
    #获取点赞数量
    m = DianzanModel.objects.filter(wenzhang_id=wenzhang_id).aggregate(zan_nmus=Sum('zan_num'))
    #获取微信打赏图
    weixindashangimg = Guanggaoimg.objects.all()
    #上一篇文章与下一篇文章
    #__gt:大于，查找出比当前文章发表时间大的全部文章列表，取最后一条.last(),__lt,小于
    upwenzhang = Blogwenzhang.objects.filter(release_time__gt=wenzhang.release_time).last()
    nextwenzhang = Blogwenzhang.objects.filter(release_time__lt=wenzhang.release_time).first()
    #如果走POST
    if request.method == 'POST':
        referer = request.META.get('HTTP_REFERER', reverse('blog_index')) #记录当前用户所处位置
        user = request.user  #获取登录用户的信息，信息存在request里
        email = user.email#获取用户的电子邮件
        if not user.is_authenticated: #如果没用户
            return render(request, 'blog/404.html', {'message': "没有登录！",'referer_to':referer})
        comment = request.POST.get('comment', '').strip() #.strip()可以将空格视为空
        if comment == '':#如果没有评论，或内容为空格，
            return render(request, 'blog/404.html', {'message': "内容不能为空或空格！",'referer_to':referer})
        try:
            wenzhang_id = request.POST.get('wenzhang_id')
            wenzhang = Blogwenzhang.objects.get(pk=wenzhang_id)
        except Exception as e:
            return render(request, 'blog/404.html', {'message': "文章不存在！",'referer_to':referer})
        pingluns = Pinlun(author=user, email=email, content=comment)
        pingluns.wenzhang = wenzhang
        pingluns.user = user
        pingluns.save()
        #重定向
        p_url = reverse('blog_wenzhangxiangqing',kwargs={'wenzhang_id':wenzhang_id})
        #反转
        return redirect(p_url)
    wenzhangs=Blogwenzhang.objects.order_by('?')  #order_by 条件查询排序，？表示随机排序
    #参考资料：http://blog.csdn.net/shanliangliuxing/article/details/7971687
    content={}
    content['wenzhang']=wenzhang
    content['pingluns']=pingluns
    content['classifys'] = classify
    content['wenzhangs'] = wenzhangs
    content['wexindashangimg'] = weixindashangimg
    content['upwenzhang'] = upwenzhang
    content['nextwenzhang'] = nextwenzhang
    content['m'] = m['zan_nmus']
    return render(request,'blog/details.html',content)
#上传图片路由
def uploadImg(request):
    if request.method == 'POST':
        new_img = IMG(
            img=request.FILES.get('img'),
            name = request.FILES.get('img').name #图片取名字
        )
        new_img.save()
    return render(request, 'blog/uploadimg.html')
#显示图片路由
def showImg(request):
    imgs = IMG.objects.all()
    content = {
        'imgs':imgs,
    }
    for i in imgs:
        print (i.img.url)
    return render(request, 'blog/showimg.html', content)

def seav_img(request):
    img_pk = request.GET.get('pk')
    u = IMG.objects.get(pk=img_pk)
    u_img ="."+u.img.url
    u_name = u.name
    qiniu_up(u_img, u_name)
    u.number += 1
    u.save()
    return HttpResponse("成功！")

def lunbotu_img(request):
    img_pk = request.GET.get('pk')
    u = Lunbotu.objects.get(pk=img_pk)
    u_img ="/usr/local/blog2018" + os.sep + u.index_img.url
    u_name = u.name
    qiniu_up(u_img, u_name)
    u.number += 1
    u.save()
    return HttpResponse("成功！")

#文章分类list
def wenzhang_list(request,classify_id):
    wenzhang_lists = Blogwenzhang.objects.filter(classify_id=classify_id).all()# 全部同类下全部文章获取
    classify = Classify.objects.all()
    wenzhangs = Blogwenzhang.objects.order_by('?')
    weixindashangimg = Guanggaoimg.objects.all()
    # 分页
    page_num = request.GET.get('page', 1)  # 获取url上 ？page= 的分页参数，GET请求,默认取1
    paginator = Paginator(wenzhang_lists, 10)  # 7篇分一次页
    page_of_blogs = paginator.get_page(page_num)  # get_page处理URL传来的参数，就算传来不合格参数，就自动使用默认值



    content = {
        'wenzhang_lists': wenzhang_lists,
        'classifys' : classify,
        'wenzhangs' : wenzhangs,
        'wexindashangimg': weixindashangimg,
        'page_of_blogs':page_of_blogs
    }
    return render(request, 'blog/list.html',content)

#按年月归档处理视图
def nygd(request,year,month):
    wenzhang_lists = Blogwenzhang.objects.filter(release_time__year=year,release_time__month=month)  # 全部同类下全部文章获取
    wenzhangs = Blogwenzhang.objects.order_by('?')
    weixindashangimg = Guanggaoimg.objects.all()
    # 分页
    page_num = request.GET.get('page', 1)  # 获取url上 ？page= 的分页参数，GET请求,默认取1
    paginator = Paginator(wenzhang_lists, 10)  # 7篇分一次页
    page_of_blogs = paginator.get_page(page_num)  # get_page处理URL传来的参数，就算传来不合格参数，就自动使用默认值
    blog_dates = Blogwenzhang.objects.dates('release_time', 'month', order='DESC')
    # 博客文章类.objects.dates 这个方法获取时间处理（“需要处理的模型字段：发布时间”，“月”，order=排序方式DESC倒叙，ASC正序
    classify = Classify.objects.all()
    content = {
        'wenzhang_lists': wenzhang_lists,
        'wenzhangs': wenzhangs,
        'wexindashangimg': weixindashangimg,
        'page_of_blogs': page_of_blogs,
        'blog_dates':blog_dates,
		'classifys':classify
    }
    return render(request, 'blog/date_list.html', content)

#点赞处理
def dianzan(request):
    if request.is_ajax():
        zan = request.POST.get('zan')
        wenzhang_id = request.POST.get('wenzhang_id')
        user_id = request.POST.get('user_id')
        user = User.objects.get(pk=user_id)
        zans = DianzanModel(wenzhang_id=wenzhang_id, zan_num=zan)
        zans.user_id = user
        zans.save()
        ret = {"msg":"感谢点赞+1"}

        return HttpResponse(json.dumps(ret))
#搜索视图
def sou(request):
    q = request.GET.get('sou')
    if not q:
        error_msg = '请输入搜索关键词字'
        return render(request,'blog/404.html',{'message':error_msg})
    post_list = Blogwenzhang.objects.filter(content__icontains=q)
    classify = Classify.objects.all()
    wenzhangs = Blogwenzhang.objects.order_by('?')
    weixindashangimg = Guanggaoimg.objects.all()
    content = {
        'classifys': classify,
        'wenzhangs': wenzhangs,
        'wexindashangimg': weixindashangimg,
        'sou': post_list
    }
    return render(request, 'blog/list_sou.html', content)