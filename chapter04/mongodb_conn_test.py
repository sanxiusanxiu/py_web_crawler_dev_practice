import pymongo
from pymongo import MongoClient

# 连接 MongoDB
client = pymongo.MongoClient(host='localhost', port=27017)
# 也可以这样写
# client = MongoClient('mongodb://localhost:27017/')

# 指定数据库
db = client.crawler
# 也可以这样写
# db = client['crawler']

# 指定集合（表）
collection = db.students_test
# 也可以这样写
# collection = db['students_test']

# 插入数据
student = {
    'id': '20240104',
    'name': 'Jordan',
    'age': 27,
    'gender': 'male'
}

# 注意在 PyMongo 3.x 版本中，官方不推荐使用 insert() 方法
# result = collection.insert(student)
result = collection.insert_one(student)
# 在 MongoDB 中，每条数据都有一个_id属性唯一标识，insert() 方法会在执行后返回 _id 值
print(result)

# 同时插入多条数据
student2 = {
    'id': '20170101',
    'name': 'Dan',
    'age': 20,
    'gender': 'male'
}
student3 = {
    'id': '20170202',
    'name': 'Mike',
    'age': 21,
    'gender': 'male'
}
result_many = collection.insert_many([student2, student3])
print(result_many)
# 调用 inserted_ids 属性可以获取插入数据的 _id 列表
print(result_many.inserted_ids)
