from django.shortcuts import render, HttpResponse, redirect
from app01.models import UserInfo


def init(request):
    UserInfo.objects.create(name='小猫', password='1', age=1)
    UserInfo.objects.create(name='小狗', password='2', age=2)
    return HttpResponse('初始化数据成功！')


def info_list(request):
    user_info = UserInfo.objects.all()
    return render(request, 'info_list.html', {'user_info': user_info})


def add_user(request):
    if request.method == 'GET':
        return render(request, 'add_user.html')
    name = request.POST.get('name')
    password = request.POST.get('password')
    age = request.POST.get('age')
    UserInfo.objects.create(name=name, password=password, age=age)
    return redirect('/add/user')


# from app01.models import UserInfo
from django.forms import ModelForm

class ModelFormInfo(ModelForm):
    class Meta:
        model = UserInfo
        fields = ['name', 'password', 'age']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {'class': 'form-control', 'placeholder': field.label}

def modelform_add_user(request):
    if request.method == 'GET':
        form = ModelFormInfo()
        return render(request, 'modelform_add_user.html', {'form': form})
    form = ModelFormInfo(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/info/list')
    return render(request, 'modelform_add_user.html', {'form': form})


def delete_user(request):
    nid = request.GET.get('nid')
    UserInfo.objects.filter(id=nid).delete()
    return redirect('/info/list')
    # return HttpResponse('删除成功')


def edit_user(request, nid):
    if request.method == 'GET':
        data = UserInfo.objects.filter(id=nid).first()
        return render(request, 'edit_user.html', {'data': data})

    name = request.POST.get('name')
    password = request.POST.get('password')
    age = request.POST.get('age')
    UserInfo.objects.filter(id=nid).update(name=name, password=password, age=age)
    return redirect('/info/list')
