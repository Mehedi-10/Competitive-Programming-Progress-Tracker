# oj=['codechef.com','codeforces.com','atcoder.jp','toph.co','lightoj.com']
# #codingcompetitions.withgoogle.com
import requests
import json
import sys
import datetime

sys.stdout.reconfigure(encoding='utf-8')

def fun():
    url = 'https://clist.by/api/v2/json/contest/?upcoming=true&format_time=true&start_time__during=30%20days&resource=codechef.com%2Ccodeforces.com%2Catcoder.jp%2Ctoph.co%2Clightoj.com&duration__lt=1%20days&order_by=end'
    header = {'Authorization': 'ApiKey Mehedi:db22d70ba099409f2eb90caa3945cf7d745a0de2'}
    page = requests.get(url, headers=header)
    text = json.loads(page.text)
    contest = {}
    now = datetime.datetime.now()
    for i in text['objects']:
        if not now.month==int(i['start'][3:5]):
            continue
        dic = {
            'date': int(i['start'][0:2]),
            'start': i['start'][6:],
            'link': i['href'],
            'duration': i['duration'],
            'event': i['event']
        }
        if dic['date'] not in contest.keys():
            contest.setdefault(dic['date'])
            contest[dic['date']] = []
        contest[dic['date']].append(dic)

    return contest

