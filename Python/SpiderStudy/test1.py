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

def getCDAList(Infourl,fpath):
    try:
        for num in range(28, 48):
            num1 = str(num)
            url = Infourl + num1 + ".html"
            html = getHTMLText(url)


            infoDict = {}
            soup =BeautifulSoup(html,"html.parser")
            p = soup.find('p',attrs={'class':'kecheng-mc'})#如何去掉打印出来的标签
            div = soup.find_all('div',attrs={'class':'padd'})#可不可以用正则表达式将文字提取出来

            key=p.string
            val=div

            print(num, p)

            infoDict[key]=val

            path = fpath +num1+str(p.string) + ".txt"

            print(path)

            with open(path,'a',encoding='utf-8') as f:#open的属性和方法有什么意思
                f.write(str(infoDict))
    except:
        return ""


def main():

    CDAurl= "http://www.cda.cn/kecheng/"
    output_file ='g:/CDA/'
    getCDAList(CDAurl,output_file)


main()