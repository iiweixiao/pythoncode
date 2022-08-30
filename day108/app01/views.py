import json
from django.shortcuts import render, HttpResponse, redirect
from django.forms import ModelForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from app01.models import UpInfo, VideoInfo, UpVideoList, HeJi, AjaxForm

from utils.bili_up import parse_mid
from utils.bilibili import mid_data
from utils.bili_heji import parse
from utils.pagination import Pagination


def index(request):
    # mid = '15960317'
    # name = parse_mid(mid)
    # if not UpInfo.objects.filter(mid=mid).exists():
    #     UpInfo.objects.create(mid=mid, name=name)
    # queryset = VideoInfo.objects.all()
    #
    # return render(request, 'index.html', {'queryset': queryset})
    return redirect('/video/list/')


def test(request):
    return render(request, 'test.html')


class ModelFormEdit(ModelForm):
    class Meta:
        model = UpInfo
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs = {'class': 'form-control', 'placeholder': field.label}


def up_edit(request, nid):
    row_object = UpInfo.objects.filter(id=nid).first()
    if request.method == 'GET':
        form = ModelFormEdit(instance=row_object)
        return render(request, 'up_edit.html', {'form': form})

    form = ModelFormEdit(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/up/list')
    return render(request, 'up_edit.html', {'form': form})


def up_delete(request, nid):
    UpInfo.objects.filter(id=nid).delete()
    return redirect('/up/list')


def up_list(request):
    if request.method == 'GET':
        queryset = UpInfo.objects.all()
        return render(request, 'up_list.html', {'queryset': queryset})

    mid = request.POST.get('mid')
    if not UpInfo.objects.filter(mid=mid).exists():
        name = parse_mid(mid)
        UpInfo.objects.create(mid=mid, name=name)
    queryset = UpInfo.objects.all()
    return render(request, 'up_list.html', {'queryset': queryset})


class VideoModelForm(ModelForm):
    class Meta:
        model = VideoInfo
        fields = '__all__'


def video_list(request):
    queryset = VideoInfo.objects.all().order_by('-created')
    page_object = Pagination(request, queryset)
    form = VideoModelForm()

    context = {
        'queryset': page_object.page_queryset,
        'form': form,
        'page_string': page_object.html()
    }
    return render(request, 'video_list.html', context)


def refresh(request):
    # 获取up主的mid列表
    queryset = UpInfo.objects.all()
    up_ids = []
    for obj in queryset:
        up_ids.append(obj.mid)

    # 对每个mid进行解析，将视频信息添加到数据库中
    queryset1 = VideoInfo.objects.all()
    title_list = []
    for obj in queryset1:
        title_list.append(obj.title)
    for mid in up_ids:
        data = mid_data(mid)
        if data:
            for item in data:
                if item[1] not in title_list:
                    VideoInfo.objects.create(name=item[0], title=item[1], href=item[2], created=item[3], status=0)
                else:
                    break

    return redirect('/video/list')


def heji(request):
    if request.method == 'GET':
        return render(request, 'heji.html')

    # url = 'https://www.bilibili.com/video/BV1C94y1X75h/?spm_id_from=333.788'
    # url = 'https://www.bilibili.com/video/BV1XL4y1L71X?spm_id_from=333.337.search-card.all.click&vd_source=e7ed50c0d7d2387c7423c27fa17f7af5'
    HeJi.objects.all().delete()
    url = request.POST.get('url')
    # if url:
    #     print(url)
    #     return HttpResponse('ok')
    print(url)

    try:
        content_list = parse(url)
    except:
        HttpResponse('url有误！')

    for index, item in enumerate(content_list):
        HeJi.objects.create(index=index + 1, title=item[0], href=item[1], created=item[2])

    queryset = HeJi.objects.all()

    return render(request, 'heji.html', {'queryset': queryset})


def up_video_list(request):
    return render(request, 'up_video_list.html')


class AjaxModelForm(ModelForm):
    class Meta:
        model = AjaxForm
        fields = '__all__'


def test_ajax(request):
    # print(request.GET)
    # return HttpResponse('test ajax')
    form = AjaxModelForm()
    return render(request, 'test_ajax.html', {'form': form})


@csrf_exempt
def test_ajax_test(request):
    # print(request.GET)
    print(request.POST)
    # return HttpResponse('成功了')

    # 将data_dict数据传到前端
    data_dict = {"status": True, "data": [11, 22, 33, 44]}

    # (import json)
    # json_string = json.dumps(data_dict)  # 字典或列表类型可以进行dumps
    # return HttpResponse(json_string)

    # (from django.http import JsonResponse)
    # return JsonResponse(data_dict)

    return HttpResponse(JsonResponse(data_dict))


@csrf_exempt
def ajax_form(request):
    print(request.POST)

    form = AjaxModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        data_dict = {"status": True}
        return HttpResponse(json.dumps(data_dict))
    data_dict = {"status": True}
    return HttpResponse(json.dumps(data_dict))
