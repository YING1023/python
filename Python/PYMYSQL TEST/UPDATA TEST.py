import pymysql

db = pymysql.connect(host='localhost',user='root',passwd='1023',db='TESTBE')

cursor = db.cursor()

sql=" UPDATE EMPLOYEE SET AGE = AGE + 1  WHERE SEX = '%c' "%('M')

try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()

db.close()