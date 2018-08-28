import requests
import json
from bs4 import BeautifulSoup
import time
import re
r=requests.get('http://www.youdao.com/w/eng/tree/')
r.raise_for_status()
r.encoding=r.apparent_encoding
html=r.text
list=[]

list.append(re.findall(r'<li>\D+</li>',html)[0])

for i in list:
    s=str(i)
    list1=s.split('\n')
    print(list1)
    print(re.findall(r'>\D+<',s)[0])
