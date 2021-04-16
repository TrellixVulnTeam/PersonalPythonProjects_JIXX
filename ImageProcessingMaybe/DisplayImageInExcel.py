from PIL import Image
import numpy as np
import xlsxwriter
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename


Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
print(filename)

im = Image.open(filename)

array = np.zeros([im.height, im.width, 3], dtype=np.uint8)

oldPercentDone = 0

for x in range(im.width):
    for y in range(im.height):
        array[y,x] = im.getpixel((x,y))
        percentDone = round(float(x/im.width) * 100)
        if (percentDone > oldPercentDone):
            oldPercentDone = percentDone
            print(str(percentDone) + "% done getting pixels")



img = Image.fromarray(array)
img.save('test2.png')


workbook = xlsxwriter.Workbook('Image.xlsx')
worksheet = workbook.add_worksheet()

oldPercentDone = 0
for x in range(im.width):
    for y in range(im.height):
        colorHexR = hex(array[y, x, 0])
        colorHexG = hex(array[y, x, 1])
        colorHexB = hex(array[y, x, 2])
        colorHexR = colorHexR[2:]
        colorHexG = colorHexG[2:]
        colorHexB = colorHexB[2:]
        if len(colorHexR) == 1:
            colorHexR = "0" + colorHexR
        if len(colorHexG) == 1:
            colorHexG = "0" + colorHexG
        if len(colorHexB) == 1:
            colorHexB = "0" + colorHexB

        cell_format = workbook.add_format()
        cell_format.set_bg_color(colorHexR + "0000")
        worksheet.write(y*3, x, '', cell_format)

        cell_format = workbook.add_format()
        cell_format.set_bg_color("00" + colorHexG + "00")
        worksheet.write(y * 3 + 1, x, '', cell_format)

        cell_format = workbook.add_format()
        cell_format.set_bg_color("0000" + colorHexB)
        worksheet.write(y * 3 + 2, x, '', cell_format)

        percentDone = round(float(x / im.width) * 100)
        if (percentDone > oldPercentDone):
            oldPercentDone = percentDone
            print(str(percentDone) + "% done formatting excel")

print('Wait until I display "Done"')
workbook.close()
print("Done")

