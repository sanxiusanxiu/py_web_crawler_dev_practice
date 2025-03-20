import csv

# 写入
def csv_write_demo():
    with open('csv_simple.csv', 'w') as csv_file:
        # writer = csv.writer(csv_file)
        # writer.writerow(['id', 'name', 'age'])
        # writer.writerow(['10001', 'Mike', 20])
        # writer.writerow(['10002', 'Bob', 22])
        # writer.writerow(['10003', 'Jordan', 21])

        # # 如果想修改列与列之间的分隔符，可以传入 delimiter 参数
        # writer = csv.writer(csv_file, delimiter='|')
        # writer.writerow(['id', 'name', 'age'])
        # writer.writerow(['10001', 'Mike', 20])
        # writer.writerow(['10002', 'Bob', 22])
        # writer.writerow(['10003', 'Jordan', 21])

        # # 也可以调用 writerows 方法同时写入多行，此时参数是二维列表
        # writer = csv.writer(csv_file)
        # writer.writerow(['id', 'name', 'age'])
        # writer.writerows([['10001', 'Mike', 20], ['10002', 'Bob', 22], ['10003', 'Jordan', 21]])

        # 一般情况下，爬虫爬取的都是结构化数据，会用字典来表示
        # csv 库提供了字典的写入方式
        fieldnames = ['id', 'name', 'age']
        # 先定义 3 个字段，将其传给 DictWriter 初始化字典写入对象
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        # 调用 writeheader 方法先写入头信息，然后再调用 writerow 方法传入相应字典
        writer.writeheader()
        writer.writerow({'id': '10001', 'name': 'Mike', 'age': 18})
        writer.writerow({'id': '10002', 'name': 'Bob', 'age': 22})
        writer.writerow({'id': '10003', 'name': 'Jordan', 'age': 21})

    # 如果想追加写入，需要将 open 函数的第二个参数改成 a
    with open('csv_simple.csv', 'a') as csv_file:
        fieldnames = ['id', 'name', 'age']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writerow({'id': '10004', 'name': 'Durant', 'age': 20})

# 写入中文
def csv_write_zh():
    # 如果要写入中文内容的话，可能会遇到字符编码的问题
    with open('csv_simple.csv', 'a', encoding='utf-8') as csv_file:
        fieldnames = ['id', 'name', 'age']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writerow({'id': '10005', 'name': '李明', 'age': 23})

# 读取文件
def csv_read_file():
    # with open('./csv_simple.csv', 'r', encoding='utf-8') as csv_file:
    #     reader = csv.reader(csv_file)
    #     for row in reader:
    #         print(row)

    import pandas as pd
    df = pd.read_csv('csv_simple.csv')
    print(df)

# csv_write_demo()
# csv_write_zh()
# csv_read_file()
