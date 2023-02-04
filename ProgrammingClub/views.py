from django.shortcuts import render
import calendar
import datetime
from .models import contestant as cnts_model
from .models import teams as team_model
from .get_date import fun
from .get_info import get_info


def home(request):
    return render(request,'home.html')

def contestant(request):
    all_contestant={}
    li=['vecteezy_champ.jpg','vecteezy_programmer.jpg','Studying.jpg']
    for i in cnts_model.objects.all():
        tmp={i.sid:get_info(i.sid)}
        all_contestant.update(tmp)
    print(all_contestant)
    return render(request,'contestants.html',{'contestant':all_contestant,'pic':li})

def calender(request):
    dis=['Sun','Mon','Tue','Wed','Thu','Fri','Sat']
    now = datetime.datetime.now()
    day_cnt=calendar.monthrange(now.year, now.month)[1]
    date=[i for i in range(1,int(day_cnt)+1)]
    contest_date=fun()
    return render(request,'calender.html',{'day':dis,'dat':date,'current_month':calendar.month_name[now.month]+' '+str(now.year),'contest':contest_date})

def teams(request):
    li=['vecteezy_champ.jpg','vecteezy_programmer.jpg','Studying.jpg']

    team_data={}
    for i in team_model.objects.all():
        team_data.update({i.id:{'name':i.team_name,'members':[i.member1.sid,i.member2.sid,i.member3.sid]}})
    all_data={
        'img': li,
        'team':team_data
    }
    print(team_data)
    return render(request,'teams.html',{'all_data':all_data})

