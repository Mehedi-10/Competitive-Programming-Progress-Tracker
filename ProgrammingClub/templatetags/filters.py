from django import template
from ..models import contestant

register = template.Library()
import random


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


@register.filter
def get_name(key):
    return contestant.objects.get(sid=key).sname


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
    print(key)
    try:
        if key[0]=='(':
            key=remove_bracket(key)
        if key[0]=='-':
            return 'fa-arrow-down text-orange-500'
        elif key[0]=='+':
            return 'fa-arrow-up text-green-500'
    except:
        pass
    try:
        if key[-1] - key[-2] >= 0:
            return 'fa-arrow-up text-green-500'
        else:
            return 'fa-arrow-down text-orange-500'
    except:
        return 'fa-arrow-up text-green-500'


@register.filter()
def rating_delta(key):
    try:
        return key[-1] - key[-2]
    except:
        return 0
@register.filter()
def percentage(key):
    try:
        return key[-1] - key[-2]
    except:
        return 0
@register.filter()
def card_class(key):
    try:
        if key[0]=='(':
            key=remove_bracket(key)
        if key[0]=='-':
            return 'text-orange-500 bg-orange-100'
        elif key[0]=='+':
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


