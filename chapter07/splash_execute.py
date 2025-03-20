import requests
from urllib.parse import quote

def execute_base():
    # Lua 脚本
    lua = '''
    function main(splash)
        return 'hello'
    end
    '''

    # 使用 urllib.parse.quote 转码 URL，把构造的 URL 作为 lua_source 参数
    url = 'http://localhost:8050/execute?lua_source=' + quote(lua)
    response = requests.get(url)
    print(response.text)

def execute_case():
    lua = '''
    function main(splash, args)
      local treat = require("treat")
      local response = splash:http_get("https://httpbin.org/get")
    	return {
    	  html=treat.as_string(response.body),
          url=response.url,
          status=response.status
        }
    end
    '''

    url = 'http://localhost:8050/execute?lua_source=' + quote(lua)
    response = requests.get(url)
    print(response.text)

# execute_base()
# execute_case()
