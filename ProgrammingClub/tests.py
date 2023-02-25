from django.test import TestCase
li=['Algebra','Data Structures','Graphs and Trees','Dynamic Programming','String Processing','Combinatorics','Geometry','Miscellaneous']
from .get_info import get_info
from .models import contestant
from .codechef import CODECHEF
from apscheduler.schedulers.background import BackgroundScheduler
import random
def schedule():
    print('scheduler start')
    li=[]
    for i in contestant.objects.all():
        li.append(i.sid)
    random.shuffle(li)
    print(li)
    for i in range(len(li)):
        get_info(li[i])


def start():
    schedule()
    sched=BackgroundScheduler()
    sched.add_job(schedule,'interval',seconds=1800)
    sched.start()

