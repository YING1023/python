import requests
import re
from bs4 import BeautifulSoup
def getHTMLText(url):
    try:
        kv = {'User-Agent':'Mozilla/5.0'}
        r = requests.get(url,headers=kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("请尝试别的解决方法")

def getList(html):
    try:
        list=[]
        soup = BeautifulSoup(html, 'html.parser')
        li = soup.find_all('li',attrs={"class":"zm-topic-cat-item"})
        for l in li :
            i=re.findall(r'#\w+',str(l))
            list.append(re.findall(r'\w+',str(i)))

        print(list)
        return list

    except:
        print( 'getList出错')

def infoTop(list):
    try:
        path = 'G:/zhihu/zhihutop.txt'
        with open(path, 'a', encoding='utf-8') as f:
            f.write(str(list) )
    except:
        print( 'info出错')





def main():
    url = "https://www.zhihu.com/topics"
    html=getHTMLText(url)
    list = getList(html)
    infoTop(list)
main()