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
            self.info = {
                'contest_count': self.dom.xpath('/html/body/div[1]/div/div/div[1]/div/div[2]/div[1]/div/div[1]/div[1]')[0].text,
                'submission_count':self.dom.xpath('/html/body/div[1]/div/div/div[1]/div/div[2]/div[1]/div/a/div[1]')[0].text,
                'rating': self.dom.xpath('/html/body/div[1]/div/div/div[2]/div[2]/div[1]/a/div[2]/div')[0].text.replace('\n',''),
                # highest_rating need to be updated
                'highest_rating': self.dom.xpath('/html/body/div[1]/div/div/div[2]/div[2]/div[1]/a/div[2]/div')[0].text.replace('\n',''),
                'contribution': self.dom.xpath('/html/body/div[1]/div/div/div[2]/div[2]/div[3]/a/div[2]/div')[0].text,
                'rank': self.dom.xpath('/html/body/div[1]/div/div/div[2]/div[2]/div[1]/a/div[2]/div/span/span')[0].text,
                'solved': self.dom.xpath('/html/body/div[1]/div/div/div[1]/div/div[2]/div[1]/div/div[2]/div[1]')[0].text
            }
            print('toph done')
            self.status=True
        except Exception as e:
            self.status=False
