"""blog2018 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from .import views
from django.conf.urls.static import static  #上传图片文件需要
from django.conf import settings#上传图片文件需要

urlpatterns = [
    path('', views.index,name='blog_index'),
    path('blog_login/', views.login,name='blog_login'),
    path('blog_logout/', views.logout,name='blog_logout'),
    path('p/<int:wenzhang_id>', views.details,name='blog_wenzhangxiangqing'),
    path('upload/', views.uploadImg,name='blog_tupianshangchuang'),#图片上传路由
    path('show/', views.showImg,name='blog_tupianxianshi'),#图片显示路由
    path('q/<int:classify_id>', views.wenzhang_list,name='blog_wenzhangfenlei'),#
    path('date/<int:year>/<int:month>', views.nygd,name='blog_nianyueguidang'),#
    path('seav/', views.seav_img,name='qiniu_up_img'),#
    path('lunbotu/', views.lunbotu_img,name='qiniu_up_lunbotu'),#
    path('blog_register/', views.blog_register,name='blog_register'),#
    path('blog_dianzan/', views.dianzan,name='blog_dianzan'),#
    path('blog_sou/', views.sou,name='blog_sou'),#

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #这句话是用来指定和映射静态文件的路径
