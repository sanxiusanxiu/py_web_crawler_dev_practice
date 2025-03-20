from urllib.robotparser import RobotFileParser

"""
urllib.robotparser.RobotFileParser(url='') 

RobotFileParser 常用的几个方法：
set_url(url)，设置 robots.txt 文件的 URL 
read()，读取和解析 robots.txt 文件，使用 robotparser 时一定要调用这个方法
parse(lines)，解析一个包含 robots.txt 文件内容的字符串列表
can_fetch(user_agent, url)，检查指定的用户代理（User-Agent）是否被 URL 允许抓取
mtime()，返回上次抓取 robots.txt 的时间
modified()，如果 robots.txt 在上次抓取后被修改，则返回 True 
"""


def robot_file_parse():
    rp = RobotFileParser()
    rp.set_url('https://www.jianshu.com/robots.txt')
    rp.read()
    # 判断网页是否可以被抓取
    print(rp.can_fetch('*', 'https://www.jianshu.com/search?q=python&page=1&type=collections'))

    # 或者这样写也可以
    rp2 = RobotFileParser('https://scrape.center/robots.txt')
    rp2.read()
    # 判断网页是否可以被抓取
    print(rp2.can_fetch('*', 'https://ssr1.scrape.center/'))


def robot_file_can_fetch():
    from urllib.request import urlopen

    rp = RobotFileParser()
    rp.parse(urlopen('https://www.baidu.com/robots.txt').read().decode('utf-8').split('\n'))

    # 判断网页是否可以被抓取
    print(rp.can_fetch('*', 'https://www.baidu.com/search?q=python&page=1&type=collections'))


# robot_file_parse()
# robot_file_can_fetch()
