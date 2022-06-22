from django.shortcuts import render, HttpResponse, redirect


def index(request):
    return HttpResponse("欢迎使用")

def list(request):
    return render(request, 'user_list.html')

def add(request):
    return HttpResponse("欢迎使用add")

def news(request):
    import requests
    res = requests.get('https://sspai.com/api/v1/article/tag/page/get?limit=10&offset=0&created_at=1653492566&tag=%E7%94%9F%E6%B4%BB%E6%96%B9%E5%BC%8F&search_type=1')
    data_list = res.json()
    print(data_list)

    return render(request, 'news.html', {"news_list": data_list['data']})

def login(request):
    # GET请求
    if request.method == "GET":
        return render(request, "login.html")
        # POST请求
    else:
        username = request.POST.get('user')
        password = request.POST.get('pwd')
        if username == 'root' and password == '123':
            return redirect('https://sspai.com/')
        else:
            return render(request, 'login.html', {'error_msg': '用户名或密码错误'})
