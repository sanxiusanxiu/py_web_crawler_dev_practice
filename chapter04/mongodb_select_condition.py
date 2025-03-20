from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['crawler']
collection = db['students_test']

results = collection.find({'age': 20})
print(results)
for result in results:
    print(result)

# 查询年龄大于 20 的数据
results_age = collection.find({'age': {'$gt': 20}})
for result in results_age:
    print(result)

"""
# 比较符号
| $lt  | 小于       | {'age': {'$lt': 20}}        |
| $gt  | 大于       | {'age': {'$gt': 20}}        |
| $ne  | 不等       | {'age': {'$ne': 20}}        |
| $lte | 小于等于    | {'age': {'$lte': 20}}       |
| $gte | 大于等于    | {'age': {'$gte': 20}}       |
| $in  | 在范围内    | {'age': {'$in': [20, 23]}}  |
| $nin | 不在范围    | {'age': {'$nin': [20, 23]}} |
"""

# 还可以进行正则匹配查询，例如查询名字以 M 开头的学生数据
results_m_start = collection.find({'name': {'$regex': '^M.*'}})

"""
# 功能符号
| $type   | 类型判断  | {'age': {'$type': 'int'}}                         | age 的类型为 int
| $exists | 是否存在  | {'name': {'$exists': True}}                       | name 属性存在
| $text   | 文本查询  | {'$text': {'$search': 'Mike'}}                    | text 类型的属性中包含 Mike 字符串
| $where  | 高级查询  | {'$where': 'obj.fans_count == obj.follows_count'} | 自身粉丝数等于关注数
| $regex  | 正则      | {'name': {'$regex': '^M.*'}}                      | name 以 M 开头
| $mod    | 数字模操作 | {'age': {'$mod': [5, 0]}}                         | 年龄模 5 余 0
"""
