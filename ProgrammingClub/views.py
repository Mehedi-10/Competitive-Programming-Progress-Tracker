import random

from django.shortcuts import render
import calendar
import datetime
from .models import contestant as cnts_model
from .models import teams as team_model
from .get_date import fun
from .get_info import get_info,get_rating
from .national_contests import synapse

def home(request):
    now = datetime.datetime.now()
    all={
        'dept':get_rating()[0],
        'university':get_rating()[1],
        'unirank':synapse(),
    }
    for i in cnts_model.objects.all():
        print(i.sid)
    all['unirank']=str(all['unirank'][0]).split(' ')
    try:
        contest_date = list(fun().values())[0][0]
    except:
        contest_date={'date': 'unknown', 'event': 'No Contest'}
    upcoming=(contest_date['event'],str(contest_date['date'])+", "+calendar.month_name[now.month]+' '+str(now.year))

    return render(request,'home.html',{'all_data':all,'uni_rank':all['unirank'],'upcoming':upcoming,'contestant':[len(all['dept'])]})

def contestant(request):
    all_contestant={}
    li=['vecteezy_champ.jpg','vecteezy_programmer.jpg','Studying.jpg']
    for i in cnts_model.objects.all():
        tmp={i.sid:get_info(i.sid)}
        all_contestant.update(tmp)
    data=get_rating()[0]
    sort_data=[]
    for i in data:
        sort_data.append((i[0],i[1]))

    return render(request,'contestants.html',{'contestant':all_contestant,'pic':li,'sorted_list':sort_data})

def calender(request):
    dis=['Sun','Mon','Tue','Wed','Thu','Fri','Sat']
    now = datetime.datetime.now()
    day_cnt=calendar.monthrange(now.year, now.month)[1]
    date=[i for i in range(1,int(day_cnt)+1)]
    contest_date=fun()
    return render(request,'calender.html',{'day':dis,'dat':date,'current_month':calendar.month_name[now.month]+' '+str(now.year),'contest':contest_date})

def teams(request,team_name):
    li=['vecteezy_champ.jpg','vecteezy_programmer.jpg','Studying.jpg']
    team_data={}
    for i in team_model.objects.all():
        team_data.update({i.id:{'name':i.team_name,'members':[i.member1.sid,i.member2.sid,i.member3.sid]}})
    try:
        team_name=int(team_name)
        all_data = {
            'img':li,
            'team': {team_name:team_data[team_name]}
        }
    except:
        all_data={}
    return render(request,'teams.html',{'all_data':all_data})

def teamlist(request):
    team_data = {}
    for i in team_model.objects.all():
        team_data.update({i.id: {'name': i.team_name, 'members': [i.member1.sid, i.member2.sid, i.member3.sid]}})
    all_data = {
        'team': team_data
    }
    return render(request,'teamlist.html',{'all_data':all_data})
