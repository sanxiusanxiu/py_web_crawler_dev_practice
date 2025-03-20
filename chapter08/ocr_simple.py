import pytesseract
from PIL import Image

def number_simple():
    # 读取图片
    image = Image.open('ocr_number_simple.png')
    # 识别文字
    string = pytesseract.image_to_string(image)
    print(string)

def text_simple():
    # 读取图片
    image = Image.open('ocr_text_simple.png')
    # 识别文字
    string = pytesseract.image_to_string(image, lang="chi_sim")
    print(string)

number_simple()
text_simple()
