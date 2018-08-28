import requests
import time


def save(school_datas):
    for data in school_datas:
        # print(data)
        year = data['year']
        province = data['province']
        type = data['type']
        bath = data['bath']
        score = data['score']
        print(province, year, type, bath, score)

def Timeinterval(interval):
    try:
        time_remaining = interval
        print("[%s] %s" % (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), "start"))
        time.sleep(time_remaining)
        print("[%s] %s" % (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), "stop"))
    except:
        print("错误")

for i in range(1, 34):
    Timeinterval(1)
    print("第%s页=====================" % str(i))
    # url = "http://data.api.gkcx.eol.cn/soudaxue/queryProvince.html?messtype=jsonp&url_sign=queryprovince&province3=&year3=&page=1&size=100&luqutype3=&luqupici3=&schoolsort=&suiji=&callback=jQuery1830426658582613074_1469201131959&_=1469201133189"
    data = requests.get("http://data.api.gkcx.eol.cn/soudaxue/queryProvince.html", params={"messtype": "json",  "page": str(i)}).json()
    print("每一页信息条数——>", len(data['school']))
    print("全部信息条数——>", data["totalRecord"]['num'])
    school_datas = data["school"]
    save(school_datas)
