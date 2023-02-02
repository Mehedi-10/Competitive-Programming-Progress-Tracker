from django.shortcuts import render
import calendar
import datetime
from .get_date import fun
from .get_info import get_info

def home(request):
    return render(request,'home.html')

def contestant(request):
    info=get_info('m-e-h-e-d-i','matrix','mehedi10','mehedihasanarafat','matrix33')
    print(info)
    return render(request,'contestants.html')

def calender(request):
    dis=['Sun','Mon','Tue','Wed','Thu','Fri','Sat']
    now = datetime.datetime.now()
    day_cnt=calendar.monthrange(now.year, now.month)[1]
    date=[i for i in range(1,int(day_cnt)+1)]
    contest_date=fun()
    return render(request,'calender.html',{'day':dis,'dat':date,'current_month':calendar.month_name[now.month]+' '+str(now.year),'contest':contest_date})

def teams(request):
    return render(request,'teams.html')

