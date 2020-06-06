import tkinter as tk
from tkinter import messagebox as mb
from funcs import *
from interface import *


def mainfunc():
    normal = convex(cutter)
    if not normal:
        mb.showerror("Ошибка", "Отсекатель не выпуклый")
    else:
        tmp = sutherlandHodgman(cutter, figure, normal)
        if tmp:
            drawFigure(tmp)




#########################################################################
##############################MAIN#######################################
#########################################################################

root = tk.Tk()
canvasField = tk.Canvas(root, width=600, height=600)
canvasField.pack()
#canvasField.create_image(img.size[0] // 2, img.size[1] // 2)

canvasField.bind("<Button-1>", mouseClick)
# canvasField.bind("<Button-2>", testfunc)

typeDrawing = tk.StringVar()
typeDrawing.set("Отсекатель")
typeMenu = tk.OptionMenu(root, typeDrawing, "Многоугольник", "Отсекатель")
typeMenu.pack(side="right")
drawBtn = tk.Button(text="Выполнить отсечение", command=mainfunc).pack(side="right")
clearBtn = tk.Button(text="Очистить", command=clearCanvasField).pack(side="right")
lockBtn = tk.Button(text="Замкнуть", command=lock).pack(side="right")
setInterfaceGlobals(canvasField, typeDrawing)


root.mainloop()
