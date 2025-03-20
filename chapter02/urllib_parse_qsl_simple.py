from urllib.parse import parse_qsl

query = 'name=Michael&age=20'
# [('name', 'Michael'), ('age', '20')]
print(parse_qsl(query))
