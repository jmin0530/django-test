# -*- coding: utf-8 -*-
from django.shortcuts import HttpResponse,render


# Create your views here.

def index(request):
#     return HttpResponse("Hello World!") # request가 왔을 때 "Hello World! 출력"

    return render(request, 'index.html')


def my_intro(request):
#     return HttpResponse("Hello World!") # request가 왔을 때 "Hello World! 출력"
    return render(request, 'myintro.html', {})
