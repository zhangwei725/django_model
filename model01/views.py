from django.http import HttpResponse
from django.shortcuts import render

from model01.models import User


def index(request):
    user = User(email='1223', username='娇娇', password='123', phone='123')
    user.save()
    return HttpResponse('增加')
