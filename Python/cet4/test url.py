import requests
from bs4 import BeautifulSoup


def getHTMLText(url):
    try:
        kv = {'User-Agent': 'Mozilla/5.0'}
        r = requests.get(url,headers=kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return '出错'

def getList(url):
    try:
        html = getHTMLText(url)
        soup = BeautifulSoup(html,'html.parser')
        p =soup.find_all(name='p')
        print(p[2])

    except:
        print()

def main():
    surl='http://www.dacidian.net/en/true.html'
    getList(surl)

main()
