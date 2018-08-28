import pymysql

db = pymysql.connect(host='localhost',user='root',passwd='1023',db='TESTBE')

cursor = db.cursor()

sql="DELETE FORM EMPLOYEE WHERE AGE > '%d' "%(20)

try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()

db.close()