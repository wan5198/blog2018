from django.db import models
from django.contrib.auth.models import User #映入系统自带的用户模型
from ckeditor_uploader.fields import RichTextUploadingField #导入富文本模块

#分类模型
class Classify(models.Model):
    name = models.CharField(max_length=100,null=False)
    def __str__(self):
        return self.name
    class Meta:  #后台管理显示汉字，这里必须用Meta
        verbose_name = '文章分类'
        verbose_name_plural = verbose_name   # verbose_name_plural 系统内置不能改用其他
#图片模型 参考文章：https://www.cnblogs.com/14061216chen/p/6537864.html
class IMG(models.Model):
    img = models.ImageField(upload_to='img',verbose_name='上传图片')
    name = models.CharField(max_length=20,verbose_name='图片名字')
    number = models.IntegerField(default=0)
    def __str__(self):
        return self.name
    #这里的upload_to是指定图片存储的文件夹名称，上传文件之后会自动创建
    class Meta:  #后台管理显示汉字，这里必须用Meta装一些父类的设置
        verbose_name = '图片上传'
        verbose_name_plural = verbose_name   # verbose_name_plural 系统内置不能改用其他


#文章模型
class Blogwenzhang(models.Model):
    title = models.CharField(max_length=100,null=False,verbose_name='文章标题')
    content = RichTextUploadingField (null=False,verbose_name='文章内容')
    release_time = models.DateTimeField(auto_now_add=True,verbose_name='加入时间')  #auto_now_add=True 保存为加入文章时的时间
    amend_time = models.DateTimeField(auto_now=True,verbose_name='最后修改') #auto_now=True 修改完成提交的时间
    author = models.ForeignKey(User,on_delete=models.DO_NOTHING,verbose_name='作者') #外键关联，关联的是User模型，on_delete=models.DO_NOTHING 表示不能级联删除
    classify = models.ForeignKey(Classify,on_delete=models.DO_NOTHING,verbose_name='文章分类')
    reads = models.IntegerField(default=0)
    img = models.ForeignKey(IMG,on_delete=models.DO_NOTHING,verbose_name='图片名字',null=True)

    class Meta:  #后台管理显示汉字，这里必须用Meta装一些父类的设置
        verbose_name = '博文发布'
        verbose_name_plural = verbose_name   # verbose_name_plural 系统内置不能改用其他
        ordering = [ '-release_time']  #ordering 内置排序的方法，中括号里指定排序发布时间倒叙



#推荐模型
class Recommended(models.Model):
    title = models.CharField(max_length=100,null=False,verbose_name='置顶标题')
    content = models.TextField(null=False,verbose_name='内容')
    class Meta:  #后台管理显示汉字，这里必须用Meta
        verbose_name = '置顶消息'
        verbose_name_plural = verbose_name   # verbose_name_plural 系统内置不能改用其他
#评论模型
class Pinlun(models.Model):
    content = models.TextField(null=False,verbose_name='评论内容')
    author = models.CharField(max_length=50,verbose_name='评论人')
    time = models.DateTimeField(auto_now_add=True,verbose_name='评论时间')
    email = models.CharField(max_length=50)
    wenzhang = models.ForeignKey(Blogwenzhang, on_delete=models.DO_NOTHING, verbose_name='评论关联')
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='评论关联')

    class Meta:
        ordering = ['-time']  # ordering 内置排序的方法，中括号里指定排序发布时间倒叙
        verbose_name = '评论管理'
        verbose_name_plural = verbose_name  # verbose_name_plural 系统内置不能改用其他g

#轮播图模型
class Lunbotu(models.Model):
    name = models.CharField(max_length=100,null=False,verbose_name='图片名字')
    index_img = models.ImageField(upload_to='index_img',verbose_name='上传图片')
    number = models.IntegerField(default=0)
    class Meta:
        verbose_name = '轮播图管理'
        verbose_name_plural = verbose_name  # verbose_name_plural 系统内置不能改用其他

#广告图模型
class Guanggaoimg(models.Model):
    name = models.CharField(max_length=100,null=False,verbose_name='图片名字')
    guanggao_img = models.ImageField(upload_to='index_img',verbose_name='上传图片')

    class Meta:
        verbose_name = '广告图管理'
        verbose_name_plural = verbose_name  # verbose_name_plural 系统内置不能改用其他g

#友情链接模块
class Good_url(models.Model):
    name = models.CharField(max_length=100,null=False,verbose_name='网站名字')
    gurl = models.CharField(max_length=100,null=False,verbose_name='跳转网址')
    miaosu = models.CharField(max_length=200,null=False,verbose_name="描述说明")

    class Meta:
        verbose_name = '友情链接管理'
        verbose_name_plural = verbose_name  # verbose_name_plural 系统内置不能改用其他g
AVATAR_ROOT='static/avatar'
#一对一关联User
class User_EX(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    avatar=models.ImageField(upload_to=AVATAR_ROOT,default='static/avatar/moren.jpg')
    bj=models.CharField(max_length=15,default='blog_2018')

    class Meta:
        verbose_name = '用户头像管理'
        verbose_name_plural = verbose_name  # verbose_name_plural 系统内置不能改用其他g

class DianzanModel(models.Model):
    wenzhang_id = models.IntegerField(verbose_name='被点文字ID')
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='点赞人ID')
    zan_num = models.IntegerField(verbose_name='点赞数量')