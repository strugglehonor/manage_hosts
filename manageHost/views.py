from django.shortcuts import render,redirect,reverse,HttpResponse
from django.views import View
from . import form, models
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator, EmptyPage
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


@auth
def host(request):
    username = request.session.get('user')
    user = models.User.objects.filter(username=username).first()
    ############ 未实现分页效果，开始批量创建主机，并且批量绑定多对多关系
    # # 批量插入数据
    # business = models.Business.objects.get(id=1)
    # hosts_list = []
    # for i in range(100, 201):
    #     host = models.Host(
    #         ip='10.10.10.%s'%(str(i)),
    #         user=user,
    #         hostname='DB%s'%(str(i-99)),
    #         b=business,
    #         port=80,
    #     )
    #     # host.application.add(3)  # 这句代码可能错，因为host没有创建
    #     hosts_list.append(host)
    # print(hosts_list)
    # models.Host.objects.bulk_create(hosts_list)
    # # 批量绑定多对多关系
    # host_list = models.Host.objects.all()
    # for host in host_list:
    #     host.application.add(3)
    host_list = models.Host.objects.filter(user_id=user.id)
    # 设置每页显示10条数据
    paginator = Paginator(host_list, 10)
    # 从前端获取current_page
    try:
        current_page = int(request.GET.get('page', 1))
        page = paginator.page(current_page)
        if paginator.num_pages > 10:
            # 设置页面的分页块超过10个
            if current_page - 5 < 1:
                page_range = range(1, 11)
            elif current_page +5 > paginator.num_pages:
                page_range = range(paginator.num_pages-10, paginator.num_pages+1)
            else:
                page_range = range(current_page-5, current_page+5)
        else:
            page_range = paginator.page_range
    except EmptyPage:
        current_page = 1
    obj = form.Host
    application_list = models.Application.objects.all()
    business_list = models.Business.objects.all()
    return render(request, 'host.html', locals())


method_decorator(auth, name='dispatch')
class addHost(View):
    def get(self, request):
        return redirect('/host/')
    def post(self, request, *args, **kwargs):
        hostname = request.POST.get('hostname')
        ip =request.POST.get('ip')
        port = request.POST.get('port')
        b_id = request.POST.get('business')
        # 使用get_or_create就可以不用重复创建了，因为business就只有运维部和开发部
        business, is_get = models.Business.objects.get_or_create(id=b_id) # 这里有问题
        application = request.POST.getlist('application')
        user = request.session.get('user')
        user = models.User.objects.filter(username=user).first()
        host = models.Host.objects.create(hostname=hostname, ip=ip, port=port, b=business, user=user)
        # 使用related_name字段来绑定多对多关系
        host.application.add(*application)
        return redirect('/host/')


class EditHost(View):
    def get(self, request, nid):
        machine = models.Host.objects.filter(nid=nid).first()
        application_list = models.Application.objects.all()
        business_list = models.Business.objects.all()
        return render(request, 'edit.html', locals())

    def post(self, request, nid):
        ip = request.POST.get('ip')
        port = request.POST.get('port')
        b_id = request.POST.get('business')
        hostname = request.POST.get('hostname')
        app_id = request.POST.getlist('application')
        """
        注意，这里不能用get筛选数据库记录，因为updateupdate是QuerySet对象的方法，get返回的是一个model对象
        """
        machine = models.Host.objects.filter(nid=nid).update(
            ip=ip,
            port=port,
            hostname=hostname,
            b_id = b_id,
        )
        print(machine)
        machine = models.Host.objects.filter(nid=nid).first()
        machine.application.set(app_id)
        return redirect('/host/')


def detail(request, nid):
    print(type(nid))
    machine = models.Host.objects.filter(nid=nid).first()
    print(machine)
    return render(request, 'detail.html', locals())


def delHost(request, nid):
    models.Host.objects.filter(nid=nid).delete()
    return redirect('/host/')
