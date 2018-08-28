import requests
from bs4 import BeautifulSoup
url='faq.html'
r=requests.get('https://docs.scrapy.org/en/latest/'+url)
r.raise_for_status()
r.encoding=r.apparent_encoding
html= r.text

soup =BeautifulSoup(html,"html.parser")
p=soup.find_all('p')
list=[]
for i in p:
    list.append(i)
    print(i)
path = 'G:\Python\scrapytext/text.txt'
with open(path, 'a', encoding='utf-8') as f:
    for i in list:
        f.write(str(i) + '\n')