import requests
from bs4 import BeautifulSoup
import re

url='https://docs.scrapy.org/en/latest/index.html'
r= requests.get(url)
r.raise_for_status()
r.encoding=r.apparent_encoding
html= r.text

soup = BeautifulSoup(html,"html.parser")
li = soup.find_all('li',attrs={'class':'toctree-l1'})
for i in li:
    a=re.findall(r'href="\S+html',str(i))
    a=str(a).split('"')[1]
    a=a.split("'")[0]

    print(a)




