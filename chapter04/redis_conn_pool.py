from redis import StrictRedis, ConnectionPool

# 连接效果是一样的
pool = ConnectionPool(host='localhost', port=6379, db=0, password='000000')
redis = StrictRedis(connection_pool=pool)

print(redis.get('key_20250208'))

"""
# ConnectionPool还支持通过URL构建连接：

# 创建 Redis TCP 连接
url = 'redis://:000000@localhost:6379/0'
pool = ConnectionPool.from_url(url)
redis = StrictRedis(connection_pool=pool)

# 创建 Redis TCP + SSL 连接
url = 'rediss://:000000@localhost:6379/0'
pool_ssl = ConnectionPool.from_url(url)
redis_ssl = StrictRedis(connection_pool=pool_ssl)

# 创建 Redis UNIX socket 连接
url_unix = 'unix://:000000@/path/to/socket.sock?db=0'
pool_unix = ConnectionPool.from_url(url_unix)
redis_unix = StrictRedis(connection_pool=pool_unix)
"""
