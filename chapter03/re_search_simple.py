import re


def re_search_base():
    content = 'Extra stings Hello 1234567 World_This is a Regex Demo Extra stings'
    result = re.match(r'Hello.*?(\d+).*?Demo$', content)
    print(result)  # None
    result2 = re.search(r'Hello.*?(\d+).*?Demo', content)
    print(result2)


html = '''<div id="songs-list">
<h2 class="title">经典老歌</h2>
<p class="introduction">
经典老歌列表
</p>
<ul id="list" class="list-group">
<li data-view="2">一路上有你</li>
<li data-view="7">
<a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
</li>
<li data-view="4" class="active">
<a href="/3.mp3" singer="齐秦">往事随风</a>
</li>
<li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
<li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
<li data-view="5">
<a href="/6.mp3" singer="邓丽君">但愿人长久</a>
</li>
</ul>
</div>'''
# 提取class为active的li节点包含的歌手名和歌名
# 首先正则可以以l开头，找到标志符active，中间部分使用.*?匹配，然后提取singer属性值，使用括号提取，还需要匹配a节点的文本
result = re.search('<li.*?active.*?singer="(.*?)">(.*?)</a>', html, re.S)
if result:
    print(result.group(1), result.group(2))
# 如果不加标志符active就会匹配第一个符合的匹配目标
result2 = re.search('<li.*?singer="(.*?)">(.*?)</a>', html, re.S)
if result2:
    print(result2.group(1), result2.group(2))
# 如果去掉re.S就会匹配到没有换行符的第四个li节点的内容
result3 = re.search('<li.*?singer="(.*?)">(.*?)</a>', html)
if result3:
    print(result3.group(1), result3.group(2))
