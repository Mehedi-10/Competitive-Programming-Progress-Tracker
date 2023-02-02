import requests
from bs4 import BeautifulSoup

class ATCODER:

    def __init__(self,handle):
        try:
            self.handle=handle
            url="https://atcoder.jp/users/"+handle
            page = requests.get(url)
            self.soup=BeautifulSoup(page.content,"html.parser")
            tab = self.soup.find('table', class_="dl-table mt-2")
            dic = {}
            for tr in tab.find_all('tr'):
                dic.setdefault(tr.find('th').text)
                dic[tr.find('th').text] = tr.find('td').text.replace('\n', '')
            self.contest_count=dic['Rated Matches ']
            # self.ac_count=self.dom.xpath('/html/body/main/div/div/div/div/div/section[6]/div/h5[1]')[0].text
            self.submission_count='undefined'
            self.rating=dic['Rating']
            self.highest_rating=dic['Highest Rating']
            self.contribution='undefined'
            self.rank=dic['Rank']
            self.last_contest=dic['Last Competed']
        except:
            pass
