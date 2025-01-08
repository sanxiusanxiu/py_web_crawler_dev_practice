import pymysql

db = pymysql.connect(host='localhost', port=3306, user='root', passwd='000000')
cursor = db.cursor()
cursor.execute('SELECT VERSION()')
data = cursor.fetchone()
print('数据库版本：', data)
cursor.execute("CREATE DATABASE crawler DEFAULT CHARACTER SET utf8")
db.close()
