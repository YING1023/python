import requests
from bs4 import BeautifulSoup
import re
import time

def getHTML(url):
    try:
        r=requests.get(url)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        print("url有误")

def TimeInterval(interval):
    try:
        time_remaining = interval - time.time() % interval
        print("[%s] %s" % (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), "start"))
        time.sleep(time_remaining)
        print("[%s] %s" % (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), "stop"))
    except:
        print("错误")


def getURL():
    try:
        url = 'https://docs.scrapy.org/en/latest/index.html'
        html=getHTML(url)
        soup = BeautifulSoup(html, "html.parser")
        li = soup.find_all('li', attrs={'class': 'toctree-l1'})
        list=[]
        for i in li:
            a = re.findall(r'href="\S+html', str(i))
            a = str(a).split('"')[1]
            a = a.split("'")[0]
            list.append(a)
        return list
    except:
        print("url不全")

def getTEXT(URLlist,timeout):
    try:
        textlist=[]
        for i in URLlist:
            TimeInterval(timeout)
            url='https://docs.scrapy.org/en/latest/'+i
            html = getHTML(url)
            soup = BeautifulSoup(html, "html.parser")
            p = soup.find_all('p')

            for i in p:
                textlist.append(i)
                print(i)
        path = 'G:\Python\scrapytext/text.txt'
        with open(path, 'a', encoding='utf-8') as f:
            for i in textlist:
                f.write(str(i) + '\n')

    except:
        print("text错误")


def main():
    URLlist=[]
    timeout=1
    URLlist=getURL()
    getTEXT(URLlist,timeout)

main()

