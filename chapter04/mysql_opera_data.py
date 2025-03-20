import pymysql

# 插入实例
def pymysql_insert_demo():
    id = '20210001'
    user = 'Bob'
    age = 20

    db = pymysql.connect(host='localhost', user='root', password='000000', port=3306, db='crawler')
    cursor = db.cursor()
    sql = 'INSERT INTO students_test(id, name, age) values(% s, % s, % s)'

    # 插入、更新和删除操作都是对数据库进行更改的操作，而更改操作都必须为一个事务，所以这些操作的标准写法如下
    try:
        cursor.execute(sql, (id, user, age))
        db.commit()
    except:
        db.rollback()

    db.close()

# 动态插入
def pymysql_insert_demo2():
    data = {
        'id': '20210002',
        'name': 'Jack',
        'age': 23
    }
    # 首先，需要构造插入的字段 id、name 和 age，这里只需要将 data 的键名拿过来，然后用逗号分隔即可
    table = 'students_test'
    # 所以 ', '.join(data.keys()) 的结果就是 id, name, age
    keys = ', '.join(data.keys())
    # 然后需要构造多个 % s 当作占位符，有几个字段构造几个即可
    # 定义长度为 1 的数组 ['% s']，用乘法扩充为 ['% s', '% s', '% s']，最终变成 % s, % s, % s
    values = ', '.join(['% s'] * len(data))

    db = pymysql.connect(host='localhost', user='root', password='000000', port=3306, db='crawler')
    cursor = db.cursor()
    # 使用字符串的 format 方法将表名、字段名和占位符构造出来
    sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table, keys=keys, values=values)
    try:
        if cursor.execute(sql, tuple(data.values())):
            print('Successful')
            db.commit()
    except:
        print('Failed')
        db.rollback()

    db.close()

def pymysql_update_demo():
    db = pymysql.connect(host='localhost', user='root', password='000000', port=3306, db='crawler')
    cursor = db.cursor()
    sql = 'UPDATE students_test SET age = %s WHERE name = %s'
    try:
        cursor.execute(sql, (25, 'Bob'))
        db.commit()
    except:
        db.rollback()

    db.close()

def pymysql_update_demo2():
    db = pymysql.connect(host='localhost', user='root', password='000000', port=3306, db='crawler')
    cursor = db.cursor()

    data = {
        'id': '20210001',
        'name': 'Bob',
        'age': 21
    }

    table = 'students_test'
    keys = ', '.join(data.keys())
    values = ', '.join(['%s'] * len(data))

    # 创建插入语句
    sql = f'INSERT INTO {table} ({keys}) VALUES ({values})'

    # 创建更新部分
    update = ', '.join([f"{key} = VALUES({key})" for key in data])
    sql += f' ON DUPLICATE KEY UPDATE {update}'

    try:
        # 如果数据存在，则更新数据；如果数据不存在，则插入数据
        if cursor.execute(sql, tuple(data.values())):
            print('成功')
            db.commit()
    except Exception as e:
        print(f'失败: {e}')
        db.rollback()

    db.close()

def pymysql_select_demo():
    db = pymysql.connect(host='localhost', user='root', password='000000', port=3306, db='crawler')
    cursor = db.cursor()
    sql = 'SELECT * FROM students_test'
    try:
        cursor.execute(sql)
        print('总数：', cursor.rowcount)
        result_one = cursor.fetchone()
        print('剩余结果：', result_one)
        result_all = cursor.fetchall()
        print('所有结果：', result_all)
        print('结果类型：', type(result_all))
        for row in result_all:
            print(row)
    except:
        print('Error')

    db.close()

def pymysql_delete_demo():
    db = pymysql.connect(host='localhost', user='root', password='000000', port=3306, db='crawler')
    cursor = db.cursor()

    table = 'students_test'
    condition = 'age > 22'
    sql = 'DELETE FROM {table} WHERE {condition}'.format(table=table, condition=condition)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()

    db.close()

def pymysql_select_demo2():
    db = pymysql.connect(host='localhost', user='root', password='000000', port=3306, db='crawler')
    cursor = db.cursor()
    sql = 'SELECT * FROM students_test WHERE age>=20'
    try:
        cursor.execute(sql)
        print('总数：', cursor.rowcount)
        row = cursor.fetchone()
        while row:
            print(row)
            row = cursor.fetchone()
    except:
        print('Error')

    db.close()

# pymysql_insert_demo()
# pymysql_insert_demo2()
# pymysql_update_demo()
# pymysql_update_demo2()
# pymysql_select_demo()
# pymysql_delete_demo()
# pymysql_select_demo2()
