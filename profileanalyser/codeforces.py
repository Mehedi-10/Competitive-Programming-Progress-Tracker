import time

import requests
import json
from bs4 import BeautifulSoup
from lxml import etree
class CODEFORCES:

    def __init__(self,handle):
        try:
            self.handle=handle
            url="https://codeforces.com/api/user.info?handles="+handle
            page = requests.get(url)
            self.soup=json.loads(page.text)
            if self.soup['status']=='OK':
                self.rating =self.soup['result'][0]['rating']
                self.highest_rating = self.soup['result'][0]['maxRating']
                self.rank=self.soup['result'][0]['rank']
                self.max_rank=self.soup['result'][0]['maxRank']
                self.contribution = self.soup['result'][0]['contribution']
            time.sleep(5)
            url = "https://codeforces.com/profile/"+ handle
            page = requests.get(url)
            self.soup=BeautifulSoup(page.content,"html.parser")
            self.dom= etree.HTML((str(self.soup)))
            self.ac_count=self.dom.xpath('//*[@id="pageContent"]/div[4]/div/div[7]/div[1]/div[1]/div[1]')[0].text
            self.submission_count ='invalid'
            time.sleep(5)
            url="https://codeforces.com/contests/with/"+handle
            page = requests.get(url)
            self.soup=BeautifulSoup(page.content,"html.parser")
            self.dom= etree.HTML((str(self.soup)))
            self.contest_count = self.dom.xpath('//*[@id="pageContent"]/div[4]/div[6]/table/tbody/tr[1]/td[1]')[0].text
        except:
            pass
