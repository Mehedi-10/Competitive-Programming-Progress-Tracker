import requests
from bs4 import BeautifulSoup
import json


class ATCODER:

    def __init__(self, handle):
        try:
            self.handle = handle
            url = "https://atcoder.jp/users/" + handle
            page = requests.get(url)
            self.soup = BeautifulSoup(page.content, "html.parser")
            tab = self.soup.find('table', class_="dl-table mt-2")
            dic = {}
            url = "https://kenkoooo.com/atcoder/atcoder-api/v3/user/ac_rank?user=" + handle
            page = requests.get(url)
            self.soup = json.loads(page.text)
            for tr in tab.find_all('tr'):
                dic.setdefault(tr.find('th').text)
                dic[tr.find('th').text] = tr.find('td').text.replace('\n', '')
        except:
            self.status = False
            return
        self.info = {
            'contest_count': '0',
            'rating': 'Unrated',
            'highest_rating': 'Unrated',
            'rank': '0',
            'solved': '0'
        }
        try:
            self.info['contest_count'] = dic['Rated Matches ']
        except:
            pass
        try:
            self.info['rating'] = dic['Rating']
        except:
            pass
        try:
            self.info['highest_rating'] = dic['Highest Rating']
        except:
            pass
        try:
            self.info['rank'] =dic['Rank']
        except:
            pass
        try:
            self.info['solved'] = str(self.soup['count'])
        except:
            pass
        self.status = True

