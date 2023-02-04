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
            self.info = {
                'contest_count': 0,
                'submission_count': self.dom.xpath('/html/body/div[1]/div/div/section/div/div/div/div[2]/div[2]/div/div[2]/div[1]/div[2]/span[1]')[0].text,
                'rating': 'unrated',
                'highest_rating':'unrated',
                'contribution': 'countless',
                'rank': 'coming soon',
                'last_solved': self.dom.xpath('//*[@id="pages-community"]/div[2]/div[2]/div/div[1]/div[2]/div/div/div[1]/span[2]/h4/span')[0].text,
                'solved': self.dom.xpath('/html/body/div[1]/div/div/section/div/div/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/span[1]')[0].text
            }
            print('lightoj done')
            self.status=True
        except:
            self.status = False
