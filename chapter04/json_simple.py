import json

def json_demo():
    str = '''
    [{
        "name": "Bob",
        "gender": "male",
        "birthday": "1992-10-18"
    }, {
        "name": "Selina",
        "gender": "female",
        "birthday": "1995-10-18"
    }]
    '''

    print(type(str))  # <class 'str'>
    # 使用 loads 方法将字符串转为 JSON 对象
    data = json.loads(str)
    print(data)
    print(type(data))  # <class 'list'>

    # 通过中括号加 0 索引，可以得到第一个字典元素，再调用其键名即可得到相应的键值
    print(data[0].get('name'))  # Bob

    # 获取键值时有两种方式，一种是中括号加键名
    print(data[0]['name'])  # Bob

    # 另一种是通过 get 方法传入键名，这里推荐使用 get 方法，这样如果键名不存在，则不会报错，会返回 None
    print(data[0].get('age'))  # None
    # 另外，get 方法还可以传入第二个参数（即默认值）
    print(data[0].get('age', 25))  # 25

# 读取 JSON 文件
def json_read_file():
    with open('json_simple.json', 'r') as file:
        line = file.read()
        data = json.loads(line)
        print(data)


# 输出 JSON 文件
def json_output_file():
    data = [{
        'name': ' 王伟 ',
        'gender': ' 男 ',
        'birthday': ' 1992-10-18 '
    }]
    # with open('./json_dumps.json', 'w') as file:
    #     file.write(json.dumps(data))

    # 如果想保存 JSON 的格式，可以再加一个参数 indent，代表缩进字符个数
    # with open('./json_dumps.json', 'w') as file:
    #     file.write(json.dumps(data, indent=2))

    # 中文字符写入时会变成 Unicode 字符
    # 为了输出中文，需要指定参数 ensure_ascii=False，另外还要规定文件输出的编码
    with open('json_dumps.json', 'w', encoding='utf-8') as file:
        file.write(json.dumps(data, indent=4, ensure_ascii=False))

# json_demo()
# json_read_file()
# json_output_file()
