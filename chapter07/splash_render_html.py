import requests

"""
Splash 对象属性

args 属性，用于获取加载时配置的参数，比如 URL。如果是 GET 请求，还可以获取 GET 请求参数；如果是 POST 请求，可以获取表单提交的数据
js_enabled 属性，Splash 执行 JavaScript 代码的开关，默认为 true 
resource_timeout 属性，用于设置加载的超时时间，单位是秒，如果设置为 0 或 nil（类似 Python 中的 None），代表不检测超时
images_enabled 属性，用于设置是否加载图片，默认为 true，禁用该属性后可以节省网络流量并提高网页加载速度，但是禁用图片加载可能会影响 JavaScript 渲染，因为禁用图片之后，外层 DOM 节点的高度会受影响，进而影响 DOM 节点的位置
plugins_enabled 属性，用于控制是否开启浏览器插件（如 Flash 插件），默认为 false 
scroll_position 属性，用于控制页面上下滚动或左右滚动
"""

def api_render_simple():
    # render.html 用于获取 JavaScript 渲染的页面的 HTML 代码
    url = 'http://localhost:8050/render.html?url=https://www.baidu.com'
    response = requests.get(url)
    print(response.text)

def api_render_params():
    # 此接口还可以指定其他参数，比如通过 wait 指定等待秒数，以确保页面完全加载出来，可以增加等待时间
    # 还支持代理设置、图片加载设置、请求头设置、请求方法设置
    url = 'http://localhost:8050/render.html?url=https://www.baidu.com&amp;wait=3'
    response = requests.get(url)
    print(response.text)

# api_render_simple()
api_render_params()
