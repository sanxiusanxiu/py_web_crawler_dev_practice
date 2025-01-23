import pytesseract
from PIL import Image
import numpy as np

image = Image.open('captcha2.png')
print(np.asarray(image).shape)
print(image.mode)
