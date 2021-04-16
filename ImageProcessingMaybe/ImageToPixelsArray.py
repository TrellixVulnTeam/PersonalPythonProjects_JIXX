from PIL import Image
import numpy as np

im = Image.open('testrgb.png')

array = np.zeros([im.height, im.width, 3], dtype=np.uint8)

oldPercentDone = 0

for x in range(im.width):
    for y in range(im.height):
        array[y,x] = im.getpixel((x,y))
        percentDone = round(float(x/im.width) * 100)
        if (percentDone > oldPercentDone):
            oldPercentDone = percentDone
            print(str(percentDone) + "% done")

print(array)

img = Image.fromarray(array)
img.save('test1.png')


# px = im.load()
# print (px[40000,40000])
# px[4,4] = (0,0,0)
# print (px[4,4])

