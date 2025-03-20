import pytesseract
from PIL import Image

image = Image.open('ocr_base.png')
result = pytesseract.image_to_string(image)
print(result)  # -b32d.
