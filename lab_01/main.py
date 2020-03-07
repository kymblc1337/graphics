import tkinter as tk
from geomerty import *
from tkinter import messagebox

list = []


def getScaleCoefficient():
    beg = 20
    end = 280

    xmax = list[0][1]
    xmin = list[0][1]
    ymax = list[0][1]
    ymin = list[0][1]

    for point in list:
        if point[0] < xmin:
            xmin = point[0]
        if point[0] > xmax:
            xmax = point[0]
        if point[1] < ymin:
            ymin = point[1]
        if point[1] > ymax:
            ymax = point[1]



    scaleX = (end - beg) / (xmax - xmin)
    scaleY = (end - beg) / (ymax - ymin)
    SCALEK = min(scaleX, scaleY)

    return SCALEK, xmin, ymax

def lboxFormatter(x, y):
    item = "{:<15f};{:>15f}".format(x, y)
    return item

def normalToTkInter(x, y):
    return (x + 330, -y + 345)

def lstBoxAddItem(lstbox, x, y):
    a = (x, y)
    item = lboxFormatter(x, y)
    lstbox.insert('end', item)



def tkInterToNormal(x, y):
    return (x - 250, y - 250)


def put_all_points():
    if len(list) < 3:
        tk.messagebox.showinfo("Ошибка", "Проверьте количетсво точек")
    else:
        xmax = list[0][1]
        xmin = list[0][1]
        ymax = list[0][1]
        ymin = list[0][1]

        for point in list:
            if point[0] < xmin:
                xmin = point[0]
            if point[0] > xmax:
                xmax = point[0]
            if point[1] < ymin:
                ymin = point[1]
            if point[1] > ymax:
                ymax = point[1]

        # print("xmax: ", xmax)
        # print("xmin: ", xmin)
        # print("ymax: ", ymax)
        # print("ymin: ", ymin)

        XCOEF = 300 / (xmax - xmin)
        YCOEF = 300 / (ymax - ymin)

        for i in list:
            #print("point ", i[0], i[1])
            #print("will become", i[0] * XCOEF, i[1] * YCOEF)
            # x, y = canvas_coords(XK, YK, i[0] + 150, -i[1] + 150)
            x = i[0] * XCOEF + 145
            y = -i[1] * YCOEF + 145
            if (x < 0):
                x += 10
            if (y < 0):
                y += 10
            c.create_oval(x - 1, y - 1, x + 1, y + 1)

def getTestCoordinates(x1, y1):

    SCALEK, xmin, ymax = getScaleCoefficient()

    x = 20 + (x1 - xmin) * SCALEK
    y = 20 + (ymax - y1) * SCALEK

    return x, y


def addButtonClicked():
    x = txtFieldOfX.get()
    y = txtFieldOfY.get()
    try:
        x = float(x)
        y = float(y)
        a = (x, y)
        if a not in list:
            list.append((x, y))
            lstBoxAddItem(box, x, y)
    except Exception:
        tk.messagebox.showinfo("Ошибка", "Проверьте корректность ввода данных")
    finally:
        txtFieldOfY.delete(0, 'end')
        txtFieldOfX.delete(0, 'end')

def getNumPointsThatAreInTriangle(xa, ya, xb, yb, xc, yc):
    num = 0
    for i in list:
        if xyIsInsideABC(i[0], i[1], xa, ya, xb, yb, xc, yc):
            num += 1
    return num

def getDiffForBigTriangle(xa, ya, xb, yb, xc, yc):
    # c.create_line(getTestCoordinates(xa, ya), getTestCoordinates(xb, yb))
    # c.create_line(getTestCoordinates(xb, yb), getTestCoordinates(xc, yc))
    # c.create_line(getTestCoordinates(xa, ya), getTestCoordinates(xc, yc))
    ablen = getABlen(xa, ya, xb, yb)
    bclen = getABlen(xb, yb, xc, yc)
    aclen = getABlen(xa, ya, xc, yc)
    abp = getPointCThatDividesABLike(xa, ya, xb, yb, aclen, bclen)
    bcp = getPointCThatDividesABLike(xb, yb, xc, yc, ablen, aclen)
    acp = getPointCThatDividesABLike(xa, ya, xc, yc, ablen, bclen)
    # print(abp)
    # c.create_line(getTestCoordinates(xc, yc), getTestCoordinates(abp[0], abp[1]))
    # c.create_line(getTestCoordinates(xa, ya), getTestCoordinates(bcp[0], bcp[1]))
    # c.create_line(getTestCoordinates(xb, yb), getTestCoordinates(acp[0], acp[1]))
    ato = getCoefficientsOfLineOfTwoPoints(xa, ya, bcp[0], bcp[1])
    bto = getCoefficientsOfLineOfTwoPoints(xb, yb, acp[0], acp[1])
    xr, yr = getPointOfIntersections(ato[0], ato[1], ato[2], bto[0], bto[1], bto[2])
    mas = []
    mas.append(getNumPointsThatAreInTriangle(xa, ya, xr, yr, abp[0], abp[1]))
    mas.append(getNumPointsThatAreInTriangle(xa, ya, xr, yr, acp[0], acp[1]))

    mas.append(getNumPointsThatAreInTriangle(xb, yb, xr, yr, abp[0], abp[1]))
    mas.append(getNumPointsThatAreInTriangle(xb, yb, xr, yr, bcp[0], bcp[1]))

    mas.append(getNumPointsThatAreInTriangle(xc, yc, xr, yr, bcp[0], bcp[1]))
    mas.append(getNumPointsThatAreInTriangle(xc, yc, xr, yr, acp[0], acp[1]))
    res = max(mas) - min(mas)
    # if max(mas):
    #
    #     print("for triangle", xa, ya, "  ", xb, yb, "  ", xc, yc)
    #     print(mas, "diff is", res)
    #     print('\n\n')

    return res

def masOut():
    print("MASOUT")
    for i in list:
        print(i)

def drawResultTriangle(savepoints):
    xa, ya, xb, yb, xc, yc = savepoints
    if (xb <= xc) and (xb <= xa):
        xa, ya, xb, yb = xb, yb, xa, ya
    if (xc <= xb) and (xc <= xa):
        xa, ya, xc, yc = xc, yc, xa, ya
    if (yc >= yb) and (yc >= ya):
        xb, yb, xc, yc = xc, yc, xb, yb
    if (ya >= yb) and (ya >= yc):
        xb, yb, xa, ya = xa, ya, xb, yb


    # drawing triangle corpus
    c.create_line(getTestCoordinates(xa, ya), getTestCoordinates(xb, yb))
    c.create_line(getTestCoordinates(xb, yb), getTestCoordinates(xc, yc))
    c.create_line(getTestCoordinates(xa, ya), getTestCoordinates(xc, yc))

    atext = str(xa) + ";" + str(ya)
    btext = str(xb) + ";" + str(yb)
    ctext = str(xc) + ";" + str(yc)

    x, y = getTestCoordinates(xa, ya)
    c.create_text(x, y + 10, text=atext, font="Verdana 9")
    x, y = getTestCoordinates(xb, yb)
    c.create_text(x, y - 7, text=btext, font="Verdana 9")
    x, y = getTestCoordinates(xc, yc)
    c.create_text(x + 5, y + 10 , text=ctext, font="Verdana 9")

    # calculationg bisectors
    ablen = getABlen(xa, ya, xb, yb)
    bclen = getABlen(xb, yb, xc, yc)
    aclen = getABlen(xa, ya, xc, yc)
    abp = getPointCThatDividesABLike(xa, ya, xb, yb, aclen, bclen) # ac bc
    bcp = getPointCThatDividesABLike(xb, yb, xc, yc, ablen, aclen) # ab ac
    acp = getPointCThatDividesABLike(xa, ya, xc, yc, ablen, bclen) # ab bc

    # drawing bisectors
    c.create_line(getTestCoordinates(xc, yc), getTestCoordinates(abp[0], abp[1]))
    c.create_line(getTestCoordinates(xa, ya), getTestCoordinates(bcp[0], bcp[1]))
    c.create_line(getTestCoordinates(xb, yb), getTestCoordinates(acp[0], acp[1]))
    # calculating points
    for point in list:
        if xyIsInsideABC(point[0], point[1], xa, ya, xb, yb, xc, yc):
            xr, yr = getTestCoordinates(point[0], point[1])
            c.create_oval(xr - 1, yr - 1, xr + 1, yr + 1)




def test():
    maxi = -1
    savepoints = []
    extrasave = []
    for a in list:
        for b in list:
            for c in list:
                if pointsMidhtBeTriangle(a[0], a[1], b[0], b[1], c[0], c[1]):
                    extrasave = a[0], a[1], b[0], b[1], c[0], c[1]
                    cur = getDiffForBigTriangle(a[0], a[1], b[0], b[1], c[0], c[1])
                    if cur > maxi:
                        maxi = cur
                        savepoints = [a[0], a[1], b[0], b[1], c[0], c[1]]
    # print(savepoints)
    if len(savepoints):
        drawResultTriangle(savepoints)
        print(cur)
    elif len(extrasave):
        drawResultTriangle(extrasave)
    else:
        tk.messagebox.showinfo("Ошибка", "На данных точках невозможно построить треугольник")

def changeButtonClicked():
    newx= txtFieldChangeX.get()
    newy = txtFieldChangeY.get()
    try:
        newx = float(newx)
        newy = float(newy)
        toAdd = (newx, newy)
        selected = box.selection_get()
        selected = selected.split(';')
        tup = (float(selected[0]), float(selected[1]))
        for i in list:
            if tup == i:
                list.remove(i)
        if toAdd not in list:
            list.append(toAdd)
        listboxRefill()
    except Exception:
        tk.messagebox.showinfo("Ошибка", "Некорректная точка")
    finally:
        txtFieldChangeY.delete(0, 'end')
        txtFieldChangeX.delete(0, 'end')

def deleteButtonClicked():
    try:
        selected = box.selection_get()
        selected = selected.split(';')
        tup = (float(selected[0]), float(selected[1]))
        for i in list:
            if tup == i:
                list.remove(i)
        listboxRefill()
    except Exception:
        tk.messagebox.showinfo("Ошибка", "Не выбрана точка")


def clearCanvas():
    c.delete('all')

def clearListBox():
    box.delete(0, 'end')
    item = "{: ^17s};{: ^17s}".format("X", "Y")
    #box.insert('end', item)
    ######################################################## <------ DELETE THIS TO INSERT 'X;Y' IN TABLE

def listboxRefill():
    clearListBox()
    for i in list:
        x = i[0]
        y = i[1]
        item = lboxFormatter(x, y)
        box.insert('end', item)

def clearAll():
    clearCanvas()
    list.clear()
    clearListBox()

def addPoint(x, y):
    itemList = (x, y)
    itemBox = lboxFormatter(x, y)
    list.append(itemList)
    box.insert('end', itemBox)




##constants#
YOFADD = 120
XSAFE = -325
############
####main####
############


root = tk.Tk()
root.geometry("700x700+700+700")





#print(pointsMidhtBeTriangle(1, 1, 1, 1, 1, 1))

################################ Box ######################################
box = tk.Listbox()
# addPoint(120, 0)
# addPoint(90, 60)
# addPoint(0, 0)
# addPoint(50, 2)
# addPoint(92, 50)
# addPoint(50, 3)
# addPoint(0, 90)
x, y = normalToTkInter(-325, 340)
box.place(x=x, y=y, width=200, height=200)
###########################################################################

############################# Add point ###################################
addbtn = tk.Button(text="Добавить\nточку", command=addButtonClicked)
x, y = normalToTkInter(XSAFE+130, YOFADD + 2)
addbtn.place(x=x, y=y, width=65, height=35)

txtFieldOfX = tk.Entry()
txtFieldOfX.insert(0, "x")
x, y = normalToTkInter(XSAFE, YOFADD)
txtFieldOfX.place(x=x, y=y, width=60)


txtFieldOfY = tk.Entry()
txtFieldOfY.insert(0, "y")
x, y = normalToTkInter(XSAFE + 60, YOFADD)
txtFieldOfY.place(x=x, y=y, width=60)
###########################################################################

c = tk.Canvas(root, width=300, height=300, bg='grey')
x, y = normalToTkInter(50, 345)
c.place(x=x, y =y)



x, y = normalToTkInter(XSAFE, 0)
tk.Button(text="Решить", width = 23, command=test).place(x=x, y=y)

tk.Button(text="Очистить\nполе отрисовки", width = 23, command=clearCanvas).place(x=x, y=y+30)
tk.Button(text="Очистить все", width = 23, command=clearAll).place(x=x, y=y+75)


############################# Change/delete point ###################################

tk.Button(text="Изменить выделенную\nточку", width = 23, command=changeButtonClicked).place(x=x, y=y+170)

txtFieldChangeX = tk.Entry()
txtFieldChangeX.insert(0, "x")
y += 170
txtFieldChangeX.place(x=x+ 40, y= y + 45, width=60)



txtFieldChangeY = tk.Entry()
txtFieldChangeY.insert(0, "y")
txtFieldChangeY.place(x=x + 120, y= y + 45, width=60)

tk.Button(text="Удалить выделенную\nточку", width = 23, command=deleteButtonClicked).place(x=x, y=y+75)
#####################################################################################
info = "Задание:\n"
info += "На плокости дано множество точек.\n"
info += "Найти такой треугольник с вершинами в этих точках,\n"
info += "у которого разность максимального и минимального\n"
info += "количетсва точек, попавших в каждый из шести\n"
info += "треугольников, образованных пересечением\n"
info += "биссектрисс максимальна."

tk.Label(text=info).place(x = x+320, y = y - 100)
# tk.Button(text="test", width = 23, command=masOut).place(x=x+250, y=y)


root.mainloop()
