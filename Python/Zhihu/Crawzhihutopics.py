import requests
from bs4 import BeautifulSoup

def getHTMLText(url):
    try:
        r= requests.get(url)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return ""




def main():
    url="https://www.zhihu.com/topics"
    html = getHTMLText(url)
    soup = BeautifulSoup(html,"html.parser")
    print (soup)


main()