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

@register.filter()
def random_num(a):
    return random.randint(1400,1700)
@register.filter()
def remove_after_space(a):
    if a.find(' ')!=-1:
        a=a[0:a.find(' ')]
    return a

@register.filter()
def star(a):
    s=a
    if len(a)>1 and a[1]=='★':
        s='★'*int(a[0])
    return s

