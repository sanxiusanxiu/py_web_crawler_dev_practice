import pymongo
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['crawler']
collection = db['students_test']

result_one = collection.delete_one({'name': 'Kevin'})
print(result_one)
print(result_one.deleted_count)
result_many = collection.delete_many({'age': {'$lt': 25}})
print(result_many.deleted_count)

"""
PyMongo 还提供了一些组合方法

如 find_one_and_delete()、find_one_and_replace() 和 find_one_and_update()

它们是查找后删除、替换和更新操作，其用法与上述方法基本一致

另外，还可以对索引进行操作，相关方法有 create_index()、create_indexes() 和 drop_index() 等

"""