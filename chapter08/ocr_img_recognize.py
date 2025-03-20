from PIL import Image
import numpy as np
import pytesseract

image = Image.open('ocr_base.png')

# 将图片二值化处理
# image = image.convert('1')

# 将图片转化成灰度图像
image = image.convert('L')

# 设置灰度的阈值
threshold = 50
# 将图片转化成数组
array = np.array(image)
# 对数组进行筛选和处理，大于阈值的设置为 255，小于阈值的设置为 0
array = np.where(array > threshold, 255, 0)
image = Image.fromarray(array.astype('uint8'))
# image.show()

print(pytesseract.image_to_string(image))  # b32d
