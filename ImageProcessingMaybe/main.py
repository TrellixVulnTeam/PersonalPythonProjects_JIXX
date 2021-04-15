import numpy as np
from PIL import Image

width = 200
height = 100

array = np.zeros([height, width, 3], dtype=np.uint8)
array[:,:100] = [255, 128, 0] #Orange left side
array[:,100:] = [0, 0, 255]   #Blue right side


img = Image.fromarray(array)
img.save('testrgb.png')