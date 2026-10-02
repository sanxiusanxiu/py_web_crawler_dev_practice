import json
import urllib.request
import urllib.parse

url = 'https://fanyi.baidu.com/sug/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/2010010 Firefox/62.0'
}
# post请求的表单数据，对perfect进行翻译
formData = {
    "kw": "perfect"
}
request = urllib.request.Request(url, headers=headers)
# 把字符串变成二进制并传入表单数据中
response = urllib.request.urlopen(request, urllib.parse.urlencode(formData).encode())
# 把结果变成中文（使用Unicode解码）
responseData = json.loads(response.read().decode("unicode_escape"))
showDatas = responseData.get("data")[0].get("v")
print(showDatas)
