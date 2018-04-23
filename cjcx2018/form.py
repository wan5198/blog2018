
from django import forms
from django.contrib import auth
class LoginFrom(forms.Form):
    username = forms.CharField(label='用户名',widget=forms.TextInput(attrs={"class":"form-control",'placeholder':'请输入用户名'}))
                                             # widget=forms.TextInput 样式
    password = forms.CharField(label='密码',widget=forms.PasswordInput(attrs={"class":"form-control",'placeholder':'请输入密码'}))
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