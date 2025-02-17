import requests

def api_render_simple():
    # render.html用于获取JavaScript渲染的页面的HTML代码
    url = 'http://localhost:8050/render.html?url=https://www.baidu.com'
    response = requests.get(url)
    print(response.text)

def api_render_params():
    # 此接口还可以指定其他参数，比如通过wait指定等待秒数，以确保页面完全加载出来，可以增加等待时间
    # 还支持代理设置、图片加载设置、请求头设置、请求方法设置
    url = 'http://localhost:8050/render.html?url=https://www.baidu.com&amp;wait=3'
    response = requests.get(url)
    print(response.text)

# api_render_simple()
api_render_params()
