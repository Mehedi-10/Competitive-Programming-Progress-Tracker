from django.test import TestCase
li=['Algebra','Data Structures','Graphs and Trees','Dynamic Programming','String Processing','Combinatorics','Geometry','Miscellaneous']
from .get_info import get_info
from .models import contestant
from apscheduler.schedulers.background import BackgroundScheduler
def schedule():
    for i in contestant.objects.all():
        get_info(i.sid)
def start():
    sched=BackgroundScheduler()
    sched.add_job(schedule,'interval',seconds=3600)
    sched.start()
