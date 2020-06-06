import tkinter as tk
from tkinter import messagebox as mb
from funcs import *

cutter = []
figure = []
IMGSIZEX = 600
IMGSIZEY = IMGSIZEX
isCutterLocked = True
isFigureLocked = True
localFirstPoint = []
newFigureLen = 0
tmp = None
figureFlag = False
canvasField = None
typeDrawing = None


def setInterfaceGlobals(canvas, method):
    global canvasField, typeDrawing
    canvasField = canvas
    typeDrawing = method


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
    global cutter, isCutterLocked, figure, isFigureLocked, localFirstPoint, newFigureLen, tmp, figureFlag
    canvasField.delete("all")
    cutter = []
    figure = []
    isCutterLocked = True
    isFigureLocked = True
    localFirstPoint = []
    newFigureLen = 0
    tmp = None
    figureFlag = False



def mouseClick(event):
    global isCutterLocked, localFirstPoint, cutter, newFigureLen, lineFlag,\
        zPixelPoint, figureFlag, isFigureLocked, figure, tmp
    x, y = int(event.x), int(event.y)
    #print(x, y)
    if typeDrawing.get() == "Многоугольник":
        if isFigureLocked:
            localFirstPoint = Point(x, y)
            figure.append(localFirstPoint)
            isFigureLocked = False
            newFigureLen = 0
        else:
            if newFigureLen == 0:
                figure.append(Point(x, y))
                lineDrawer(Point(x, y), localFirstPoint, canvasField, blueColor)
                newFigureLen += 1
            else:
                l = len(figure) - 1
                figure.append((Point(x=x, y=y)))
                lineDrawer(Point(x=x, y=y), figure[l], canvasField, blueColor)
                newFigureLen += 1
    else:
        if isCutterLocked:
            localFirstPoint = Point(x, y)
            cutter.append(localFirstPoint)
            isCutterLocked = False
            newFigureLen = 0
        else:
            if newFigureLen == 0:
                cutter.append(Point(x, y))
                lineDrawer(Point(x, y), localFirstPoint, canvasField, blackColor)
                newFigureLen += 1
            else:
                l = len(cutter) - 1
                cutter.append((Point(x=x, y=y)))
                lineDrawer(Point(x=x, y=y), cutter[l], canvasField, blackColor)
                newFigureLen += 1


def fakeMouseClick(x, y):
    global isCutterLocked, localFirstPoint, cutter, newFigureLen, lineFlag, \
        zPixelPoint, figureFlag, isFigureLocked, figure, tmp
    # print(x, y)
    if typeDrawing.get() == "Многоугольник":
        if isFigureLocked:
            localFirstPoint = Point(x, y)
            figure.append(localFirstPoint)
            isFigureLocked = False
            newFigureLen = 0
        else:
            if newFigureLen == 0:
                figure.append(Point(x, y))
                lineDrawer(Point(x, y), localFirstPoint, canvasField, blueColor)
                newFigureLen += 1
            else:
                l = len(figure) - 1
                figure.append((Point(x=x, y=y)))
                lineDrawer(Point(x=x, y=y), figure[l], canvasField, blueColor)
                newFigureLen += 1
    else:
        if isCutterLocked:
            localFirstPoint = Point(x, y)
            cutter.append(localFirstPoint)
            isCutterLocked = False
            newFigureLen = 0
        else:
            if newFigureLen == 0:
                cutter.append(Point(x, y))
                lineDrawer(Point(x, y), localFirstPoint, canvasField, blackColor)
                newFigureLen += 1
            else:
                l = len(cutter) - 1
                cutter.append((Point(x=x, y=y)))
                lineDrawer(Point(x=x, y=y), cutter[l], canvasField, blackColor)
                newFigureLen += 1

def lock():
    global isCutterLocked, localFirstPoint, cutter, isFigureLocked
    if (typeDrawing.get() == "Многоугольник"):
        if isFigureLocked:
            return
        else:
            l = len(figure) - 1
            lineDrawer(localFirstPoint, figure[l], canvasField, blueColor)
            isFigureLocked = True
    else:
        if isCutterLocked:
            return
        else:
            l = len(cutter) - 1
            lineDrawer(localFirstPoint, cutter[l], canvasField, blackColor)
            isCutterLocked = True


def redrawEdges(canvas, color):
    global cutter
    for edge in cutter:
        lineDrawer(edge[0], edge[1], edge[2], edge[3], canvas, color)


def lineBtnClicked():
    global lineFlag
    lineFlag = True


def figureBtnCliced():
    global figureFlag
    figureFlag = True

def drawFigure(figure):
    for i in range(len(figure) - 1):
        lineDrawer(figure[i], figure[i + 1], canvasField, redColor)
    lineDrawer(figure[0], figure[len(figure) - 1], canvasField, redColor)