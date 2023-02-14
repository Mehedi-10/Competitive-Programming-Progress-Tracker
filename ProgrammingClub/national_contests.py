import requests
from bs4 import BeautifulSoup
import pandas as pd
def synapse():
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
    rnk_list=rnk_list[0:20]
    pp=pd.DataFrame(rnk_list,columns =['Rank','University','Rating'])
    return pp.to_html()
