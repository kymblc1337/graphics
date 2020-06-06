from math import sin, cos, exp, sqrt
from horizon import float_horizon
import tkinter as tk
from constants import *

rx = 20
ry = -10
rz = 0
XFrom = -5
XTo = 5
ZFrom = -5
ZTo = 5
XStep = 0.2
ZStep = 0.2


def f(x, z):
    return abs(cos(x) * cos(z))

def dxplus():
    global rx
    rx += 5
    mainfunc()

def dxminus():
    global rx
    rx -= 5
    mainfunc()

def dyplus():
    global ry
    ry += 5
    mainfunc()

def dyminus():
    global ry
    ry -= 5
    mainfunc()



def mainfunc():
    canvasField.delete("all")
    float_horizon(WIDTH + 1, HEIGHT + 1, XFrom, XTo, XStep, ZFrom, ZTo,
                  ZStep, rx, -ry, rz, f, canvasField)





#########################################################################
##############################MAIN#######################################
#########################################################################

root = tk.Tk()
canvasField = tk.Canvas(root, width=WIDTH, height=HEIGHT)
canvasField.pack()



typeDrawing = tk.StringVar()
typeDrawing.set("Отсекатель")
typeMenu = tk.OptionMenu(root, typeDrawing, "Многоугольник", "Отсекатель")
typeMenu.pack(side="right")
tk.Button(command=mainfunc, text="GO").pack(side="right")
tk.Button(command=dxplus, text="|\nV").pack(side="left")
tk.Button(command=dxminus, text="^\n|").pack(side="left")
tk.Button(command=dyplus, text="->").pack(side="left")
tk.Button(command=dyminus, text="<-").pack(side="left")


root.mainloop()
