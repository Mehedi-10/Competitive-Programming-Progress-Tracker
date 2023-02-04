import requests
from bs4 import BeautifulSoup
import json

class ATCODER:

    def __init__(self,handle):
        try:
            self.handle=handle
            url="https://atcoder.jp/users/"+handle
            page = requests.get(url)
            self.soup=BeautifulSoup(page.content,"html.parser")
            tab = self.soup.find('table', class_="dl-table mt-2")
            dic = {}
            url="https://kenkoooo.com/atcoder/atcoder-api/v3/user/ac_rank?user="+handle
            page=requests.get(url)
            self.soup=json.loads(page.text)
            for tr in tab.find_all('tr'):
                dic.setdefault(tr.find('th').text)
                dic[tr.find('th').text] = tr.find('td').text.replace('\n', '')
            self.info={
                'contest_count':dic['Rated Matches '],
                'submission_count':'countless',
                'rating':dic['Rating'],
                'highest_rating':dic['Highest Rating'],
                'contribution':'countless',
                'rank':dic['Rank'],
                'last_contest':dic['Last Competed'],
                'solved':str(self.soup['count'])
            }
            print('atcoder done')
            self.status=True
        except:
            self.status=False
if __name__ == '__main__':
    u=ATCODER('mehedi10')


