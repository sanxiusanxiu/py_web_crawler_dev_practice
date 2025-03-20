import pymysql

# 连接数据库
db = pymysql.connect(host='localhost', port=3306, user='root', passwd='000000')
# 创建游标对象
cursor = db.cursor()
# 利用游标执行 SQL 语句，获取 MySQL 的版本
cursor.execute('SELECT VERSION()')
# 调用 fetchone 方法获得第一条数据
data = cursor.fetchone()
print('数据库版本：', data)
cursor.execute("CREATE DATABASE crawler DEFAULT CHARACTER SET utf8")
# 关闭游标
db.close()
