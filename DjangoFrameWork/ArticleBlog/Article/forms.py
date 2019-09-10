from django import forms


class Register(forms.Form):
    username=forms.CharField(label='用户名',required=True,error_messages={"required":"用户名不能为空"})
    password=forms.CharField(min_length=6,max_length=32,label='密码',widget=forms.PasswordInput,initial="hello world")
    email=forms.EmailField()
    def clean_username(self):
        #自定义校验函数的名字是固定的
        username=self.cleaned_data.get('username')
        if username=='admin':
            self.add_error('username',"用户名不可以是：%s"%username)
        else:
            return username