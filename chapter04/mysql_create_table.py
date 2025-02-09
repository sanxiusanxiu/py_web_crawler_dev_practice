import pymysql

db = pymysql.connect(host='localhost', user='root', password='000000', port=3306, db='crawler')
cursor = db.cursor()
sql = ('CREATE TABLE IF NOT EXISTS students_test ('
       'id VARCHAR(255) NOT NULL, name VARCHAR(255) NOT NULL, age INT NOT NULL, PRIMARY KEY (id))')
cursor.execute(sql)
db.close()
