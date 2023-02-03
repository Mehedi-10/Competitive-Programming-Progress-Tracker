import requests
from bs4 import BeautifulSoup
from lxml import etree, html


class CODECHEF:

    def __init__(self,handle):
        try:
            self.handle=handle
            url="https://www.codechef.com/users/"+handle
            page = requests.get(url)
            self.soup=BeautifulSoup(page.content,"html.parser")
            self.dom= etree.HTML((str(self.soup)))
            self.contest_count=self.dom.xpath('/html/body/main/div/div/div/div/div/section[3]/div[1]/div/b')[0].text
            self.ac_count=self.dom.xpath('/html/body/main/div/div/div/div/div/section[6]/div/h5[1]')[0].text
            self.ac_count=self.ac_count[self.ac_count.find('(')+1:self.ac_count.rfind(')')]
            self.submission_count='undefined'
            self.rating=self.dom.xpath('/html/body/main/div/div/div/aside/div[1]/div/div[1]/div[1]')[0].text
            self.highest_rating=self.dom.xpath('/html/body/main/div/div/div/aside/div[1]/div/div[1]/small')[0].text[2]
            self.contribution='undefined'
            self.rank=self.dom.xpath('/html/body/main/div/div/div/div/div/section[1]/ul/li[1]/span/span[1]')[0].text
            # self.last_solved=html.fromstring(etree.tostring(self.soup)).xpath('/html/body/main/div/div/div/aside/div[4]/div/div/div[1]/table/tbody/tr[1]')
            self.status=True
        except:
            self.status = False
