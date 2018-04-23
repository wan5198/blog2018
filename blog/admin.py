#后台管理管理模型
from django.contrib import admin
from .models import Blogwenzhang,Classify,Recommended,IMG,Lunbotu,Guanggaoimg,Good_url,User_EX,Pinlun
from django.template.defaultfilters import mark_safe


# Register your models here.
@admin.register(Classify)  #用装饰器注册
class ClassifyAdmin(admin.ModelAdmin): #要显示的字段
    list_display = ('id','name')  #要显示的字段
@admin.register(Blogwenzhang)
class BlogwenzhangAdmin(admin.ModelAdmin):
    list_display = ('id','title','img','release_time','author','classify','amend_time')

@admin.register(Recommended)
class RecommendedAdmin(admin.ModelAdmin):
    list_display = ('id','title','content')

@admin.register(IMG)
class IMGAdmin(admin.ModelAdmin):
    list_display = ('id','img','name',"get_id")

    #添加个自定义的列表按钮
    def get_id(self,obj):
        #这里的obj就是这个模型的一条数据对象，如果你有10条数据，这个方法就要执行10次
        get_pk = int(obj.pk)   #获取这个队列的pk
        mm = int(obj.number)
        if mm == 0:
            return  mark_safe("""<a href="/seav/?pk=%s">点我上传</a>""" % get_pk)
        else:
            return  mark_safe("""<p>上传成功 </p> """)

    get_id.short_description = "同步数据到七牛云"
    get_id.allow_tags = True  #允F许这个函数return返回的时候支持html


@admin.register(Lunbotu)
class LunbotuAdmin(admin.ModelAdmin):
    list_display = ('id','index_img','name',"get_id")

    # 添加个自定义的列表按钮
    def get_id(self, obj):
        # 这里的obj就是这个模型的一条数据对象，如果你有10条数据，这个方法就要执行10次
        get_pk = int(obj.pk)  # 获取这个队列的pk
        mm = int(obj.number)
        if mm == 0:
            return mark_safe("""<a href="/lunbotu/?pk=%s">点我上传</a>""" % get_pk)
        else:
            return mark_safe("""<p>上传成功 </p> """)
    get_id.short_description = "同步数据到七牛云"
    get_id.allow_tags = True  # 允F许这个函数return返回的时候支持html


@admin.register(Guanggaoimg)
class GuanggaoimgAdmin(admin.ModelAdmin):
    list_display = ('id','guanggao_img','name')

@admin.register(Good_url)
class GoodurlAdmin(admin.ModelAdmin):
    list_display = ('id','name','gurl','miaosu')

@admin.register(User_EX)
class User_EXAdmin(admin.ModelAdmin):
    list_display = ('id','user','avatar','bj')

@admin.register(Pinlun)
class PinlunAdmin(admin.ModelAdmin):
    list_display = ('id','user','wenzhang','time','content')