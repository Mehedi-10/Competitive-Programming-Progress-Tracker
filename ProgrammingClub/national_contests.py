import requests
from bs4 import BeautifulSoup
def synapse():
    try:
        url = "https://synapse0.com/"
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        soup.prettify()
        table=soup.table.tbody
        rnk_list=[]
        for i in table.find_all('tr'):
            tmp=[]
            first=True
            for j in i:
                if j.text!='\n':
                    if first:
                        first=False
                        continue
                    tmp.append(j.text)
            rnk_list.append(tmp)
        indx=0
        for i in range(0,len(rnk_list)):
            if rnk_list[i][1]=='Comilla University':
                indx=i
        return rnk_list[indx]
    except:
        return ['Fetching (+0)']

