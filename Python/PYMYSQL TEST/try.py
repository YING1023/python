import pymysql

db = pymysql.connect(host='localhost',user='root',passwd='1023',db='TESTBE')

cursor = db.cursor()

#注意values 后面是s
sql ='select age from employee'

try:
    cursor.execute(sql)
    results = cursor.fetchall()
    for i in results:
        print('age=%d' % (i))
    db.commit()
except:
    db.rollback()

db.close()