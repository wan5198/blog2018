from django import forms
from django.contrib import auth
from django.contrib.auth.models import User
from captcha.fields import CaptchaField #引入验证码验证模块
class LoginFrom(forms.Form):
    username = forms.CharField(label='用户名',widget=forms.TextInput(attrs={"class":"form-control",'placeholder':'请输入用户名'}))
                                             # widget=forms.TextInput 样式
    password = forms.CharField(label='密码',widget=forms.PasswordInput(attrs={"class":"form-control",'placeholder':'请输入密码'}))
    # captcha = CaptchaField(label='验证码',widget=forms.TextInput(attrs={"class":"form-control",'placeholder':'请输入验证码'}))  # 验证验证码
    captcha = CaptchaField(label='验证码')  # 验证验证码
    #attrs=可以传递一些参数进去，比如CSS类
    def clean(self):#调用这个内置方法：
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        user = auth.authenticate( username=username, password=password)  # 去用户模型里比对
        if user is  None:  # 如果查不到，就会返回一个空值
            raise forms.ValidationError('用户名或密码错误')
        else: #验证如果通过，就把用户写进去
            self.cleaned_data['user'] = user
        return self.cleaned_data

#用户注册表单验证
class RegForm(forms.Form):
    username = forms.CharField(label='用户名',min_length=3,max_length=20,
                               widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': '请输入用户名'}))
    # widget=forms.TextInput 样式
    password1 = forms.CharField(label='密码',min_length=6,max_length=20,
                               widget=forms.PasswordInput(attrs={"class": "form-control", 'placeholder': '请输入密码'}))
    # attrs=可以传递一些参数进去，比如CSS类
    password2 = forms.CharField(label='密码',min_length=6,max_length=20,
                               widget=forms.PasswordInput(attrs={"class": "form-control", 'placeholder': '请再次输入密码'}))
    # attrs=可以传递一些参数进去，比如CSS类
    email = forms.CharField(label='email',
                               widget=forms.EmailInput(attrs={"class": "form-control", 'placeholder': '请输入邮箱'}))
    # attrs=可以传递一些参数进去，比如CSS类
    captcha = CaptchaField(label='验证码')  # 验证验证码
    def clean_username(self):
        username = self.cleaned_data['username']
        #验证用户名是否已经存在
        user = User.objects.filter(username=username).exists() #.exists()方法判断存在就返回True
        if user:
            raise forms.ValidationError("用户名已经存在！")
        return username

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        # 验证两次密码是否已经存在
        if password1 != password2 :
            raise forms.ValidationError("两次密码输入不一样！请核对重新输入。")
        return password2
    def clean_email(self):
        email = self.cleaned_data['email']
        #验证邮箱是否已经存在
        user_emali = User.objects.filter(email=email).exists() #.exists()方法判断存在就返回True
        if user_emali:
            raise forms.ValidationError("邮箱已经存在！")
        return email
