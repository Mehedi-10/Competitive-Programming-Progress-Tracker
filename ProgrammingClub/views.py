from django.shortcuts import render
import calendar
import datetime
from .models import contestant as cnts_model
from .get_date import fun
from .get_info import get_info
import requests
from bs4 import BeautifulSoup
from lxml import etree

def home(request):
    return render(request,'home.html')

def contestant(request):
    all_contestant={}

    for i in cnts_model.objects.all():
        tmp={i.sid:get_info(i.sid)}
        all_contestant.update(tmp)
    print(all_contestant)
    return render(request,'contestants.html',{'contestant':all_contestant})

def calender(request):
    dis=['Sun','Mon','Tue','Wed','Thu','Fri','Sat']
    now = datetime.datetime.now()
    day_cnt=calendar.monthrange(now.year, now.month)[1]
    date=[i for i in range(1,int(day_cnt)+1)]
    contest_date=fun()
    return render(request,'calender.html',{'day':dis,'dat':date,'current_month':calendar.month_name[now.month]+' '+str(now.year),'contest':contest_date})

def teams(request):
    return render(request,'teams.html')

