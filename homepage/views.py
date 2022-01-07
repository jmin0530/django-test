# -*- coding: utf-8 -*-
from django.shortcuts import HttpResponse,render


# Create your views here.

def index(request):
#     return HttpResponse("Hello World!") # request가 왔을 때 "Hello World! 출력"
    nums = [1,2,3,4,5]
    return render(request, 'index.html', {"my_list": nums})


def my_intro(request):
#     return HttpResponse("Hello World!") # request가 왔을 때 "Hello World! 출력"
    return render(request, 'myintro.html', {})
