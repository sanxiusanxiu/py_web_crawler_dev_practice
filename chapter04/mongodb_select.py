from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['crawler']
collection = db['students_test']

result = collection.find_one({'name': 'Mike'})
print(type(result))
# 可以发现数据多了 _id 属性，这是 MongoDB 在插入过程中自动添加的
print(result)

# 也可以根据 ObjectId 来查询，此时需要使用 bson 库
from bson.objectid import ObjectId

result2 = collection.find_one({'_id': ObjectId('677cfa61639e7cf20fbb5553')})
print(result)
