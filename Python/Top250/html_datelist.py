import requests
from bs4 import BeautifulSoup
import re
try:
    list = []
    url='https://movie.douban.com/subject/1295644/'
    r= requests.get(url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    html = r.text
    soup = BeautifulSoup(html,'html.parser')

    top = soup.find(name= 'span',attrs={'class':'top250-no'})
    top = top.string

    title = soup.find(name= 'span',attrs={'property':'v:itemreviewed'})
    title =title.string

    point = soup.find(name= 'strong',attrs={'class':'ll rating_num'})
    point = point.string

    people = soup.find(name='span', attrs={'property': 'v:votes'})
    people = people.string

    time = soup.find(name= 'span',attrs={'property':'v:initialReleaseDate'})
    time=time.string

    length = soup.find(name='span', attrs={'property': 'v:runtime'})
    length = length.string

    director = soup.find(name='a', attrs={'rel': 'v:directedBy'})
    director = director.string
    '''
    screenwriter = soup.find(name='span', attrs={'class': 'attrs'})
    screenwriter = screenwriter.string
    '''
    list.append([top, title, point, people, time, length, director])
    tplt = '{:^4}\t{:16}\t{:4}\t{:8}\t{:16}\t{:14}\t{:8}'
    print(tplt.format('top', '电影名称', '评分', '评分人数', '上映时间', '时长', '导演'))

    '''测试
    print(top)
    print(title)
    print(point)
    print(people)
    print(time)
    print(length)
    print(director)
    '''
    for g in list:
        print(tplt.format(g[0],g[1],g[2],g[3],g[4],g[5],g[6]))
    path = 'G:\Python\Top250\list.txt'
    with open(path,'a',encoding='utf-8') as f:
        f.write(str(list) + '\n')


except:
    print('please change')
