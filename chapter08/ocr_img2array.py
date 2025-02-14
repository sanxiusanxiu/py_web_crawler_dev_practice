from PIL import Image
import numpy as np

image = Image.open('picture03.png')
print(np.asarray(image).shape)
print(image.mode)

# (38, 112, 4)
# RGBA
