import requests
import time
from bs4 import BeautifulSoup
import traceback
import re



def getHtmlText(url):
    try:
        kv = {'User-Agent': 'Mozilla/5.0'}
        r = requests.get(url,headers=kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return 1


def TimeInterval(interval):
    try:
        time_remaining = interval - time.time() % interval
        print("[%s] %s" % (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), "start"))
        time.sleep(time_remaining)
        print("[%s] %s" % (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), "stop"))
    except:
        print("错误")


def getMoiveUrl(url,interval):
    try:
        list=[]
        for i in range(50):
            TimeInterval(interval)
            html = getHtmlText(url + str(i * 20) + '&type=S')
            a = re.findall(r'https://movie.douban.com/subject/\d*/', html)
            count=1
            for i in a:
                if (count%2) ==0 :
                    list.append(i)
                count = count + 1

        return list
    except:
        print('Moive wrong')


def getDatelist(interval,list):
    try:
        n=0
        Datelist = []
        for i in list:
            TimeInterval(interval)
            n=n+1
            print(n)
            html = getHtmlText(i)
            if html == 1:
                Datelist.append([1,i])
            else:
                soup = BeautifulSoup(html, 'html.parser')

                try:
                    title = soup.find(name='span', attrs={'property': 'v:itemreviewed'})
                    title = title.string
                except:
                    title = "none"

                try:
                    point = soup.find(name='strong', attrs={'class': 'll rating_num'})
                    point = point.string
                except:
                    point ="none"

                try:
                    people = soup.find(name='span', attrs={'property': 'v:votes'})
                    people = people.string
                except:
                    people = "none"

                try:
                    time = soup.find(name='span', attrs={'property': 'v:initialReleaseDate'})
                    time = time.string
                except:
                    time = "none"

                '''
                screenwriter = soup.find(name='span', attrs={'class': 'attrs'})
                screenwriter = screenwriter.string
                '''
                try:
                    if int(people)>2999:
                        Datelist.append([title, point, people, time])
                except:
                    print('chucuo ')





        tplt = '{:16}\t{:4}\t{:8}\t{:16}'
        print(tplt.format( '电影名称', '评分', '评分人数', '上映时间'))
        for g in Datelist:
            if g[0] == 1:
                print('链接失效，原链接为',g[1])
            else:
                print(tplt.format(g[0], g[1], g[2], g[3]))

        path = 'G:\Python\Douban/纪录片.txt'
        with open(path, 'a', encoding='utf-8') as f:
            for i in Datelist:
                f.write(str(i) + '\n')
        print('打印完毕')






    except:
        traceback.print_exc()

def main():
    Janpeneseurl='https://movie.douban.com/tag/%E7%BA%AA%E5%BD%95%E7%89%87?start='
    intervaltime=0.5
    urllist=getMoiveUrl(Janpeneseurl,intervaltime)
    getDatelist(intervaltime,urllist)


main()