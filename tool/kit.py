import random
import time
import os


# 生成一个a~b之间的随机数
def make_random(a, b):
    random_number = random.randint(a, b)
    return random_number


# 输出文件的结构
def print_tree(dir_path, prefix=''):
    """
    打印给定目录的文件结构。
    :param dir_path: 要打印的目录路径。
    :param prefix: 用于缩进的前缀字符串。
    """
    if not os.path.isdir(dir_path):
        print('路径输入错误！不是一个目录')
        return

    if not os.listdir(dir_path):
        print(f'{prefix}└── {os.path.basename(dir_path)} (空目录)')
    else:
        files = os.listdir(dir_path)
        for i, file in enumerate(files):
            print(f"{prefix}├── {file}")
            path = os.path.join(dir_path, file)
            if os.path.isdir(path):
                if i == len(files) - 1:
                    # 最后一个元素
                    new_prefix = prefix + '    '
                else:
                    new_prefix = prefix + '|   '
                print_tree(path, new_prefix)

