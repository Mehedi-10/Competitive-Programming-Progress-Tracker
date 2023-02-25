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
        except:
            self.status = False
            return
        self.info = {
        'contest_count': '0',
        'rating': 'Unrated',
        'highest_rating': 'Unrated',
        'rank': '0',
        'solved':'0'
    }
        try:
            self.info['contest_count']='0'
        except:
            pass
        try:
            self.info['rating']='Unrated'
        except:
            pass
        try:
            self.info['highest_rating']='Unrated'
        except:
            pass
        try:
            self.info['rank']='0'
        except:
            pass
        try:
            self.info['solved']=self.dom.xpath('/html/body/div[1]/div/div/section/div/div/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/span[1]')[0].text
        except:
            pass
        self.status = True


