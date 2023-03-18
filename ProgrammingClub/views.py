from ProgrammingClub.middlewares.my_middleware import is_allowed
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render, HttpResponseRedirect
import calendar
import datetime
from .models import contestant as cnts_model, coach
from .models import teams as team_model
from .get_date import fun
from .get_info import get_info, get_rating
from .national_contests import synapse


@is_allowed
def home(request):
    now = datetime.datetime.now()
    try:
        all = {
            'dept': get_rating()[0],
            'university': get_rating()[1],
            'weekly': get_rating()[2],
            'unirank': synapse(),
        }
    except:
        pass

    print('contestant list')
    dept_contestent_cnt = 0;
    for i in cnts_model.objects.all():
        if str(i.sid)[3:5] == '08':
            dept_contestent_cnt += 1
        print(i.sid)
    try:
        all['unirank'] = str(all['unirank'][0]).split(' ')
        contest_date = list(fun().values())[0][0]
    except:
        contest_date = {'date': 'Unknown', 'event': 'No Contest', 'link': '#'}
    upcoming = (
    contest_date['event'], str(contest_date['date']) + ", " + calendar.month_name[now.month] + ' ' + str(now.year),
    contest_date['link'])

    return render(request, 'home.html', {'all_data': all, 'uni_rank': all['unirank'], 'upcoming': upcoming,
                                         'contestant': [dept_contestent_cnt]})


@is_allowed
def contestant(request):
    all_contestant = {}
    li = ['vecteezy_champ.jpg', 'vecteezy_programmer.jpg', 'Studying.jpg']
    try:
        for i in cnts_model.objects.all():
            tmp = {i.sid: get_info(i.sid, False)}
            all_contestant.update(tmp)
        data = get_rating()[0]
        sort_data = []
        for i in data:
            sort_data.append((i[0], i[1]))
    except:
        pass
    for i in all_contestant.items():
        print(i)

    return render(request, 'contestants.html', {'contestant': all_contestant, 'pic': li, 'sorted_list': sort_data})


@is_allowed
def calender(request):
    dis = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    now = datetime.datetime.now()
    day_cnt = calendar.monthrange(now.year, now.month)[1]
    date = [i for i in range(1, int(day_cnt) + 1)]
    contest_date = fun()
    return render(request, 'calender.html',
                  {'day': dis, 'dat': date, 'current_month': calendar.month_name[now.month] + ' ' + str(now.year),
                   'contest': contest_date})


def teams(request, team_name):
    if not request.session['user_type']:
        return HttpResponseRedirect('signin')
    li = ['vecteezy_champ.jpg', 'vecteezy_programmer.jpg', 'Studying.jpg']
    team_data = {}
    for i in team_model.objects.all():
        team_data.update({i.id: {'name': i.team_name, 'members': [i.member1.sid, i.member2.sid, i.member3.sid]}})
    try:
        team_name = int(team_name)
        all_data = {
            'img': li,
            'team': {team_name: team_data[team_name]},
            'name': team_data[team_name]['name']
        }
    except:
        all_data = {}
    return render(request, 'teams.html', {'all_data': all_data})


@is_allowed
def teamlist(request):
    team_data = {}
    try:

        for i in team_model.objects.all():
            team_data.update({i.id: {'name': i.team_name, 'members': [i.member1.sid, i.member2.sid, i.member3.sid]}})
        all_data = {
            'team': team_data
        }
    except:
        pass

    return render(request, 'teamlist.html', {'all_data': all_data})


def signup(request):
    if request.method == 'POST':
        data = request.POST
        try:
            if data.get('password') != data.get('repassword'):
                messages.error(request, "Password does not matches.")
            else:
                if cnts_model.objects.get(sid=data.get('id')):
                    messages.error(request, "Already have an account.")
                else:
                    ob = cnts_model(
                        sid=data['sid'],
                        sname=data['name'],
                        user_email=data['email'],
                        password=make_password(request.POST.get('password1'))
                    )
                    ob.save()
                    return HttpResponseRedirect('signin')
        except:
            messages.error(request, "Try again properly.")

    return render(request, 'signup.html')


def signin(request):
    if request.method == 'POST':
        data = request.POST
        try:
            cnts = cnts_model.objects.filter(user_email=data.get('email')).last()
            if not check_password(data['password'], cnts.password):
                request.session['user_type'] = 'contestant'
                request.session['id'] = cnts.sid
                if 'remember' in data:
                    request.session.set_expiry(30 * 24 * 60 * 60)  # 30 days in seconds
                return HttpResponseRedirect('/')
            coch = coach.objects.get(coach_email=data['email'])
            if check_password(data['password'], coch.password):
                request.session['user_type'] = 'coach'
                request.session['email'] = coch.coach_email
                if 'remember' in data:
                    request.session.set_expiry(30 * 24 * 60 * 60)  # 30 days in seconds
                return HttpResponseRedirect('/')
        except:
            messages.error(request, "Try again properly.")

    return render(request, 'signin.html')


@is_allowed
def settings(request):
    if request.method == 'GET':
        if request.session['user_type'] == 'contestant':
            user_data = cnts_model.objects.get(sid=request.session['id'])
            all_data = {
                'sid': user_data.sid,
                'sname': user_data.sname,
                'toph_handle': user_data.toph_handle,
                'cf_handle': user_data.cf_handle,
                'cc_handle': user_data.cc_handle,
                'atcoder_handle': user_data.atcoder_handle,
                'loj_handle': user_data.loj_handle,
                'user_email': user_data.user_email,
            }
        else:
            # user_data =
            all_data = {
                'sname': '',
                'toph_handle': '',
                'cf_handle': '',
                'cc_handle': '',
                'atcoder_handle': '',
                'loj_handle': '',
                'user_email': request.session['email'],
            }
        return render(request, 'settings.html', {'user_data':all_data})
    if request.session['user_type'] == 'contestant':
        user_data = cnts_model.objects.get(sid=request.session['id'])
        changes=request.POST
        for i in ['sname',
                'toph_handle',
                'cf_handle',
                'cc_handle',
                'atcoder_handle',
                'loj_handle',
                'user_email']:
            setattr(user_data,i,changes[i])
        user_data.save()

        all_data = {
            'sid': user_data.sid,
            'sname': user_data.sname,
            'toph_handle': user_data.toph_handle,
            'cf_handle': user_data.cf_handle,
            'cc_handle': user_data.cc_handle,
            'atcoder_handle': user_data.atcoder_handle,
            'loj_handle': user_data.loj_handle,
            'user_email': user_data.user_email,
        }
        messages.success(request,"Info Updated")

    return render(request, 'settings.html', {'user_data': all_data})


@is_allowed
def signout(request):
    request.session.clear()
    return HttpResponseRedirect('signin')
