from pyquery import PyQuery as pq
import requests

html = '''
<div>
    <ul>
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
'''
# 字符串初始化  # 最常用的初始化方式
doc = pq(html)
print(doc('li'))

# URL初始化
# PyQuery 对象会首先请求这个 URL，然后用得到的 HTML 内容完成初始化
doc2 = pq(url='https://cuiqingcai.com')
print(doc2('title'))
# 这其实就相当于用网页的源代码以字符串的形式传递给 PyQuery 类来初始化
doc3 = pq(requests.get('https://cuiqingcai.com').text)
print(doc3('title'))

# 文件初始化
def init_from_file():
    doc4 = pq(filename='pyquery_test.html')
    print(doc4('li'))

init_from_file()
