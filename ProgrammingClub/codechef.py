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
            ac_count=self.dom.xpath('/html/body/main/div/div/div/div/div/section[6]/div/h5[1]')[0].text
            ac_count=ac_count[ac_count.find('(')+1:ac_count.rfind(')')]
            # self.last_solved=html.fromstring(etree.tostring(self.soup)).xpath('/html/body/main/div/div/div/aside/div[4]/div/div/div[1]/table/tbody/tr[1]')
        except:
            self.status = False
            return
        self.info ={
        'contest_count': '0',
        'rating': 'Unrated',
        'highest_rating': 'Unrated',
        'rank': '0',
        'solved':'0'
    }
        try:
            self.info['contest_count'] = self.dom.xpath('/html/body/main/div/div/div/div/div/section[3]/div[1]/div/b')[
                0].text
        except:
            pass
        try:
            self.info['rating'] = self.dom.xpath('/html/body/main/div/div/div/aside/div[1]/div/div[1]/div[1]')[0].text
        except:
            pass
        try:
            self.info['highest_rating'] =self.dom.xpath('/html/body/main/div/div/div/aside/div[1]/div/div[1]/small')[0].text[2]
        except:
            pass
        try:
            self.info['rank'] = self.dom.xpath('/html/body/main/div/div/div/div/div/section[1]/ul/li[1]/span/span[1]')[
                0].text
        except:
            pass
        try:
            self.info['solved'] = ac_count
        except:
            pass
        self.status = True
if __name__ == '__main__':
    hi=CODECHEF('matrix33')
    hi.info