import requests
from bs4 import BeautifulSoup
from lxml import etree
class LIGHTOJ:

    def __init__(self,handle):
        try:
            self.handle=handle
            url="https://lightoj.com/user/"+handle
            page = requests.get(url)
            self.soup=BeautifulSoup(page.content,"html.parser")
            self.dom= etree.HTML((str(self.soup)))
            self.contest_count=0
            self.ac_count=self.dom.xpath('/html/body/div[1]/div/div/section/div/div/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/span[1]')[0].text
            self.submission_count=self.dom.xpath('/html/body/div[1]/div/div/section/div/div/div/div[2]/div[2]/div/div[2]/div[1]/div[2]/span[1]')[0].text
            self.rating='unrated'
            self.highest_rating='unrated'
            self.contribution=0
            self.last_solved=self.dom.xpath('//*[@id="pages-community"]/div[2]/div[2]/div/div[1]/div[2]/div/div/div[1]/span[2]/h4/span')[0].text
        except:
            pass
