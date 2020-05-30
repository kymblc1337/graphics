# from constants import WINDOWSIZE, STRWINDOWSIZE
from constants import *
from point import *
import tkinter as tk
import math
from tkinter import messagebox
from datetime import datetime
import time

YSAFE = WINDOWSIZE // 2
XSAFE = -WINDOWSIZE // 2.6

tmpPoint = ()
lines = []
locker = False
rect = []
eps = 0.01

root = tk.Tk()
modeDrawing = tk.StringVar()

def lineDrawer(xs, ys, xf, yf, canvas, color="black"):
    canvas.create_line(xs, ys, xf, yf, fill=color)
    # if yf < ys:
    #     xs, ys, xf, yf = xf, yf, xs, ys
    #
    # dx = abs(xf - xs)
    # dy = abs(yf - ys)
    #
    # if dx > dy:
    #     steep = dx
    # else:
    #     steep = dy
    # stepx = (xf - xs) / steep
    # stepy = (yf - ys) / steep
    #
    # curx = xs
    # cury = ys
    # for i in range(int(steep + 1)):
    #     drawPixel(curx, cury, canvas, color)
    #     curx += stepx
    #     cury += stepy

def rectDrawer(xs, ys, xf, yf, canvas):
    lineDrawer(xs, ys, xf, ys, canvas)
    lineDrawer(xf, ys, xf, yf, canvas)
    lineDrawer(xs, ys, xs, yf, canvas)
    lineDrawer(xs, yf, xf, yf, canvas)

def mouseClick(event):
    global lines, locker, tmpPoint, modeDrawing, rect
    x, y = int(event.x), int(event.y)
    if modeDrawing.get() == "Отрезок":
        if locker:
            lines.append((tmpPoint[0], tmpPoint[1], x, y))
            lineDrawer(tmpPoint[0], tmpPoint[1], x, y, canvasField)
            locker = False
        else:
            tmpPoint = (x, y)
            locker = True
    else:
        if locker:
            rect = [tmpPoint[0], tmpPoint[1], x, y]
            rectDrawer(tmpPoint[0], tmpPoint[1], x, y, canvasField)
            locker = False
        else:
            tmpPoint = (x, y)
            locker = True

def clearCanvasField():
    canvasField.delete("all")
    global lines, locker, tmpPoint, rect
    tmpPoint = ()
    lines = []
    locker = False
    rect = []

def code(x, y, rect):
    res = [0, 0, 0, 0]
    if x < rect[0]:
        res[0] = 1
    if x > rect[2]:
        res[1] = 1
    if y < rect[1]:
        res[2] = 1
    if y > rect[3]:
        res[3] = 1
    return res

def logicMultiply(code1, code2):
    p = 0
    for i in range(4):
        p += code1[i] & code2[i]
    return p


def tstrun():
    for line in lines:
        lineSolver(line)


def lineSolver(line):
    global eps
    i = 1
    P1 = (line[0], line[1])
    P2 = (line[2], line[3])

    while True:
        T1 = code(P1[0], P1[1], rect)
        T2 = code(P2[0], P2[1], rect)

        S1 = sum(T1)
        S2 = sum(T2)

        if S1 == 0 and S2 == 0:
            print("jopa")
            lineDrawer(P1[0], P1[1], P2[0], P2[1], canvasField, "red")
            return

        P = logicMultiply(T1, T2)

        if P != 0:
            lineDrawer(P1[0], P1[1], P2[0], P2[1], canvasField, "green")
            return

        if i > 2:
            lineDrawer(P1[0], P1[1], P2[0], P2[1], canvasField, "red")
            return

        R = P1

        if S2 == 0:
            P1, P2 = P2, R
            i += 1
            continue

        while True:
            if math.sqrt((P1[0] - P2[0]) ** 2 + (P1[1] - P2[1]) ** 2) < eps:
                P1, P2 = P2, R
                i += 1
                break
            else:
                Psr = (((P1[0] + P2[0]) / 2), ((P1[1] + P2[1]) / 2))
                Pm = P1
                P1 = Psr

                T1 = code(P1[0], P1[1], rect)
                T2 = code(P2[0], P2[1], rect)

                P = logicMultiply(T1, T2)

                if P != 0:
                    P1 = Pm
                    P2 = Psr



############################# MAIN ###################################


canvasField = tk.Canvas(root, width=CANVASSIZE, height=CANVASSIZE, bg='white', highlightthickness=1,
                        highlightbackground="black")
canvasField.pack()
canvasField.bind("<Button-1>", mouseClick)


modeDrawing.set("Отрезок")
x, y = normalToTkInter(XSAFE, YSAFE)
drawMenu = tk.OptionMenu(root, modeDrawing, "Отрезок", "Отсекатель")
drawMenu.pack(side="right")
tk.Button(text="Очистить", command=clearCanvasField).pack(side="right")
tk.Button(text="Отсечь", command=tstrun).pack(side="right")
#

# tk.Button(text="Очитстить", command=clearCanvasField).place(x=x,y=y+60)


root.mainloop()
