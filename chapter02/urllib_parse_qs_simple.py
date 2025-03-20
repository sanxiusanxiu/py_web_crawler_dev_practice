from urllib.parse import parse_qs

query = 'name=Thomas&age=24'
# {'name': ['Thomas'], 'age': ['24']}
print(parse_qs(query))
