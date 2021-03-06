from django import forms
from django.forms import fields, widgets


class FM(forms.Form):
    username = fields.CharField(
        required=True,
        error_messages={"required": '用户名不能为空'},
        widget=widgets.TextInput(attrs={'placeholder':'请输入用户名'})
    )
    passwd = fields.CharField(
        required=True,
        max_length=20,
        min_length=6,
        error_messages={'min_length':'密码长度不能小于6', 'max_length':'密码长度不能大于20', 'required':'密码不能为空'},
        widget=widgets.PasswordInput(attrs={'placeholder':'请输入密码'})
    )


class Host(forms.Form):
    ip = fields.GenericIPAddressField(
        required=True,
        error_messages={"required": 'IP不能为空'},
        widget=widgets.TextInput(attrs={'placeholder': "请输入IP"})
    )
    hostname = fields.CharField(
        required=True,
        max_length=20,
        min_length=3,
        error_messages={'min_length':'密码长度不能小于6', 'max_length':'密码长度不能大于20', 'required':'密码不能为空'},
        widget=widgets.TextInput(attrs={'placeholder': '请输入主机名'})
    )
    port = fields.IntegerField(
        required=True,
        error_messages={'required': '端口号必填'},
        widget=widgets.TextInput(attrs={'placeholder': '请输入端口号'})
    )
