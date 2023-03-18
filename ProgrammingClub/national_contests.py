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
            for j in i:
                txt=j.text.replace('\n','').strip()
                if len(txt)>0:
                    tmp.append(txt)
            rnk_list.append(tmp[1:])

        indx=0
        for i in range(0,len(rnk_list)):
            print(rnk_list[i])
            if rnk_list[i][1]=='Comilla University':
                indx=i
        return rnk_list[indx]
    except:
        return ['Fetching (+0)']

