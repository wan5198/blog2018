from django.db import models

#教师
class TeacherModel(models.Model):
    name = models.CharField(max_length=100,verbose_name='老师名字')
    subject = models.CharField(max_length=50, verbose_name='教学科目')
    time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    def __str__(self):
        return "%s" % self.name
    class Meta:  # 后台管理显示汉字，这里必须用Meta
        verbose_name = '教师管理'
        verbose_name_plural = verbose_name  # verbose_name_plural 系统内置不能改用其他
#班级
class ClassRoomModel(models.Model):
    name = models.CharField(max_length=100,verbose_name='班级名称')
    time = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')

    def __str__(self):
        return "%s" % self.name
    class Meta:  # 后台管理显示汉字，这里必须用Meta
        verbose_name = '班级管理'
        verbose_name_plural = verbose_name  # verbose_name_plural 系统内置不能改用其他
#家长
class ParentsModel(models.Model):
    name = models.CharField(max_length=100, verbose_name='家长名字')
    time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __str__(self):
        return "%s" % self.name
    class Meta:  # 后台管理显示汉字，这里必须用Meta
        verbose_name = '家长管理'
        verbose_name_plural = verbose_name  # verbose_name_plural 系统内置不能改用其他


#学生
class StudentModel(models.Model):
    name = models.CharField(max_length=100,verbose_name='学生名字')
    time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    parents = models.ForeignKey(ParentsModel,on_delete=models.DO_NOTHING,verbose_name='父/母名称')
    class_room = models.OneToOneField(ClassRoomModel,on_delete=models.CASCADE,verbose_name='所属班级')
    def __str__(self):
        return "%s" % self.name
    class Meta:  # 后台管理显示汉字，这里必须用Meta
        verbose_name = '学生管理'
        verbose_name_plural = verbose_name  # verbose_name_plural 系统内置不能改用其他
#成绩类型
class KemuModel(models.Model):
    name = models.CharField(max_length=100, verbose_name='成绩类型')
    time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    def __str__(self):
        return "%s" % self.name
    class Meta:  # 后台管理显示汉字，这里必须用Meta
        verbose_name = '成绩类型管理'
        verbose_name_plural = verbose_name  # verbose_name_plural 系统内置不能改用其他
#成绩
class ResultModel(models.Model):
    yuwen = models.IntegerField(null=True,verbose_name='语文成绩')
    shuxue = models.IntegerField(null=True,verbose_name='数学成绩')
    yingyu = models.IntegerField(null=True,verbose_name='英语成绩')
    wuli = models.IntegerField(null=True,verbose_name='物理成绩')
    huaxue = models.IntegerField(null=True,verbose_name='化学成绩')
    dili = models.IntegerField(null=True,verbose_name='地理成绩')
    shengwu = models.IntegerField(null=True,verbose_name='生物成绩')
    lishi = models.IntegerField(null=True,verbose_name='历史成绩')
    zhengzhi = models.IntegerField(null=True,verbose_name='政治成绩')
    tiyu = models.IntegerField(null=True,verbose_name='体育成绩')
    qimo = models.IntegerField(null=True,verbose_name='期末成绩')
    kemu = models.OneToOneField(KemuModel,on_delete=models.CASCADE,verbose_name='成绩类别')
    student= models.OneToOneField(StudentModel,on_delete=models.CASCADE,verbose_name='所属学生')

    class Meta:  # 后台管理显示汉字，这里必须用Meta
        verbose_name = '成绩管理'
        verbose_name_plural = verbose_name  # verbose_name_plural 系统内置不能改用其他