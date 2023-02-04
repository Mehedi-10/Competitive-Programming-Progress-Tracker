import time
import sys
import requests
import json
from bs4 import BeautifulSoup
from lxml import etree
rest_time=5
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
            solved=self.dom.xpath('//*[@id="pageContent"]/div[4]/div/div[7]/div[1]/div[1]/div[1]')[0].text
            time.sleep(rest_time)
            url="https://codeforces.com/contests/with/"+handle
            page = requests.get(url)
            self.soup=BeautifulSoup(page.content,"html.parser")
            self.dom= etree.HTML((str(self.soup)))

            self.info = {
                'contest_count': self.dom.xpath('//*[@id="pageContent"]/div[4]/div[6]/table/tbody/tr[1]/td[1]')[0].text,
                'submission_count':'countless',
                'rating': str(rating),
                'highest_rating': str(highest_rating),
                'contribution': str(contribution),
                'rank': str(rank),
                'max rank':str(max_rank),
                'solved': str(solved)
            }
            self.status=True
        except Exception as e:
            print(e)
            self.status = False
if __name__ == '__main__':
    us=CODEFORCES('m-e-h-e-d-i')
    print(us.status)
