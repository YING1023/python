import requests
from bs4 import BeautifulSoup
import re
import time

def TimeInterval(interval):
    try:
        time_remaining = interval - time.time() % interval
        print("[%s] %s" % (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), "start"))
        time.sleep(time_remaining)
        print("[%s] %s" % (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), "stop"))
    except:
        print("错误")

try:
    list=[]
    interval=1
    url = 'https://movie.douban.com/top250?start='
    for i in range(10):
        TimeInterval(interval)
        print(i)
        r= requests.get(url+str(i*25)+'&filter=')
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        html = r.text

        a=re.findall(r'https://movie.douban.com/subject/\d+/">',html)
        for i in a:
            c=i[:-2]
            list.append(c)


    n=0
    for g in list:
        n = n+1
        print(n,g)



        # 全部用正则表达式！！！！！！！！！！
        #,string=re.compile(r'https://movie.douban.com/subject/\d+/'))
        #存在span的到底是什么东西居然不能直接用正则表达式

        #为什么list输出会带有【‘’】这种狗屎
        #为什么beautifusoup 打出来的finshid_all列表不是text


            #将由获得的 spam列表遍历找到网址并且用另一个列表储存










        '''
        for g in list:
            print()

            v= requests.get(g)
            v.encoding = v.apparent_encoding
            print(v.text)
            '''






except:
    print('破站要亡')