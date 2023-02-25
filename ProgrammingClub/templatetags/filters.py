from django import template
from ..models import contestant

register = template.Library()
import random
import datetime


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


@register.filter
def get_name(key):
    return contestant.objects.get(sid=key).sname.title()


@register.filter
def get_expertise(key):
    li = ['Algebra', 'Data Structures', 'Graphs and Trees', 'Dynamic Programming', 'String Processing', 'Combinatorics',
          'Geometry', 'Miscellaneous']
    n = random.randint(1, 2)
    topics = []
    for i in range(n):
        topics.append(li[random.randint(0, len(li) - 1)])
    topics = set(topics)
    return topics


@register.filter()
def random_num(a):
    return random.randint(1400, 1700)


@register.filter()
def remove_after_space(a):
    if a.find(' ') != -1:
        a = a[0:a.find(' ')]
    return a


@register.filter()
def star(a):
    s = a
    if len(a) > 1 and a[1] == '★':
        s = '★' * int(a[0])
    return s


@register.filter()
def tophlink(key):
    return "https://toph.co/u/" + contestant.objects.get(sid=key).toph_handle


@register.filter()
def cflink(key):
    return "https://codeforces.com/profile/" + contestant.objects.get(sid=key).cf_handle


@register.filter()
def cclink(key):
    return "https://www.codechef.com/users/" + contestant.objects.get(sid=key).cc_handle


@register.filter()
def get_class(key):
    try:
        if key[0] == '(':
            key = remove_bracket(key)
        if key[0] == '-':
            return 'fa-arrow-down text-orange-500'
        elif key[0] == '+':
            return 'fa-arrow-up text-green-500'
    except:
        pass
    try:
        if int(key[-1][0]) - int(key[-2][0]) >= 0:
            return 'fa-arrow-up text-green-500'
        else:
            return 'fa-arrow-down text-orange-500'
    except:
        return 'fa-arrow-up text-green-500'


@register.filter()
def rating_delta(key):
    try:
        x=int(key[-1][0]) - int(key[-2][0])
        if x<0:
            return str(x)
        elif x!=0:
            return '+'+str(x)
        else:
            return '0'
    except:
        return '0'


@register.filter()
def percentage(key):
    try:
        return key[-1] - key[-2]
    except:
        return 0


@register.filter()
def card_class(key):
    try:
        if key[0] == '(':
            key = remove_bracket(key)
        if key[0] == '-':
            return 'text-orange-500 bg-orange-100'
        elif key[0] == '+':
            return 'text-green-500 bg-green-100'
    except:
        pass
    try:
        if key[-1] - key[-2] >= 0:
            return 'text-green-500 bg-green-100'
        else:
            return 'text-orange-500 bg-orange-100'
    except:
        return 'text-green-500 bg-green-100'


@register.filter()
def remove_bracket(key):
    return key[1:-1]


@register.filter()
def day(date):
    date = date[0:19].replace('-', '/')
    x = datetime.datetime.strptime(date, '%Y/%m/%d %H:%M:%S')
    return x


@register.filter()
def next_day(date):
    date = date[0:19].replace('-', '/')
    x = datetime.datetime.strptime(date, '%Y/%m/%d %H:%M:%S')
    x = x + datetime.timedelta(days=1)
    return x

@register.filter()
def get_rating_fortnight(data):
    day_solved = {}

    for i in data:
        today = i[1]
        today = today[0:19].replace('-', '/')
        x = datetime.datetime.strptime(today, '%Y/%m/%d %H:%M:%S')
        day_solved.update({x.date().__str__(): int(i[0])})

    today = datetime.datetime.now().__str__()
    today = today[0:19].replace('-', '/')
    x = datetime.datetime.strptime(today, '%Y/%m/%d %H:%M:%S')
    pre = list(day_solved.keys())[-1]
    for i in range(16):
        x = x - datetime.timedelta(days=1)
        if x.date().__str__() not in day_solved.keys():
            day_solved.update({x.date().__str__(): day_solved[pre]})
        else:
            pre = x.date().__str__()
    day_solved = list(day_solved.items())
    day_solved.sort(reverse=True)
    new_day_solved = []

    for i in range(len(day_solved) - 1):
        today = day_solved[i][0]
        today = today[0:19].replace('-', '/')
        new_day_solved.append(
            (datetime.datetime.strptime(today, '%Y/%m/%d'), day_solved[i][1]))
    new_day_solved=new_day_solved[0:15]
    new_day_solved.reverse()

    return new_day_solved

@register.filter()
def get_solved_weekly(data):
    day_solved = {}
    #
    for i in data:
        today = i[1]
        today = today[0:19].replace('-', '/')
        x = datetime.datetime.strptime(today, '%Y/%m/%d %H:%M:%S')
        day_solved.update({x.date().__str__(): int(i[0])})

    today = datetime.datetime.now().__str__()
    today = today[0:19].replace('-', '/')
    x = datetime.datetime.strptime(today, '%Y/%m/%d %H:%M:%S')
    pre = list(day_solved.keys())[-1]
    for i in range(8):
        x = x - datetime.timedelta(days=1)
        if x.date().__str__() not in day_solved.keys():
            day_solved.update({x.date().__str__(): day_solved[pre]})
        else:
            pre = x.date().__str__()
    day_solved = list(day_solved.items())
    day_solved.sort(reverse=True)
    new_day_solved = []

    for i in range(len(day_solved) - 1):
        today = day_solved[i][0]
        today = today[0:19].replace('-', '/')
        new_day_solved.append(
            (datetime.datetime.strptime(today, '%Y/%m/%d'), min(day_solved[i][1] - day_solved[i + 1][1], 100)))
    new_day_solved=new_day_solved[0:7]
    new_day_solved.reverse()
    print('day solved',new_day_solved)
    return new_day_solved
