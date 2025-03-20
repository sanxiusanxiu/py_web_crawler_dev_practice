import requests
from requests.auth import HTTPBasicAuth


# 身份认证
def requests_auth_base():
    r = requests.get('https://ssr3.scrape.center/', auth=HTTPBasicAuth('admin', 'admin'))
    print(r.status_code)


# 身份认证简写
def requests_auth_abbreviation():
    r = requests.get('https://ssr3.scrape.center/', auth=('admin', 'admin'))
    print(r.status_code)


# requests_auth_base()
# requests_auth_abbreviation()
