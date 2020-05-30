import tkinter as tk
from point import *
from PIL import Image, ImageTk
from funcs import *
import time
from datetime import datetime
from math import sin, cos, pi

mas = []
lines = []
IMGSIZEX = 600
IMGSIZEY = IMGSIZEX
isLocked = True
localFirstPoint = []
newFigureLen = 0
tmp = None
zPixelPoint = ()
lineFlag = False
lineExistPoint = False
figureFlag = False

'''
whiteColor = Color(255, 255, 255)
redColor = Color(255, 0, 0)
blackColor = Color(1, 1, 1)
greenColor = Color(0, 255, 0)
blueColor = Color(0, 0, 255)
purpleColor = Color(166, 0, 255)
yellowColor = Color(247, 255, 0)
'''
whiteColor = "white"
redColor = "red"
blackColor = "black"
greenColor = "green"
blueColor = "blue"
purpleColor = "purple"
yellowColor = "yellow"







def colorRecognizer():
    color = typeDrawing.get()
    if color == "Синий":
        return blueColor
    elif color == "Красный":
        return redColor
    elif color == "Зеленый":
        return greenColor
    elif color == "Фиолетовый":
        return purpleColor
    elif color == "Жёлтый":
        return yellowColor
    else:
        return blackColor


def clearCanvasField():
    global mas, img, image_tk, isLocked
    canvasField.delete("all")
    mas.clear()
    img = Image.new('RGB', (IMGSIZEX, IMGSIZEY), "white")
    image_tk = ImageTk.PhotoImage(img)
    canvasField.create_image(img.size[0] // 2, img.size[1] // 2, image=image_tk)
    isLocked = True


def mouseClick(event):
    global isLocked, localFirstPoint, mas, newFigureLen, lineFlag,\
        zPixelPoint, figureFlag, lineExistPoint, lines, tmp
    color = colorRecognizer()
    x, y = int(event.x), int(event.y)
    #print(x, y)
    if typeDrawing.get() == "Отрезок":
        if lineExistPoint:
            lineExistPoint = False
            lines.append((tmp, Point(x=x, y=y)))
            lineDrawer(tmp, Point(x=x, y=y), canvasField, color)
        else:
            lineExistPoint = True
            tmp = Point(x=x, y=y)
    else:
        if isLocked:
            localFirstPoint = Point(x, y)
            mas.append(localFirstPoint)
            isLocked = False
            newFigureLen = 0
        else:
            if newFigureLen == 0:
                mas.append(Point(x, y))
                lineDrawer(Point(x, y), localFirstPoint, canvasField, color)
                newFigureLen += 1
            else:
                l = len(mas) - 1
                mas.append((Point(x=x, y=y)))
                lineDrawer(Point(x=x, y=y), mas[l], canvasField, color)
                newFigureLen += 1


def fakeMouseClick(x, y):
    pass


def lock():
    global isLocked, localFirstPoint, mas
    color = colorRecognizer()
    if isLocked:
        return
    else:
        l = len(mas) - 1
        lineDrawer(localFirstPoint, mas[l], canvasField, color)
        isLocked = True
        print(convex(mas))


def redrawEdges(canvas, color):
    global mas
    for edge in mas:
        lineDrawer(edge[0], edge[1], edge[2], edge[3], canvas, color)


def lineBtnClicked():
    global lineFlag
    lineFlag = True


def figureBtnCliced():
    global figureFlag
    figureFlag = True

def mainfunc():
    global lines
    norm = convex(mas)
    for line in lines:
        cyrus_beck(line, mas, norm, canvasField)


img = Image.new('RGB', (IMGSIZEX, IMGSIZEY), "white")

#########################################################################
##############################MAIN#######################################
#########################################################################

root = tk.Tk()
canvasField = tk.Canvas(root, width=img.size[0], height=img.size[1])
canvasField.pack()
image_tk = ImageTk.PhotoImage(img)
canvasField.create_image(img.size[0] // 2, img.size[1] // 2, image=image_tk)

canvasField.bind("<Button-1>", mouseClick)
# canvasField.bind("<Button-2>", testfunc)

typeDrawing = tk.StringVar()
typeDrawing.set("Отрезок")
typeMenu = tk.OptionMenu(root, typeDrawing, "Отрезок", "Отсекатель")
typeMenu.pack(side="right")
dynamic = tk.IntVar()
drawBtn = tk.Button(text="Поехали", command=mainfunc).pack(side="right")
clearBtn = tk.Button(text="Очистить", command=clearCanvasField).pack(side="right")
lockBtn = tk.Button(text="Замкнуть", command=lock).pack(side="right")
zatPixelButton = tk.Button(text="Ввести затравочный пиксел", command=lineBtnClicked).pack(side="right")
circleBtn = tk.Button(text="Окружность", command=figureBtnCliced).pack(side="right")
dynamicCheckbutton = tk.Checkbutton(text="С задержкой", variable=dynamic).pack(side="right")



root.mainloop()
