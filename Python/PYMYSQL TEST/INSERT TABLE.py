import pymysql

db = pymysql.connect(host='localhost',user='root',passwd='1023',db='TESTBE')

cursor = db.cursor()

sql = '''INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME,AGE,SEX,INCOME)
         VALUES('Mac','Mohan',20,'M',2000)'''

try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()

db.close()
