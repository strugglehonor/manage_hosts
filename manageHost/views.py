from django.shortcuts import render,redirect,reverse,HttpResponse
from django.views import View
from . import form, models
from django.utils.decorators import method_decorator
# Create your views here.


def auth(func):
    def wrapper(request, *args, **kwargs):
        is_login = request.session.get('is_login')
        if not is_login:
            return redirect('/login/')
        print('auth is called')
        return func(request, *args, **kwargs)
    return wrapper


class Login(View):
    def get(self, request):
        obj = form.FM()
        return render(request, 'login.html', {"obj":obj})

    def post(self, request):
        obj = form.FM(request.POST)
        if obj.is_valid():
        # 如果用户名，密码格式正确，开始验证
            print(obj.cleaned_data)
            user = models.User.objects.filter(**obj.cleaned_data).first()
            if user:
                # 用户名密码输入正确
                print(user.username)
                # 设置session
                request.session['is_login'] = True
                request.session['user'] =  user.username
                return redirect('/host/')
            else:
                # 验证失败，就给增加一个错
                error = '用户名或者密码错误'
                return render(request, 'login.html', {'error': error, 'obj': obj})
        else:
            error = '用户名或者密码格式错误'
            return render(request, 'login.html', {'obj': obj, 'error':error})


class Register(View):
    def get(self, request):
        obj = form.FM()
        return render(request, 'register.html', {'obj': obj})
    def post(self, request):
        obj = form.FM(request.POST)
        if obj.is_valid():
            new_user = models.User.objects.create(**obj.cleaned_data)
            return render(request, 'register.html', {'obj': obj, 'new_user': new_user})
        else:
            error = '用户名或者密码错误'
            return render(request, 'register.html', {'error': error})

#
# @method_decorator(auth, name="dispatch")    # 如果没有登录就回到登录页面
# class Host(View):
#     def get(self, request, *args, **kwargs):
#         print('1')
#         username = request.session.get('user')
#         user = models.User.objects.filter(username=username).first()
#         obj = form.FM()
#         return render(request, 'host.html', {"user": user, 'obj': obj})
@auth
def host(request):
    username = request.session.get('user')
    user = models.User.objects.filter(username=username).first()
    # # 批量插入数据
    # business = models.Business.objects.create(b_name='DB')
    # hosts_list = []
    # for i in range(100, 201):
    #     host = models.Host()
    obj = form.Host
    return render(request, 'host.html', {"user": user, 'obj': obj})

def delHost(request, nid):
    models.Host.objects.filter(nid=nid).delete()
    return redirect('/host/')

method_decorator(auth, name='dispatch')
class addHost(View):
    def get(self, request):
        return redirect('/host/')
    def post(self, request):
        hostname = request.POST.get('hostname')
        ip =request.POST.get('ip')
        port = request.POST.get('port')
        business = request.POST.get('business')
        # 使用get_or_create就可以不用重复创建了，因为business就只有运维部和开发部
        business, is_get = models.Business.objects.get_or_create(b_name=business)
        application_name = request.POST.getlist('application')
        user = request.session.get('user')
        user = models.User.objects.filter(username=user).first()
        host = models.Host.objects.create(hostname=hostname, ip=ip, port=port, b=business, user=user)
        # 使用related_name字段来绑定多对多关系
        host.application.add(*application_name)
        return redirect('/host/')

