import pymongo
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['crawler']
collection = db['students_test']

# 数据更新可以使用 update()
condition = {'name': 'Petor'}
student = collection.find_one(condition)
student['age'] = 25
result_update = collection.update(condition, student)
# 返回结果是字典形式，ok 代表执行成功，nModified 代表影响的数据条数
print(result_update)

# 我们也可以使用 $set 操作符对数据进行更新，代码如下：
result = collection.update(condition, {'$set': student})
