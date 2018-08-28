import requests
import time
from bs4 import BeautifulSoup


def getHTMLText(url):
    try:
        kv = {'User-Agent': 'Mozilla/5.0'}
        r = requests.get(url, headers=kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ''


def Timeinterval(interval):
    try:
        time_remaining = interval - time.time() % interval
        print("[%s] %s" % (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), "start"))
        time.sleep(time_remaining)
        print("[%s] %s" % (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), "stop"))
    except:
        print("错误")


def openTXT(path):
    try:
        list =[]
        with open(path, 'r') as f:
            for line in f.readlines():
                list.append(line.strip('\n'))# 用strip去掉结尾的\n
                print(line)
        return list
    except:
        print('read wrong!')

def searchTXT(list,interval,url):
    try:
        dict={}
        for date in list:
            Timeinterval(interval)
            Surl = url+date+".html"
            html = getHTMLText(Surl)
            soup = BeautifulSoup(html,'html.parser')
            p = soup.find_all(name='p')
            try:
                dict[date]=p[2]
            except:
                dict[date]='wrong'
                print(date)
        with open('G:\Python\cet4\one.txt', 'a', encoding='utf-8') as f:
            f.write(str(dict))

        print("下载完成")
    except:
        print('出错')

def main():
    nowinterval = 1
    dicturl = "http://www.dacidian.net/en/"
    path = 'G:\Python\cet4\cet4.txt'
    search = []
    search = openTXT(path)
    searchTXT(search,nowinterval,dicturl)





main()