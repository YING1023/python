import pymysql
# 打开数据库连接
db = pymysql.connect(host='localhost',user='root',passwd='1023',db='TESTBE')
# 使用 cursor() 方法创建一个游标对象 cursor
cur = db.cursor()
# 使用 execute()  方法执行 SQL 查询
cur.execute("SELECT * FROM EMPLOYEE")
# 使用 fetall() 方法获取全部数据.
data = cur.fetchall()

for r in data:
    print(r)

db.close()
cur.close()

