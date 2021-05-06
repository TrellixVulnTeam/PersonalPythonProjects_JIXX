import os
import shutil
from tkinter import Tk     # from tkinter import Tk for Python 3.x #pretty sure these being gray means they dont matter
from tkinter.filedialog import askopenfilename
from tkinter import filedialog
from tkinter import *



print("Select the directory you would like to search.")
root = Tk()
root.withdraw()
fromFile = filedialog.askdirectory()

print("Select the directory you would like to move files to.")
root = Tk()
root.withdraw()
toFile = filedialog.askdirectory()

stringToFind = input("What string do you want to look for? >>>")

for filename in os.listdir(fromFile):
    if filename.endswith(".txt") or filename.endswith(".qan"): #dunno how to work with qan #nvm i do bc im the bomb
        path = os.path.join(fromFile, filename)
        print("\n\n\n Searching " + path)

        file = open(path, "r")
        flag = 0
        index = 0

        for line in file:
            index += 1
            if stringToFind in line:
                flag = 1
                break
        if flag == 0:
            print("String: '" + stringToFind + "' not found in " + path + ".")
            file.close()
        else:
            print("String found in line: " + str(index) + " **************************************")
            file.close()
            #os.rename(path, toFile) #these bad boys aren't needed as far as I can tell.
            shutil.move(path, toFile)
            #os.replace(path, toFile)

    else:
        continue