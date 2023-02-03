import requests
from bs4 import BeautifulSoup
from lxml import etree
class TOPH:

    def __init__(self,handle):
        try:
            self.handle=handle
            url="https://toph.co/u/"+handle
            page = requests.get(url)
            self.soup=BeautifulSoup(page.content,"html.parser")
            self.dom= etree.HTML((str(self.soup)))
            self.contest_count=self.dom.xpath('/html/body/div[1]/div/div/div[1]/div/div[2]/div[1]/div/div[1]/div[1]')[0].text
            self.ac_count=self.dom.xpath('/html/body/div[1]/div/div/div[1]/div/div[2]/div[1]/div/div[2]/div[1]')[0].text
            self.submission_count=self.dom.xpath('/html/body/div[1]/div/div/div[1]/div/div[2]/div[1]/div/a/div[1]')[0].text
            self.rating=self.dom.xpath('/html/body/div[1]/div/div/div[2]/div[2]/div[1]/a/div[2]/div')[0]
            self.contribution=self.dom.xpath('/html/body/div[1]/div/div/div[2]/div[2]/div[3]/a/div[2]/div')[0].text
            self.rank=self.dom.xpath('/html/body/div[1]/div/div/div[2]/div[3]/div[1]/a/div[2]/div/span/span')[0].text
            self.status=True
        except:
            self.status=False