import requests
from urllib.parse import quote

def execute_base():
    # Lua脚本
    lua = '''
    function main(splash)
        return 'hello'
    end
    '''

    # 使用urllib.parse.quote转码URL，把构造的URL作为lua_source参数
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
execute_case()
