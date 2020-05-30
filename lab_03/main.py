#from constants import WINDOWSIZE, STRWINDOWSIZE
from constants import *
from point import *
import tkinter as tk
from math import sin, cos, pi
from tkinter import messagebox
from drawers import *
from datetime import datetime
import time



YSAFE = WINDOWSIZE//2
XSAFE = -WINDOWSIZE//2.6

root = tk.Tk()
root.geometry(STRWINDOWSIZE)

def supertester():
    start_time = datetime.now()
    high = 90
    start = Point(0, 0).getCanvasCoordinates()
    right = Point(high, 0).getCanvasCoordinates()
    left = Point(-high, 0).getCanvasCoordinates()
    up = Point(0, high).getCanvasCoordinates()
    down = Point(0, -high).getCanvasCoordinates()
    upleft = Point(-high, high).getCanvasCoordinates()
    upright = Point(high, high).getCanvasCoordinates()
    downleft = Point(-high, -high).getCanvasCoordinates()
    downright = Point(high, -high).getCanvasCoordinates()

    p1 = Point(high/2, high).getCanvasCoordinates()
    p2 = Point(high, high/2).getCanvasCoordinates()
    p3 = Point(high/2, -high).getCanvasCoordinates()
    p4 = Point(high, -high/2).getCanvasCoordinates()
    p5 = Point(-high/2, -high).getCanvasCoordinates()
    p6 = Point(-high, -high/2).getCanvasCoordinates()
    p7 = Point(-high/2, high).getCanvasCoordinates()
    p8 = Point(-high, high/2).getCanvasCoordinates()
    met = method.get()
    if met == 0:
        f = cdaDrawer
    elif met == 1:
        f = basicDrawer
    elif met == 2:
        f = bresenhamFloat
    elif met == 3:
        f = bresenhamInt
    elif met == 4:
        f = bresenhamSmooth
    elif met == 5:
        f = Vu
    color = drawingColor.get()
    f(start, left, canvasField, color)
    f(start, right, canvasField, color)
    f(start, up, canvasField, color)
    f(start, down, canvasField, color)
    f(start, upleft, canvasField, color)
    f(start, upright, canvasField, color)
    f(start, downleft, canvasField, color)
    f(start, downright, canvasField, color)

    f(start, p1, canvasField, color)
    f(start, p2, canvasField, color)
    f(start, p3, canvasField, color)
    f(start, p4, canvasField, color)
    f(start, p5, canvasField, color)
    f(start, p6, canvasField, color)
    f(start, p7, canvasField, color)
    f(start, p8, canvasField, color)
    print(datetime.now() - start_time)

def drawer():
    xs = float(txtFieldFromX.get())
    ys = float(txtFieldFromY.get())
    xf = float(txtFieldToX.get())
    yf = float(txtFieldToY.get())
    met = method.get()
    if met == 0:
        f = cdaDrawer
    elif met == 1:
        f = basicDrawer
    elif met == 2:
        f = bresenhamFloat
    elif met == 3:
        f = bresenhamInt
    elif met == 4:
        f = bresenhamSmooth
    elif met == 5:
        f = Vu
    start = Point(xs, ys)
    finish = Point(xf, yf)
    color = drawingColor.get()
    f(start, finish, canvasField, color)


def drawPixel(pixel, canvas, color):
    pixel.drawAsPixel(canvas, color)





def clearCanvasField():
    canvasField.delete("all")


############################# Zoom ###################################

x, y = normalToTkInter(XSAFE + 400, YSAFE - 500)
tk.Button(text="Нарисовать", command=supertester).place(x=x, y=y, width=150, height=30)

x, y = normalToTkInter(XSAFE + 400, YSAFE - 550)
tk.Button(text="Очистить поле", command=clearCanvasField).place(x=x, y=y, width=160, height=30)

x, y = normalToTkInter(XSAFE + 0, YSAFE - 490)
tk.Label(text="Из точки").place(x=x, y=y)

x, y = normalToTkInter(XSAFE + 0, YSAFE - 520)
tk.Label(text="x").place(x=x, y=y)

txtFieldFromX = tk.Entry()
x, y = normalToTkInter(XSAFE + 20, YSAFE - 518)
txtFieldFromX.place(x=x, y=y, width=45)


x, y = normalToTkInter(XSAFE + 0, YSAFE - 550)
tk.Label(text="y").place(x=x, y=y)

txtFieldFromY = tk.Entry()
x, y = normalToTkInter(XSAFE + 20, YSAFE - 548)
txtFieldFromY.place(x=x, y=y, width=45)


x, y = normalToTkInter(XSAFE + 90, YSAFE - 490)
tk.Label(text="В точку").place(x=x, y=y)

x, y = normalToTkInter(XSAFE + 90, YSAFE - 520)
tk.Label(text="x").place(x=x, y=y)

txtFieldToX = tk.Entry()
x, y = normalToTkInter(XSAFE + 110, YSAFE - 518)
txtFieldToX.place(x=x, y=y, width=45)


x, y = normalToTkInter(XSAFE + 90, YSAFE - 550)
tk.Label(text="y").place(x=x, y=y)

txtFieldToY = tk.Entry()
x, y = normalToTkInter(XSAFE + 110, YSAFE - 548)
txtFieldToY.place(x=x, y=y, width=45)




canvasField = tk.Canvas(root, width=CANVASSIZE, height=CANVASSIZE, bg='white')
x, y = normalToTkInter(XSAFE + 130, YSAFE - 50)
canvasField.place(x=x, y=y)


x, y = normalToTkInter(XSAFE, YSAFE - 50)
drawingColor = tk.StringVar()
tk.Radiobutton(text='Белый', variable=drawingColor, value='white').place(x=x, y=y - 30)
tk.Radiobutton(text='Красный', variable=drawingColor, value='red').place(x=x, y=y)
tk.Radiobutton(text='Черный', variable=drawingColor, value='black').place(x=x, y=y + 30)
tk.Radiobutton(text='Синий', variable=drawingColor, value='blue').place(x=x, y=y + 60)

y += 100
method = tk.IntVar()
tk.Radiobutton(text='ЦДА', variable=method, value=0).place(x=x, y=y)
tk.Radiobutton(text='Библиотечный', variable=method, value=1).place(x=x, y=y + 30)
tk.Radiobutton(text='Брезенхем вещественный', variable=method, value=2).place(x=x, y=y + 60)
tk.Radiobutton(text='Брезенхем целочисленный', variable=method, value=3).place(x=x, y=y + 90)
tk.Radiobutton(text='Брезенхем сглаженный', variable=method, value=4).place(x=x, y=y + 120)
tk.Radiobutton(text='Ву', variable=method, value=5).place(x=x, y=y + 150)



root.mainloop()
