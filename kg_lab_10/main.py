from math import sin, cos, exp, sqrt
from horizon import float_horizon
import tkinter as tk
from constants import *

rx = 20
ry = -10
rz = 0
XFrom = -6
XTo = 6
ZFrom = -6
ZTo = 6
XStep = 0.1
ZStep = 0.1



def abssincos(x, z):
    return abs(cos(x) * sin(z))

def prettybend(x, z):
    return x**2 // 30 + z**2 // 30

def xpz(x, z):
    return sin(x) * sin(z)

def dxplus():
    global rx
    rx %= 180
    mainfunc()

def dxminus():
    global rx
    rx -= 5
    rx %= 180
    mainfunc()

def dyplus():
    global ry
    ry += 5
    ry %= 180
    print(ry)
    mainfunc()

def dyminus():
    global ry
    ry -= 5
    ry %= 180
    print(ry)
    mainfunc()


f = abssincos

def selectModel():
    global f
    s = typeDrawing.get()
    if s == "x^2 + z ^ 2":
        f = prettybend
    elif s == "|cos(x) * sin(z)|":
        f = abssincos
    elif s == "x + z":
        f = xpz

def mainfunc():
    selectModel()
    canvasField.delete("all")
    float_horizon(WIDTH + 1, HEIGHT + 1, XFrom, XTo, XStep, ZFrom, ZTo,
                  ZStep, rx, -ry, rz, f, canvasField)

def clr():
    canvasField.delete("all")





#########################################################################
##############################MAIN#######################################
#########################################################################

root = tk.Tk()
canvasField = tk.Canvas(root, width=WIDTH, height=HEIGHT)
canvasField.pack()



typeDrawing = tk.StringVar()
typeDrawing.set("x + z")
typeMenu = tk.OptionMenu(root, typeDrawing, "x^2 + z ^ 2", "|cos(x) * sin(z)|", "x + z")
typeMenu.pack(side="right")
tk.Button(command=mainfunc, text="Нарисовать").pack(side="right")
tk.Button(command=clr, text="Очистить").pack(side="right")
tk.Button(command=dxplus, text="|\nV").pack(side="left")
tk.Button(command=dxminus, text="^\n|").pack(side="left")
tk.Button(command=dyplus, text="->").pack(side="left")
tk.Button(command=dyminus, text="<-").pack(side="left")


root.mainloop()
