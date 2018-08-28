import requests
import re

url = "https://www.zhihu.com/topics"
try:
    kv = {'User-Agent':'Mozilla/5.0'}
    r = requests.get(url,headers=kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    html = r.text


    topics = re.findall(r'<a href="#.*">.*<\/a>', html)
    list=[]
    path='G:\zhihu'




    for topic in topics:
        top = re.findall(r'>.*<', topic)
        top = str(top)#看错误提醒发现是str问题
        list = re.findall(r'\w+',top)
        print(list)

    with open(path, 'a', encoding='utf-8') as f:  # open的属性和方法有什么意思
        f.write(str(list))


except:
    print("请尝试别的解决方法")