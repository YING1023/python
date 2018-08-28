import pymysql

#链接数据库
db = pymysql.connect(host='localhost',user='root',passwd='1023',db='TESTBE')

#用cursor（）方法获取操作游
cursor = db.cursor()

#使用execute（） 方法执行 SQL，如果表存在则删除
cursor.execute('DROP TABLE IF EXISTS EMPLOYEE')

#设置预处理语句
sql ='''CREATE TABLE EMPLOYEE(
        FIRST_NAME CHAR(20) NOT NULL,
        LAST_NAME CHAR(20),
        AGE INT,
        SEX CHAR(1),
        INCOME FLOAT)'''

cursor.execute(sql)

#关闭数据库连接
db.close()
