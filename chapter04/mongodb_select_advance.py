import pymongo
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['crawler']
collection = db['students_test']

# 统计数据条数  # 较新的版本中没有这个方法了
# count = collection.find({'age': 20}).count()
count = collection.count_documents({'age': 20})
print(count)

# 排序，并传入排序的字段、升降序   pymongo.ASCENDING 表示升序， pymongo.DESCENDING 表示降序
results_sort = collection.find().sort('name', pymongo.ASCENDING)
print([result['name'] for result in results_sort])

# 用 skip() 方法进行偏移，比如偏移为 2，就是忽略前两个元素，得到第三个及以后的元素
results_offset = collection.find().sort('name', pymongo.ASCENDING).skip(2)
print([result['name'] for result in results_offset])

# 限制条数（个数）
results_limit = collection.find().sort('name', pymongo.ASCENDING).skip(2).limit(2)
print([result['name'] for result in results_limit])

"""
注意在数据库数量非常庞大的时候，如千万、亿级别，最好不要使用大的偏移量来查询数据，很可能导致内存溢出。
此时可以使用类似如下操作来查询，需要记录好上次查询的 _id：
from bson.objectid import ObjectId
collection.find({'_id': {'$gt': ObjectId('593278c815c2602678bb2b8d')}})
"""
