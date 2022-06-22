from django.shortcuts import render, HttpResponse


def index(request):
    return HttpResponse('欢迎使用')