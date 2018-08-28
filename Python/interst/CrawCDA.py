import requests
from bs4 import BeautifulSoup
import re

def getHTMLText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def getCDAList(Infourl):
    try:
        for num in range(29,48):
            num1=str(num)
            url=Infourl + num1 + ".html"
            html = getHTMLText(url)
            soup =BeautifulSoup(html,"html.parser")
            p = soup.find('p',attrs={'class':'kecheng-mc'})
            div = soup.find_all('div',attrs={'class':'padd'})
            print(num,p.string)

    except:
        return ""


def main():

    CDAurl= "http://www.cda.cn/kecheng/"
    getCDAList(CDAurl)

main()
