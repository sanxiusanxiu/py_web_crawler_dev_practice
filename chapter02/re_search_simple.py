import re


def re_search_simple():
    content = 'Extra stings Hello 1234567 World_This is a Regex Demo Extra stings'

    # match 更适合检测某个字符串是否符合某个正则表达式的规则
    result = re.match(r'Hello.*?(\d+).*?Demo$', content)
    # None
    print(result)

    # search 在匹配时会扫描整个字符串，然后返回第一个匹配成功的结果
    result2 = re.search(r'Hello.*?(\d+).*?Demo', content)
    # <re.Match object; span=(13, 53), match='Hello 1234567 World_This is a Regex Demo'>
    print(result2)


def re_search_base():
    # 提取 class 为 active 的 li 节点包含的歌手名和歌名
    html = '''
    <div id="songs-list">
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
    </div>
    '''

    # 首先正则可以以 li 开头，找到标志符 active，中间部分使用 .*? 匹配，然后提取 singer 属性值，使用括号提取，还需要匹配 a 节点的文本
    result = re.search(r'<li.*?active.*?singer="(.*?)">(.*?)</a>', html, re.S)
    if result:
        # 齐秦 往事随风
        print(result.group(1), result.group(2))

    # 如果不加标志符 active 就会匹配第一个符合的匹配目标
    result2 = re.search('<li.*?singer="(.*?)">(.*?)</a>', html, re.S)
    if result2:
        # 任贤齐 沧海一声笑
        print(result2.group(1), result2.group(2))

    # 如果去掉 re.S 就会匹配到没有换行符的第四个 li 节点的内容
    result3 = re.search('<li.*?singer="(.*?)">(.*?)</a>', html)
    if result3:
        # beyond 光辉岁月
        print(result3.group(1), result3.group(2))

# re_search_simple()
# re_search_base()
