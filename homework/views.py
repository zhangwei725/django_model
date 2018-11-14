from django.shortcuts import render

from model02.models import Goods


def shops(request):
    goods = Goods.objects.all()
    return render(request, 'shops.html', context={'goods': goods})


def emp_list(request):
    return render(request, 'emp_list.html')
