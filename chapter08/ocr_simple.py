import pytesseract
from PIL import Image

def simple1():
    # 读取图片
    image = Image.open('picture01.png')
    # 识别文字
    string = pytesseract.image_to_string(image)
    print(string)

def simple2():
    # 读取图片
    image = Image.open('picture02.png')
    # 识别文字
    string = pytesseract.image_to_string(image, lang="chi_sim")
    print(string)

simple2()
