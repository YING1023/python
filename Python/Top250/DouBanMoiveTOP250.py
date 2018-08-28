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

def getMoiveUrl(url,interval,list):
    try:
        list=[]
        for i in range(10):
            TimeInterval(interval)
            html = getHtmlText(url + str(i * 25) + '&filter=')
            a = re.findall(r'https://movie.douban.com/subject/\d+/">', html)
            for i in a:
                c = i[:-2]
                list.append(c)
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

                top = soup.find(name='span', attrs={'class': 'top250-no'})
                top = top.string

                title = soup.find(name='span', attrs={'property': 'v:itemreviewed'})
                title = title.string

                point = soup.find(name='strong', attrs={'class': 'll rating_num'})
                point = point.string

                people = soup.find(name='span', attrs={'property': 'v:votes'})
                people = people.string

                time = soup.find(name='span', attrs={'property': 'v:initialReleaseDate'})
                time = time.string

                length = soup.find(name='span', attrs={'property': 'v:runtime'})
                try:
                    length = length.string
                except:
                    length = 'unlength'

                director = soup.find(name='a', attrs={'rel': 'v:directedBy'})
                try:
                    director = director.string
                except:
                    director='unkonw'
                '''
                screenwriter = soup.find(name='span', attrs={'class': 'attrs'})
                screenwriter = screenwriter.string
                '''
                Datelist.append([top, title, point, people, time, length, director])




        tplt = '{:4}\t{:16}\t{:4}\t{:8}\t{:16}\t{:14}\t{:8}'
        print(tplt.format('top', '电影名称', '评分', '评分人数', '上映时间', '时长', '导演'))
        for g in Datelist:
            if g[0] == 1:
                print('链接失效，原链接为',g[1])
            else:
                print(tplt.format(g[0], g[1], g[2], g[3], g[4], g[5], g[6]))
        path = 'G:\Python\Top250\Top250.txt'
        with open(path, 'a', encoding='utf-8') as f:
            for i in Datelist:
                f.write(str(i) + '\n')
        print('打印完毕')





    except:
        traceback.print_exc()


    '''
def printlist(list):
    try:
        tplt = '{:^4}\t{:16}\t{:4}\t{:8}\t{:16}\t{:14}\t{:8}'
        print(tplt.format('top', '电影名称', '评分', '评分人数', '上映时间', '时长', '导演'))
        for g in list:
            print(tplt.format(g[0],g[1],g[2],g[3],g[4],g[5],g[6]))
    except:
        print('输出错误')

    '''



#def WriteDate(path):


def main():
    SETurl = "https://movie.douban.com/top250?start="
    SETinterval = 0.5
    Urllist=[]
    Dateurl=getMoiveUrl(SETurl,SETinterval,Urllist)
    print('电影链接获得完成')
    getDatelist(SETinterval,Dateurl)






    path = 'G:\douban'


main()
