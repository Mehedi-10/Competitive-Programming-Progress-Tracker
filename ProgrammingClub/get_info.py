import math
import random
import time
from datetime import datetime
from .toph import TOPH as tp
from .codechef import CODECHEF as cc
from .codeforces import CODEFORCES as cf
from .lightoj import LIGHTOJ as loj
from .atcoder import ATCODER as ac
from .models import contestant, codechef, codeforces, atcoder, lightoj, toph, resent_datas

take_rest = 3
take_lit_rest=2

def stodic(s: str):
    s = s.strip('{}')
    pairs = s.split(', ')
    dic = {key[1:-1]: str(value)[1:-1] for key, value in (pair.split(': ') for pair in pairs)}
    return dic


def time_delta(s):
    t1 = str(s.last_update_time)
    t11 = t1[0:19].replace('-', '/')
    t2 = str(datetime.now())
    t22 = t2[0:19].replace('-', '/')
    delta = datetime.strptime(t22, '%Y/%m/%d %H:%M:%S') - datetime.strptime(t11, '%Y/%m/%d %H:%M:%S')

    return delta.total_seconds() < (86400 // 2)

def time_difference_calc(s):
    t1 = str(s)
    t11 = t1[0:19].replace('-', '/')
    t2 = str(datetime.now())
    t22 = t2[0:19].replace('-', '/')
    delta = datetime.strptime(t22, '%Y/%m/%d %H:%M:%S') - datetime.strptime(t11, '%Y/%m/%d %H:%M:%S')

    return delta.total_seconds()



def init_atcoder(ob: contestant):
    ojdata = {}
    if len(ob.atcoder_handle) > 0:
        handle = ob.atcoder_handle
        try:
            ob = atcoder.objects.get(sid=ob.sid)
            if not time_delta(ob):
                cntstnt = ac(handle)
                if cntstnt.status:
                    ob.info = cntstnt.info.__str__()
                    ob.last_update_time = datetime.now().__str__()
                    ob.save()
            ojdata['atcoder'] = stodic(ob.info)
        except:
            cntstnt = ac(handle)
            if not cntstnt.status:
                time.sleep(take_lit_rest)
            else:
                ojdata.setdefault('atcoder')
                ojdata['atcoder'] = stodic(cntstnt.info.__str__())
                new_o = atcoder(
                    sid_id=ob.sid,
                    info=ojdata['atcoder'].__str__(),
                    last_update_time=datetime.now().__str__()
                )
                new_o.save()
            time.sleep(take_rest)
    return ojdata


def init_codeforces(ob: contestant):
    ojdata = {}
    if len(ob.cf_handle) > 0:
        handle = ob.cf_handle
        try:
            ob = codeforces.objects.get(sid=ob.sid)
            if not time_delta(ob):
                cntstnt = cf(handle)
                if cntstnt.status:
                    ob.info = cntstnt.info.__str__()
                    ob.last_update_time = datetime.now().__str__()
                    ob.save()
            ojdata['codeforces'] = stodic(ob.info)

        except:
            cntstnt = cf(handle)
            if not cntstnt.status:
                time.sleep(take_lit_rest)
            else:
                ojdata.setdefault('codeforces')
                ojdata['codeforces'] = str(cntstnt.info.__str__())
                new_o = codeforces(
                    sid_id=ob.sid,
                    info=ojdata['codeforces'].__str__(),
                    last_update_time=datetime.now().__str__()
                )
                new_o.save()
            time.sleep(take_rest)
    return ojdata


def init_toph(ob: contestant):
    ojdata = {}
    if len(ob.toph_handle) > 0:
        handle = ob.toph_handle
        try:
            ob = toph.objects.get(sid=ob.sid)
            if not time_delta(ob):
                cntstnt = tp(handle)
                print(cntstnt.status)
                if cntstnt.status:
                    ob.info = cntstnt.info.__str__()
                    ob.last_update_time = datetime.now().__str__()
                    ob.save()
            ojdata['toph'] = stodic(ob.info)
        except:
            cntstnt = tp(handle)
            if not cntstnt.status:
                time.sleep(take_lit_rest)
            else:
                ojdata.setdefault('toph')
                ojdata['toph'] = stodic(cntstnt.info.__str__())
                new_o = toph(
                    sid_id=ob.sid,
                    info=ojdata['toph'].__str__(),
                    last_update_time=datetime.now().__str__()
                )
                new_o.save()
            time.sleep(take_rest)

    return ojdata


def init_lightoj(ob: contestant):
    ojdata = {}
    if len(ob.loj_handle) > 0:
        handle = ob.loj_handle
        try:
            ob = lightoj.objects.get(sid=ob.sid)
            if not time_delta(ob):
                cntstnt = loj(handle)
                if cntstnt.status:
                    ob.info = cntstnt.info.__str__()
                    ob.last_update_time = datetime.now().__str__()
                    ob.save()
            ojdata['lightoj'] = stodic(ob.info)
        except:
            cntstnt = loj(handle)
            if not cntstnt.status:
                time.sleep(take_lit_rest)
            else:
                ojdata.setdefault('lightoj')
                ojdata['lightoj'] = stodic(cntstnt.info.__str__())
                new_o = lightoj(
                    sid_id=ob.sid,
                    info=ojdata['lightoj'].__str__(),
                    last_update_time=datetime.now().__str__()
                )
                new_o.save()
            time.sleep(take_rest)

    return ojdata


def init_codechef(ob: contestant):
    ojdata = {}
    if len(ob.cc_handle) > 0:
        handle = ob.cc_handle
        try:
            ob = codechef.objects.get(sid=ob.sid)
            if not time_delta(ob):
                cntstnt = cc(handle)
                if cntstnt.status:
                    ob.info = cntstnt.info.__str__()
                    ob.last_update_time = datetime.now().__str__()
                    ob.save()
            ojdata['codechef'] = stodic(ob.info)
        except:
            cntstnt = cc(handle)
            if not cntstnt.status:
                time.sleep(take_lit_rest)
            else:
                ojdata.setdefault('codechef')
                ojdata['codechef'] = stodic(cntstnt.info.__str__())
                new_o = codechef(
                    sid_id=ob.sid,
                    info=ojdata['codechef'].__str__(),
                    last_update_time=datetime.now().__str__()
                )
                new_o.save()
            time.sleep(take_rest)
    return ojdata

from collections import deque

names = ['codechef', 'codeforces', 'atcoder', 'lightoj', 'toph']
init_array=deque([init_codechef, init_atcoder, init_toph, init_lightoj, init_codeforces])
model_array=deque([codechef,atcoder, toph,lightoj,codeforces])


def get_info(student_id: int, Update_now=True):
    init_array.rotate(1)
    model_array.rotate(1)
    try:
        ob = contestant.objects.get(sid=student_id)
    except:
        return {}
    ojdata = {}

    if Update_now:
        for f in init_array:
            try:
                ojdata.update(f(ob))
            except:
                pass
    else:
        i_name = 0
        for f in model_array:
            try:
                ob = f.objects.get(sid=student_id)
                ojdata.update({names[i_name]: stodic(ob.info)})
            except:
                pass
            i_name += 1

    print(ojdata)

    return ojdata


def stoi(num: str):
    s = '0'
    for i in num:
        if i >= '0' and i <= '9':
            s += i
    return int(s)


def get_rating():
    all_contestant = {}
    for i in contestant.objects.all():
        tmp1 = {}
        i_name = 0
        for f in [codechef, codeforces, atcoder, lightoj, toph]:
            try:
                ob = f.objects.get(sid=i.sid)
                tmp1.update({names[i_name]: stodic(ob.info)})
            except:
                pass
            i_name += 1
        tmp = {i.sid: tmp1}
        all_contestant.update(tmp)
    dic = []
    all_dic = []
    weekly = []
    for key, val in all_contestant.items():
        total_solved = 0
        calc_ok = True
        # print(key, end=" ")
        for key1, val1 in val.items():
            # print(key1, val1)
            try:
                rating = stoi(val1['rating'])
                total_solved += stoi(val1['solved'])
            except:
                rating = 0
                calc_ok = False
                print("error getting rating")
        if calc_ok:
            rating /= 6
            rating = math.ceil(rating)
            if not resent_datas.objects.filter(sid=key).exists():
                ob = resent_datas(
                    sid_id=key,
                    solved=str(total_solved),
                    rating=str(rating),
                    date=datetime.now().__str__()
                )
                ob.save()
            else:
                if time_difference_calc(resent_datas.objects.filter(sid=key).order_by('date').last().date)>=86400:
                    ob = resent_datas(
                        sid_id=key,
                        solved=str(total_solved),
                        rating=str(rating),
                        date=datetime.now().__str__()
                    )
                    ob.save()
            rating_set = []
            solved_set = []
            for i in resent_datas.objects.filter(sid=key).order_by('date'):
                rating_set.append((int(i.rating), i.date))
                solved_set.append((int(i.solved), i.date))
            color = ['#f87171', '#a3e635', '#4ade80', '#34d399', '#22d3ee', '#38bdf8', '#60a5fa', '#818cf8', '#a78bfa',
                     '#fb7185','#c084fc', '#ef4444', '#84cc16', '#22c55e', '#06b6d4', '#a855f7']
            if str(key)[3:5] == '08':
                dic.append((key, rating, rating_set, color[len(dic)%len(color)]))
                weekly.append((key, total_solved, solved_set, color[len(dic)%len(color)]))
            all_dic.append((key, rating, rating_set, color[len(dic)%len(color)]))
    # print('pre',dic)
    # dept rank-list
    dic.sort(key=lambda x: x[1], reverse=True)
    # university rank-link
    all_dic.sort(key=lambda x: x[1], reverse=True)
    # weekly solved rank-list
    weekly.sort(key=lambda x: x[1], reverse=True)
    # print('hi',dic)
    # print('hello',all_dic)
    # print('hp', weekly)
    return (dic, all_dic, weekly)
