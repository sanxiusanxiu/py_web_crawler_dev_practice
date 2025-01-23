import requests

from urllib.parse import urljoin

from chapter03.urlencode_simple import params

base_url = 'https://login3.scrape.center/'
login_url = urljoin(base_url, '/api/login')
index_url = urljoin(base_url, '/api/book')
username = 'admin'
password = 'admin'

response_login = requests.post(login_url, json={
    'username': username,
    'password': password
})
data = response_login.json()
print('Response JSON: ', data)

jwt = data.get('token')
print('JWT: ', jwt)

header = {
    'Authorization': f'jwt {jwt}'
}
response_index = requests.get(index_url, params={
    'limit': 18,
    'offset': 0
}, headers=header)

print('状态码：', response_index.status_code)
print('URL: ', response_index.url)
print('Data: ', response_index.json())
