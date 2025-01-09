import pymongo
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['crawler']
collection = db['students_test']

# 数据更新可以使用 update_one() 和 update_many()
condition = {'name': 'Petor'}
student = collection.find_one(condition)
student['age'] = 25
# 使用 $set 操作符可以只更新 student 字典内存在的字段，不用 $set 的话，则会把之前的数据覆盖写
result_update = collection.update_one(condition, {'$set': student})
# 返回结果是 UpdateResult 类型
print('result1 -->', result_update)

# 查询年龄大于 20 的数据
condition2 = {'age': {'$gt': 20}}
# 更新条件为 {'$inc': {'age': 1}}，也就是年龄加 1，执行之后会将第一条符合条件的数据年龄加 1
result2 = collection.update_one(condition, {'$inc': {'age': 1}})
# matched_count 和 modified_count 属性，可以获得匹配的数据条数和影响的数据条数
print('result2 -->', result2.matched_count, result2.modified_count)

# 如果调用 update_many() 方法，所有符合条件的数据都会更新
condition3 = {'age': {'$gt': 20}}
result3 = collection.update_many(condition, {'$inc': {'age': 1}})
print('result3 -->', result3)
print(result3.matched_count, result3.modified_count)
