import time
import sys
import requests
import json
from bs4 import BeautifulSoup
from lxml import etree
rest_time=2
sys.stdout.reconfigure(encoding='utf-8')

class CODEFORCES:

    def __init__(self,handle):
        # self.handle = handle
        # url = "https://codeforces.com/api/user.info?handles=" + handle
        # page = requests.get(url)
        # print(page.text)
        # self.soup = json.loads(page.text)
        # print('hello')
        # if self.soup['status'] == 'OK':
        #     rating = self.soup['result'][0]['rating']
        #     highest_rating = self.soup['result'][0]['maxRating']
        #     rank = self.soup['result'][0]['rank']
        #     max_rank = self.soup['result'][0]['maxRank']
        #     contribution = self.soup['result'][0]['contribution']
        # self.info={}
        # self.status=False

        try:
            self.handle=handle
            url="https://codeforces.com/api/user.info?handles="+handle
            page = requests.get(url)
            self.soup=json.loads(page.text)
            if self.soup['status']=='OK':
                rating =self.soup['result'][0]['rating']
                highest_rating = self.soup['result'][0]['maxRating']
                rank=self.soup['result'][0]['rank']
                max_rank=self.soup['result'][0]['maxRank']
                contribution = self.soup['result'][0]['contribution']
            time.sleep(rest_time)
            url = "https://codeforces.com/profile/"+ handle
            page = requests.get(url)
            self.soup=BeautifulSoup(page.content,"html.parser")
            self.dom= etree.HTML((str(self.soup)))
            # // *[ @ id = "pageContent"] / div[4] / div / div[3] / div[1] / div[1] / div[1]
            solved=self.dom.xpath('//*[@id="pageContent"]/div[4]/div/div[3]/div[1]/div[1]/div[1]')[0].text
            time.sleep(rest_time)
            url="https://codeforces.com/contests/with/"+handle
            page = requests.get(url)
            self.soup=BeautifulSoup(page.content,"html.parser")
            self.dom= etree.HTML((str(self.soup)))


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
            self.info['contest_count'] = self.dom.xpath('//*[@id="pageContent"]/div[4]/div[6]/table/tbody/tr[1]/td[1]')[0].text
        except:
            pass
        try:
            self.info['rating'] = str(rating)
        except:
            pass
        try:
            self.info['highest_rating'] = str(highest_rating)
        except:
            pass
        try:
            self.info['rank'] = str(rank)
        except:
            pass
        try:
            self.info['solved'] = str(solved)
        except:
            pass
        self.status = True

if __name__ == '__main__':
    us=CODEFORCES('m-e-h-e-d-i')
    print(us.status)
