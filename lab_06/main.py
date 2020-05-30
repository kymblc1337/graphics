import tkinter as tk
from point import *
from PIL import Image, ImageTk
import time
from datetime import datetime
from math import sin, cos, pi

mas = []
IMGSIZEX = 600
IMGSIZEY = IMGSIZEX
isLocked = True
localFirstPoint = []
newFigureLen = 0
zPixelPoint = ()
zPixelFlag = False
circleFlag = False
radius = 50
stack = []

whiteColor = Color(255, 255, 255)
redColor = Color(255, 0, 0)
blackColor = Color(1, 1, 1)
greenColor = Color(0, 255, 0)
blueColor = Color(0, 0, 255)
purpleColor = Color(166, 0, 255)
yellowColor = Color(247, 255, 0)


def draw4Points(xc, yc, x, y, canvas, color):
    drawPixel(xc + x, yc + y, canvas, img, color)
    drawPixel(xc + x, yc - y, canvas, img, color)
    drawPixel(xc - x, yc + y, canvas, img, color)
    drawPixel(xc - x, yc - y, canvas, img, color)


def draw8Points(xc, yc, x, y, canvas, color):
    draw4Points(xc, yc, x, y, canvas, color)
    draw4Points(xc, yc, y, x, canvas, color)


def parametricCircle(xc, yc, r, canvas, color):
    t = 0
    s = 1 / r
    while t < (pi / 4):
        x = round(r * cos(t))
        y = round(r * sin(t))
        draw8Points(xc, yc, x, y, canvas, color)
        t += s


def cdaDrawer(xs, ys, xf, yf, canvas, color):
    # canvas.create_line(xs, ys, xf, yf)
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


def colorRecognizer():
    color = colorDrawing.get()
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
    global isLocked, localFirstPoint, mas, newFigureLen, zPixelFlag, zPixelPoint, circleFlag
    color = colorRecognizer()
    x, y = int(event.x), int(event.y)
    print(x, y)
    if zPixelFlag:
        zPixelFlag = False
        zPixelPoint = (int(x), int(y))
        z = [zPixelPoint[0], zPixelPoint[1]]
        stack.append(z)
        drawPixel(x, y, canvasField, img, color)
    elif circleFlag:
        circleFlag = False
        parametricCircle(x, y, radius, canvasField, blackColor)
    else:
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
    global isLocked, localFirstPoint, mas, newFigureLen, zPixelFlag, zPixelPoint, circleFlag
    color = colorRecognizer()
    if zPixelFlag:
        zPixelFlag = False
        zPixelPoint = (int(x), int(y))
        z = [zPixelPoint[0], zPixelPoint[1]]
        stack.append(z)
        drawPixel(x, y, canvasField, img, color)
    elif circleFlag:
        circleFlag = False
        parametricCircle(x, y, radius, canvasField, blackColor)
    else:
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


def zPixelBtnClicked():
    global zPixelFlag
    zPixelFlag = True


def circleBtnClicked():
    global circleFlag
    circleFlag = True


def run():
    global stack
    d = dynamic.get()
    edge = blackColor
    fill = colorRecognizer()

    # пока стек не пуст

    while stack:
        print(len(stack))
        p = stack.pop()
        x = p[0]
        y = p[1]

        drawPixel(x, y, canvasField, img, fill)
        xl = paintToLeftEdge(x, y, edge, fill)  # заполняем интервал слева от затравки и сохраняем левую границу
        xr = paintToRightEdge(x, y, edge, fill)  # заполняем интервал справа от затравки и сохраняем правую границу

        findZPixel(xl, xr, y + 1, edge, fill, stack)  # ищем затравку на строке выше
        findZPixel(xl, xr, y - 1, edge, fill, stack)  # ищем затравку на строку ниже

        if d:
            root.update()
            canvasField.update()
            time.sleep(0.02)


def findZPixel(x, xr, y, edgeColor, fillColor, stack):
    while x <= xr:
        Fl = 0
        while getPixelColor(img, x, y) != edgeColor and getPixelColor(img, x, y) != fillColor and x <= xr:
            if Fl == 0:
                Fl = 1
            x += 1

        if Fl == 1:
            if x == xr and getPixelColor(img, x, y) != fillColor and getPixelColor(img, x, y) != edgeColor:
                stack.append((x, y))
            else:
                stack.append((x - 1, y))

        xt = x
        while (getPixelColor(img, x, y) == edgeColor or getPixelColor(img, x, y) == fillColor) and x < xr:
            x += 1

        if x == xt:
            x += 1


def paintToRightEdge(x, y, edgeColor, fillColor):
    while getPixelColor(img, x, y) != edgeColor:
        drawPixel(x, y, canvasField, img, fillColor)
        x += 1
    return x - 1


def paintToLeftEdge(x, y, edgeColor, fillColor):
    while getPixelColor(img, x, y) != edgeColor:
        drawPixel(x, y, canvasField, img, fillColor)
        x -= 1
    return x + 1

def rect(size):
    x = 2
    y = 2
    z = [x, y]
    stack.append(z)
    fakeMouseClick(1, 1);
    fakeMouseClick(1 + size, 1);
    fakeMouseClick(1 + size, 1 + size);
    fakeMouseClick(1, 1 + size);
    lock()
    start_time = datetime.now()
    run()
    print(datetime.now() - start_time)
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
colorDrawing.set("Красный")
colorMenu = tk.OptionMenu(root, colorDrawing, "Синий", "Красный", "Зеленый", "Фиолетовый", "Жёлтый")
colorMenu.pack(side="right")
dynamic = tk.IntVar()
# drawBtn = tk.Button(text="Где закраска, Лебовски?", command=run1).pack(side="right")
drawBtn = tk.Button(text="Моя закраска", command=run).pack(side="right")
clearBtn = tk.Button(text="Очистить", command=clearCanvasField).pack(side="right")
lockBtn = tk.Button(text="Замкнуть", command=lock).pack(side="right")
zatPixelButton = tk.Button(text="Ввести затравочный пиксел", command=zPixelBtnClicked).pack(side="right")
circleBtn = tk.Button(text="Окружность", command=circleBtnClicked).pack(side="right")
dynamicCheckbutton = tk.Checkbutton(text="С задержкой", variable=dynamic).pack(side="right")


# rect(10)
rect(100)
# rect(500)
# rect(1000)
# fakeMouseClick(100, 100)
# fakeMouseClick(100, 300)
# fakeMouseClick(300, 300)
# fakeMouseClick(300, 100)
# fakeMouseClick(250, 100)
# fakeMouseClick(250, 200)
# fakeMouseClick(200, 200)
# fakeMouseClick(200, 100)
# drawPixel(150, 250, canvasField, img, blackColor)
# fakeMouseClick(150, 100)
# fakeMouseClick(150, 200)
# fakeMouseClick(125, 200)
# fakeMouseClick(125, 100)
# lock()
# fakeMouseClick(140, 100)
# fakeMouseClick(240, 310)
# fakeMouseClick(320, 210)
# fakeMouseClick(412, 221)
# fakeMouseClick(211, 442)
# lock()
# parametricCircle(240, 360, 30, canvasField, blackColor)
# x = 341
# y = 245
# z = [x, y]
# stack.append(z)
#drawPixel(x, y, canvasField, img, redColor)


root.mainloop()
