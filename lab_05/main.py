import tkinter as tk
from point import *
from PIL import Image, ImageTk
import time
from datetime import datetime

mas = []
IMGSIZEX = 650
IMGSIZEY = IMGSIZEX
whiteColor = Color(255, 255, 255)
redColor = Color(255, 0, 0)
blackColor = Color(1, 1, 1)
greenColor = Color(0, 255, 0)
blueColor = Color(0, 0, 255)
isLocked = True
localFirstPoint = []
newFigureLen = 0
tstmas = []


def cdaDrawer(xs, ys, xf, yf, canvas, color):
    if yf < ys:
        xs, ys, xf, yf = xf, yf, xs, ys

    dx = abs(xf - xs)
    dy = abs(yf - ys)

    if dx > dy:
        steep = dx
    else:
        steep = dy
    stepx = (xf - xs) / steep
    stepy = (yf - ys) / steep

    curx = xs
    cury = ys
    for i in range(int(steep + 1)):
        drawPixel(curx, cury, canvas, img, blackColor)
        curx += stepx
        cury += stepy


def edgePainter(edge, canvas, color: Color):
    xs = edge[0]
    ys = edge[1]
    xf = edge[2]
    yf = edge[3]
    if ys == yf:
        return
    if yf < ys:
        xs, ys, xf, yf = xf, yf, xs, ys
    dx = (xf - xs) / (yf - ys)
    y = ys
    endy = yf
    startx = xs
    while y < endy:
        x = startx
        while x < 500:
            changePixelColor(img, x, y, canvas, color)
            x += 1
        root.update()
        canvasField.update()
        startx += dx
        y += 1


def edgePainter2(edge, canvas, color: Color):
    xs = edge[0]
    ys = edge[1]
    xf = edge[2]
    yf = edge[3]
    if yf < ys:
        xs, ys, xf, yf = xf, yf, xs, ys

    dx = abs(xf - xs)
    dy = abs(yf - ys)

    if dx > dy:
        steep = dx
    else:
        steep = dy
    stepx = (xf - xs) / steep
    stepy = (yf - ys) / steep

    curx = xs
    cury = ys
    stable = cury
    for i in range(int(steep + 1)):
        if int(cury + stepy) - stable >= 1:
            x = curx
            while x < 500:
                changePixelColor(img, x, cury, canvasField, redColor)
                x += 1
            stable = int(cury + stepy)
        curx += stepx
        cury += stepy


def lineChangeColor(x, y, color: Color):
    for ix in range(int(x + 1), 500):
        changePixelColor(img, ix, y, canvasField, greenColor)


def colorRecognizer():
    color = colorDrawing.get()
    if color == "Синий":
        return blueColor
    elif color == "Красный":
        return redColor
    elif color == "Зеленый":
        return greenColor
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
    global isLocked, localFirstPoint, mas, newFigureLen
    color = colorRecognizer()
    x, y = event.x, event.y
    tstmas.append((x, y))
    if isLocked:
        localFirstPoint = [int(x), int(y)]
        isLocked = False
        newFigureLen = 0
    else:
        if newFigureLen == 0:
            mas.append((int(x), int(y), int(localFirstPoint[0]), int(localFirstPoint[1])))
            cdaDrawer(int(x), int(y), int(localFirstPoint[0]), int(localFirstPoint[1]), canvasField, color)
            newFigureLen += 1
        else:
            l = len(mas) - 1
            tmpx = mas[l][0]
            tmpy = mas[l][1]
            mas.append((int(x), int(y), tmpx, tmpy))
            cdaDrawer(int(x), int(y), tmpx, tmpy, canvasField, color)
            newFigureLen += 1


def fakeMouseClick(x, y):
    global isLocked, localFirstPoint, mas, newFigureLen
    if isLocked:
        localFirstPoint = [int(x), int(y)]
        isLocked = False
        newFigureLen = 0
    else:
        if newFigureLen == 0:
            mas.append((int(x), int(y), int(localFirstPoint[0]), int(localFirstPoint[1])))
            cdaDrawer(int(x), int(y), int(localFirstPoint[0]), int(localFirstPoint[1]), canvasField, blackColor)
            newFigureLen += 1
        else:
            l = len(mas) - 1
            tmpx = mas[l][0]
            tmpy = mas[l][1]
            mas.append((int(x), int(y), tmpx, tmpy))
            cdaDrawer(int(x), int(y), tmpx, tmpy, canvasField, blackColor)
            newFigureLen += 1


def lock():
    global isLocked, localFirstPoint, mas
    color = colorRecognizer()
    if isLocked:
        return
    else:
        l = len(mas) - 1
        tmpx = mas[l][0]
        tmpy = mas[l][1]
        mas.append((localFirstPoint[0], localFirstPoint[1], tmpx, tmpy))
        cdaDrawer(localFirstPoint[0], localFirstPoint[1], tmpx, tmpy, canvasField, color)
        isLocked = True


def redrawEdges(canvas, color):
    global mas
    for edge in mas:
        cdaDrawer(edge[0], edge[1], edge[2], edge[3], canvas, color)


def run1():
    color = colorRecognizer()
    for i in range(len(mas)):
        edgePainter(mas[i], canvasField, color)
    redrawEdges(canvasField, color)


def getMaxX():
    maxi = mas[0][0]
    for i in mas:
        if i[0] > maxi:
            maxi = i[0]
        if i[2] > maxi:
            maxi = i[2]
    return maxi


def run2():
    clr = colorRecognizer()
    d = dynamic.get()
    xmax = getMaxX()
    start_time = datetime.now()

    for i in range(len(mas)):
        xs, ys, xf, yf = mas[i][0], mas[i][1], mas[i][2], mas[i][3]
        if yf < ys:
            xs, ys, xf, yf = xf, yf, xs, ys
        level = ys
        while level < yf:
            x = getXIntersection(xs, ys, xf, yf, level)
            if x:
                x += 1
                while x < xmax:
                    changePixelColor(img, x, level, canvasField, clr)
                    x += 1
                if d:
                    root.update()
                    canvasField.update()
            level += 1
    print(datetime.now() - start_time)
    redrawEdges(canvasField, blackColor)


def runForTimetest():
    clr = colorRecognizer()
    xmax = getMaxX()
    start_time = datetime.now()

    for i in range(len(mas)):
        xs, ys, xf, yf = mas[i][0], mas[i][1], mas[i][2], mas[i][3]
        if yf < ys:
            xs, ys, xf, yf = xf, yf, xs, ys
        level = ys
        while level < yf:
            x = getXIntersection(xs, ys, xf, yf, level)
            if x:
                x += 1
                while x < xmax:
                    changePixelColor(img, x, level, canvasField, clr)
                    x += 1
            level += 1
    print(datetime.now() - start_time)
    redrawEdges(canvasField, blackColor)


def createRectangle(size: int):
    lx = 10
    ly = 10
    fakeMouseClick(lx, ly)
    fakeMouseClick(lx + size, ly)
    fakeMouseClick(lx + size, ly + size)
    fakeMouseClick(lx, ly + size)
    lock()


def timeTestForSize(size: int):
    print(size, ":", end=" ")
    createRectangle(size)
    runForTimetest()
    clearCanvasField()


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

colorDrawing = tk.StringVar()
colorDrawing.set("Черный")
colorMenu = tk.OptionMenu(root, colorDrawing, "Синий", "Красный", "Зеленый")
colorMenu.pack(side="right")
# drawBtn = tk.Button(text="Где закраска, Лебовски?", command=run1).pack(side="right")
drawBtn = tk.Button(text="Моя закраска", command=run2).pack(side="right")
clearBtn = tk.Button(text="Очистить", command=clearCanvasField).pack(side="right")
lockBtn = tk.Button(text="Замкнуть", command=lock).pack(side="right")
dynamic = tk.IntVar()
dynamicCheckbutton = tk.Checkbutton(text="С задержкой", variable=dynamic).pack(side="right")

# timeTestForSize(10)
# timeTestForSize(100)
# timeTestForSize(500)
# timeTestForSize(1000)

# tstmas = [(82, 272), (291, 351), (196, 264), (321, 245), (215, 210), (344, 197), (213, 121), (188, 219), (108, 141), (115, 253), (170, 253), (115, 206)]
#
# for i in range(len(tstmas) - 3):
#     fakeMouseClick(tstmas[i][0], tstmas[i][1])
# lock()
#
# for i in range(len(tstmas) - 3, len(tstmas)):
#     fakeMouseClick(tstmas[i][0], tstmas[i][1])
# lock()

# timeTestForSize(10)
# timeTestForSize(100)
# timeTestForSize(500)
# timeTestForSize(1000)
# fakeMouseClick(150, 100)
#
# fakeMouseClick(150, 350)
#
# fakeMouseClick(200, 350)
#
# fakeMouseClick(250, 275)
#
# fakeMouseClick(300, 350)
#
# fakeMouseClick(400, 350)


#
# fakeMouseClick(368, 142)
#
# fakeMouseClick(15, 165)

# lock()


root.mainloop()
print(tstmas)