# from constants import WINDOWSIZE, STRWINDOWSIZE
from constants import *
from point import *
import tkinter as tk
from circleDrawer import *
from ellipseDrawer import *
from math import sin, cos, pi
from tkinter import messagebox
from datetime import datetime
import time

YSAFE = WINDOWSIZE // 2
XSAFE = -WINDOWSIZE // 2.6

root = tk.Tk()
root.geometry(STRWINDOWSIZE)

def colorRecognizer(color):
    if color == "Синий":
        return "blue"
    elif color == "Красный":
        return "red"
    elif color == "Зеленый":
        return "green"
    elif color == "Белый":
        return "white"
    else:
        return "black"





def drawCircle():
    met = drawingMethod.get()
    color = colorRecognizer(colorDrawing.get())
    xc = float(centerX.get())
    yc = float(centerY.get())
    r = float(circleRadius.get())
    f = libDrawCircle
    if met == "Библиотечный":
        f = libDrawCircle
    elif met == "Каноническое уравнение":
        f = canonicCircle
    elif met == "Параметрическое уравнение":
        f = parametricCircle
    elif met == "Брезенхем":
        f = bresCircle
    elif met == "Метод средней точки":
        f = middlePointCircle
    start_time = datetime.now()
    f(xc, yc, r, canvasField, color)
    print("Radius,", r, "-", datetime.now() - start_time)

def drawEllipse():
    met = drawingMethod.get()
    xc = float(centerX.get())
    yc = float(centerY.get())
    a = float(ellipseRadiusA.get())
    b = float(ellipseRadiusB.get())
    color = colorRecognizer(colorDrawing.get())
    f = libDrawEllipse
    if met == "Библиотечный":
        f = libDrawEllipse
    elif met == "Каноническое уравнение":
        f = canonicEllipse
    elif met == "Параметрическое уравнение":
        f = parametricEllipse
    elif met == "Брезенхем":
        f = bresEllispe
    elif met == "Метод средней точки":
        f = middlePointEllispe
    start_time = datetime.now()
    f(xc, yc, a, b, canvasField, color)
    print("Current ellipse:", datetime.now() - start_time)

def rangeDrawCircle():
    met = drawingMethod.get()
    xc = float(centerX.get())
    yc = float(centerY.get())
    rFrom = float(circleRadiusFrom.get())
    rStep = float(circleRadiusStep.get())
    rNum = int(circleRadiusNumber.get())
    color = colorRecognizer(colorDrawing.get())
    print(color)
    if met == "Библиотечный":
        f = libDrawCircle
    elif met == "Каноническое уравнение":
        f = canonicCircle
    elif met == "Параметрическое уравнение":
        f = parametricCircle
    elif met == "Брезенхем":
        f = bresCircle
    elif met == "Метод средней точки":
        f = middlePointCircle
    currentR = rFrom
    for i in range(rNum):
        f(xc, yc, currentR, canvasField, color)
        currentR += rStep


def rangeDrawEllipse():
    met = drawingMethod.get()
    xc = float(centerX.get())
    yc = float(centerY.get())
    aFrom = float(ellipseRadiusAFrom.get())
    bFrom = float(ellipseRadiusBFrom.get())
    bStep = float(ellipseRadiusBStep.get())
    rNum = int(ellipseRadiusNum.get())
    color = colorRecognizer(colorDrawing.get())
    if met == "Библиотечный":
        f = libDrawEllipse
    elif met == "Каноническое уравнение":
        f = canonicEllipse
    elif met == "Параметрическое уравнение":
        f = parametricEllipse
    elif met == "Брезенхем":
        f = bresEllispe
    elif met == "Метод средней точки":
        f = middlePointEllispe
    curA = aFrom
    curB = bFrom
    for i in range(rNum):
        f(xc, yc, curA, curB, canvasField, color)
        curA *= ((curB + bStep) / curB)
        curB += bStep



def clearCanvasField():
    canvasField.delete("all")


def cirel():
    type = drawingType.get()
    if type == "circle":
        ellipseRadiusA.place_forget()
        ellipseRadiusB.place_forget()
        ellipseRadiusAText.place_forget()
        ellipseRadiusBText.place_forget()
        ellipseRadiusAFrom.place_forget()
        ellipseRadiusBFrom.place_forget()
        ellipseRadiusAStep.place_forget()
        ellipseRadiusBStep.place_forget()
        ellipseRadiusNum.place_forget()
        ellipseRangeButton.place_forget()

        ellipseRadiusAFromText.place_forget()
        ellipseRadiusBFromText.place_forget()
        ellipseRadiusAStepText.place_forget()
        ellipseRadiusBStepText.place_forget()
        ellipseRadiusNumText.place_forget()

        x, y = normalToTkInter(XSAFE, YSAFE - 150)
        circleRadiusText.place(x=x, y=y)
        circleRadius.place(x=x + 145, y=y, width=45)

        x, y = normalToTkInter(XSAFE, YSAFE - 180)
        drawCircleButton.place(x=x, y=y)
        drawEllipseButton.place_forget()

        x, y = normalToTkInter(XSAFE, YSAFE - 330)
        circleRadiusFromText.place(x=x, y=y)
        circleRadiusFrom.place(x=x+180, y=y-2, width=45)

        x, y = normalToTkInter(XSAFE, YSAFE - 360)
        circleRadiusToText.place(x=x, y=y)
        circleRadiusTo.place(x=x + 180, y=y - 2, width=45)

        x, y = normalToTkInter(XSAFE, YSAFE - 390)
        circleRadiusNumberText.place(x=x, y=y)
        circleRadiusNumber.place(x=x+180, y=y - 2, width=45)

        x, y = normalToTkInter(XSAFE, YSAFE - 420)
        circleRadiusStepText.place(x=x, y=y)
        circleRadiusStep.place(x=x +180, y=y - 2, width=45)

        x, y = normalToTkInter(XSAFE, YSAFE - 450)
        circleRangeButton.place(x=x, y=y)


    else:
        circleRadiusFrom.place_forget()
        circleRadiusTo.place_forget()
        circleRadiusNumber.place_forget()
        circleRadiusStep.place_forget()
        circleRadius.place_forget()
        circleRadiusText.place_forget()
        circleRadiusFromText.place_forget()
        circleRadiusToText.place_forget()
        circleRadiusNumberText.place_forget()
        circleRadiusStepText.place_forget()
        circleRangeButton.place_forget()

        x, y = normalToTkInter(XSAFE, YSAFE - 150)
        ellipseRadiusAText.place(x=x, y=y)
        ellipseRadiusA.place(x=x + 145, y=y, width=45)

        ellipseRadiusBText.place(x=x, y=y + 30)
        ellipseRadiusB.place(x=x + 145, y=y + 30, width=45)

        x, y = normalToTkInter(XSAFE, YSAFE - 210)
        drawCircleButton.place_forget()
        drawEllipseButton.place(x=x, y=y)

        x, y = normalToTkInter(XSAFE, YSAFE - 330)
        ellipseRadiusAFromText.place(x=x, y=y)
        ellipseRadiusAFrom.place(x=x + 180, y=y - 2, width=45)

        x, y = normalToTkInter(XSAFE, YSAFE - 360)
        ellipseRadiusBFromText.place(x=x, y=y)
        ellipseRadiusBFrom.place(x=x + 180, y=y - 2, width=45)

        x, y = normalToTkInter(XSAFE, YSAFE - 390)
        ellipseRadiusAStepText.place(x=x, y=y)
        ellipseRadiusAStep.place(x=x + 180, y=y - 2, width=45)

        x, y = normalToTkInter(XSAFE, YSAFE - 420)
        ellipseRadiusBStepText.place(x=x, y=y)
        ellipseRadiusBStep.place(x=x + 180, y=y - 2, width=45)

        x, y = normalToTkInter(XSAFE, YSAFE - 450)
        ellipseRadiusNumText.place(x=x, y=y)
        ellipseRadiusNum.place(x=x + 180, y=y - 2, width=45)

        x, y = normalToTkInter(XSAFE, YSAFE - 480)
        ellipseRangeButton.place(x=x, y=y)




############################# Zoom ###################################


canvasField = tk.Canvas(root, width=CANVASSIZE, height=CANVASSIZE, bg='white')
x, y = normalToTkInter(XSAFE + 220, YSAFE - 50)
canvasField.place(x=x, y=y)

x, y = normalToTkInter(XSAFE, YSAFE - 50)
drawingType = tk.StringVar()
tk.Radiobutton(text="Окружность", variable=drawingType, value="circle", indicatoron=0, command=cirel).place(x=x,
                                                                                                            y=y - 30)
tk.Radiobutton(text="Эллипс", variable=drawingType, value="ellipse", indicatoron=0, command=cirel).place(x=x + 100,
                                                                                                         y=y - 30)

x, y = normalToTkInter(XSAFE, YSAFE - 90)
tk.Label(text="Координаты центра:").place(x=x, y=y - 30)
tk.Label(text="X:").place(x=x, y=y - 10)
centerX = tk.Entry()
centerX.place(x=x + 25, y=y - 12, width=45, height=27)

tk.Label(text="Y:").place(x=x, y=y + 15)
centerY = tk.Entry()
centerY.place(x=x + 25, y=y + 13, width=45, height=27)

#
circleRadius = tk.Entry()
circleRadiusFrom = tk.Entry()
circleRadiusTo = tk.Entry()
circleRadiusNumber = tk.Entry()
circleRadiusStep = tk.Entry()
circleRadiusText = tk.Label(text="Радиус окружности:")
circleRadiusFromText = tk.Label(text="Начальный радиус:")
circleRadiusToText = tk.Label(text="Конечный радиус:")
circleRadiusNumberText = tk.Label(text="Количество окружностей:")
circleRadiusStepText = tk.Label(text="Шаг радиуса:")
circleRangeButton = tk.Button(text="Нарисовать \nмножество окружностей", command=rangeDrawCircle)
drawCircleButton = tk.Button(text="Нарисовать", command=drawCircle)



ellipseRadiusA = tk.Entry()
ellipseRadiusB = tk.Entry()
ellipseRadiusAFrom = tk.Entry()
ellipseRadiusBFrom = tk.Entry()
ellipseRadiusAStep = tk.Entry()
ellipseRadiusBStep = tk.Entry()
ellipseRadiusNum = tk.Entry()

ellipseRadiusAFromText = tk.Label(text="Начальное а:")
ellipseRadiusBFromText = tk.Label(text="Начальное b:")
ellipseRadiusAStepText = tk.Label(text="Шаг a:")
ellipseRadiusBStepText = tk.Label(text="Шаг b:")
ellipseRadiusNumText = tk.Label(text="Количество эллписов:")

ellipseRadiusAText = tk.Label(text="A:")
ellipseRadiusBText = tk.Label(text="B:")

drawEllipseButton = tk.Button(text="Нарисовать", command=drawEllipse)
ellipseRangeButton = tk.Button(text="Нарисовать \nмножество эллипсов", command=rangeDrawEllipse)
#

drawingMethod = tk.StringVar()
colorDrawing = tk.StringVar()
drawingMethod.set("Библиотечный")
colorDrawing.set("Черный")
methodMenu = tk.OptionMenu(root, drawingMethod, "Библиотечный", "Каноническое уравнение", "Параметрическое уравнение",
                           "Брезенхем", "Метод средней точки")
colorMenu = tk.OptionMenu(root, colorDrawing, "Черный", "Синий", "Красный", "Зеленый", "Белый")
x, y = normalToTkInter(XSAFE, YSAFE - 240)
methodMenu.place(x=x, y=y)
colorMenu.place(x=x, y=y+30)
tk.Button(text="Очитстить", command=clearCanvasField).place(x=x,y=y+60)




root.mainloop()
