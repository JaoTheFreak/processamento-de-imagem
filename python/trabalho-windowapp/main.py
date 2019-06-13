## 1) Crie um algoritmo que escale uma imagem tom de cinza com valores de pixel [0, 255]. 
## A imagem original tem 256x256. A imagem final deve ter 512x512

import cv2 as opencv
import numpy as np
from matplotlib import pyplot as plt
from tkinter import *
from tkinter import filedialog
import os

class App:

    def __init__(self, master, title, resolution, icon):

        self.__frameroot = master

        master.geometry(resolution)

        master.iconbitmap(icon)

        master.title(title)

        frame = Frame(master)

        frame.pack()

        self.scalebtn = Scale(master, from_=0, to=100, orient=VERTICAL, command=self.readscale)

        self.scalebtn.pack(side=LEFT)

        self.button = Button(frame, text="QUIT", fg="red", command=frame.quit)

        self.button.pack(side=LEFT)

        ##
        self.fileselect = Button(frame, text="File", fg="red", command=self.loadimage)

        self.fileselect.pack(side=LEFT)

        self.hi_there = Button(frame, text="Hello", command=self.say_hi)

        self.hi_there.pack(side=LEFT)



    def say_hi(self):
        print("hi there, everyone!")

    def readscale(self, value):
        value

    def loadimage(self):

        my_filetypes = [('all files', '.*'), ('text files', '.txt')]

        answer = filedialog.askopenfile(parent=self.__frameroot,
                                        initialdir=os.getcwd(),
                                        title="Selecione a imagem: ",
                                        filetypes=my_filetypes)
        print(answer)

        #self.__imageSource = opencv.imread(answer)

        #print(self.__imageSource)


def negative(imgnegative):

    (_height, _width, _levels) = imgnegative.shape

    for line in range(_height):
        for column in range(_width):
            for level in range(_levels):
                pxl = imgnegative.item(line, column, level)

                imgnegative.itemset((line, column, level), 255 - pxl)

    return imgnegative


def binary(imagetobinarize, threshold):

    (_height, _width, _levels) = imagetobinarize.shape

    for line in range(_height):
        for column in range(_width):
            pxl = threshold

            for level in range(_levels):
                pxl += imagetobinarize.item(line, column, level)

            for level in range(_levels):
                if (pxl / 3) > threshold:
                    imagetobinarize.itemset((line, column, level), 255)
                else:
                    imagetobinarize.itemset((line, column, level), 0)

    return imagetobinarize


def scale(imagetoscale, factor):

    (_height, _width, _levels) = imagetoscale.shape

    scaledimage = np.zeros((int(_height*factor), int(_width*factor), _levels), dtype=int)

    for line in range(_height):
        for column in range(_width):
            for level in range(_levels):
                pxl = imagetoscale.item(line, column, level)

                scaledline = int(line * factor)

                scaledcolumn = int(column * factor)

                if factor < 1:
                    scaledimage.itemset((scaledline, scaledcolumn, level), pxl)
                else:

                    for difline in range(int(_height*factor/_height)):
                        for difcol in range(int(_width*factor/_width)):
                            scaledimage.itemset((difline, difcol, level), pxl)

    return scaledimage


def shine(imagetoshine, deltashine):
    (_height, _width, _levels) = imagetoshine.shape

    for line in range(_height):
        for column in range(_width):
            for level in range(_levels):
                pxl = imagetoshine.item(line, column, level)

                pxlshine = int(pxl + deltashine)

                if pxlshine < 0:
                    imagetoshine.itemset((line, column, level), 0)
                elif pxlshine > 255:
                    imagetoshine.itemset((line, column, level), 255)
                else:
                    imagetoshine.itemset((line, column, level), pxlshine)

    return imagetoshine


def grayshade(imgsource):

    (_height, _width, _levels) = imgsource.shape

    imgtarget = np.zeros((_height, _width), dtype=int)

    for line in range(_height):
        for column in range(_width):

            if _levels == 3:
                redpxl = imgsource.item(line, column, 2)

                greenpxl = imgsource.item(line, column, 1)

                bluepxl = imgsource.item(line, column, 0)

                pxlgray = int(0.299 * redpxl + 0.587 * greenpxl + 0.114 * bluepxl)

                imgtarget.itemset((line, column), pxlgray)
            else:
                pxlgray = imgsource.item(line, column, 0)

                imgtarget.itemset((line, column), pxlgray)

    return imgtarget

#imgLennaBGR = opencv.imread('mulier.png')

imgLennaBGR = opencv.imread('C:\\Users\\JoaoI\\Desktop\\Processamento de Imagem\\Binarização\\mulier.png')

print(imgLennaBGR)

#b,g,r = opencv.split(imgLennaBGR)           # get b, g, r

#imgLenna = opencv.merge( [r,g,b] )     # switch it to r, g, b

#(height, width, levels) = imgLennaBGR.shape

#imgLennaScale = shine(imgLenna, 150)

root = Tk()

app = App(root, "Processamento de Imagem", "1024x768", "favicon.ico")

root.mainloop()
