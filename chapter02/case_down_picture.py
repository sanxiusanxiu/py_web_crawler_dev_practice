import requests
import os
import re
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/2010010 Firefox/62.0'
}

# 定义下载函数
def picture_download(img_path, img_title):
    dir = "D:\workspace\py_web_crawler_dev_practice\chapter02\picture"
    if not os.path.exists(dir):
        os.mkdir(dir)
    file_name = img_title.replace("/", " ").strip()
    try:
        result = requests.get(img_path.strip())
    except:
        print(img_path, "Download Failed")
    else:
        if result.status_code == 200:
            file = open(os.path.join(dir, file_name + '.jpg'), 'wb')
            file.write(result.content)
            file.close()

# 获取图片地址和标题
def img_url(url):
    result = requests.get(url, headers=headers)
    print(result)
    result.encoding = 'gbk'
    compile = re.compile(r'<img src="(.*?)" alt="(.*?)" />')
    print(compile)
    all = compile.findall(result.text)
    for item in all:
        print(item[0], item[1])
        picture_download(item[0], item[1])

def main():
    # 临时测试，只下载前两页的图片
    for i in range(1, 3):
        if i == 1:
            img_url(r'https://www.netbian.com/weimei/index.htm')
        else:
            img_url(r'https://www.netbian.com/weimei/index_%d.htm' % i)
            time.sleep(2)

if __name__ == '__main__':
    main()
