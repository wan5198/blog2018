#后台管理管理模型
from django.contrib import admin
from .models import ClassRoomModel,TeacherModel,ParentsModel,StudentModel,ResultModel,KemuModel
from django.template.defaultfilters import mark_safe


# Register your models here.
@admin.register(ClassRoomModel)  #用装饰器注册
class ClassRoomModelAdmin(admin.ModelAdmin): #要显示的字段
    list_display = ('id','name','time')  #要显示的字段

@admin.register(TeacherModel)  #用装饰器注册
class TeacherModelAdmin(admin.ModelAdmin): #要显示的字段
    list_display = ('id','name','time','subject')  #要显示的字段

@admin.register(ParentsModel)
class ParentsModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'time')  # 要显示的字段

@admin.register(StudentModel)
class StudentModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'time', 'parents','class_room')  # 要显示的字段

@admin.register(ResultModel)
class ResultModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'yuwen', 'shuxue', 'yingyu','wuli','huaxue','dili','shengwu','lishi','zhengzhi','tiyu','qimo','kemu','student')  # 要显示的字段

@admin.register(KemuModel)
class StudentModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'time')  # 要显示的字段