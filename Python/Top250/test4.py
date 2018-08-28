import requests
from bs4 import BeautifulSoup
import re
try:
    url='https://movie.douban.com/top250?start=0&filter='
    r= requests.get(url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    html = r.text
    soup = BeautifulSoup(html,'html.parser')
    span = soup.find_all(name='span', attrs={'class': "title"},string=re.compile(r'^\w+'))
    for i in span:
        title = i.string
        print(title)


except:
    print('破站要亡')
