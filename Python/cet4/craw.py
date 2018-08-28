import requests
import time


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

#def getCET4List():


def main():
    interval = 5
    url = "http://dict.cn/tree"
    r=getHTMLText(url)

    print(r)


main()