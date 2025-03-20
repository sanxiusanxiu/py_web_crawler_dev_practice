from PIL import Image
import numpy as np

image = Image.open('ocr_base.png')
print(np.asarray(image).shape)
print(image.mode)

# (38, 112, 4)
# RGBA
