import tkinter as tk
from math import sin, cos, pi
from tkinter import messagebox
from copy import deepcopy

##constants#
YSAFE = 330
XSAFE = -325
flagCoordinatesShown = True


############

def getCanvasCoordinates(x, y):
    newx = x + 205
    newy = -y + 210
    return (newx, newy)


def clearCanvas():
    canvasField.delete('all')


class myPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def zoom(self, kx, ky, xm, ym):
        self.x = self.x * kx + (1 - kx) * xm
        self.y = self.y * ky + (1 - ky) * ym

    def getMSKCoordinates(self):
        return (self.x, self.y)

    def drawAsPoint(self):
        xc, yc = getCanvasCoordinates(self.x, self.y)
        canvasField.create_oval(xc - 1, yc - 1, xc + 1, yc + 1)

    def rotate(self, angle, xc, yc):
        tmp_x = xc + (self.x - xc) * cos(angle * pi / 180) + (self.y - yc) * sin(angle * pi / 180)
        tmp_y = yc + (self.y - yc) * cos(angle * pi / 180) - (self.x - xc) * sin(angle * pi / 180)
        self.x = tmp_x
        self.y = tmp_y

    def getMyPointObject(self):
        return myPoint(self.x, self.y)

    def getCoordinatesForCanvas(self):
        return getCanvasCoordinates(self.x, self.y)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setCoordinates(self, x, y):
        self.x = x
        self.y = y


class myAxis:
    def __init__(self):
        self.zeropoint = myPoint(0, 0)
        self.leftedge = myPoint(-80, 0)
        self.rightedge = myPoint(80, 0)
        self.upedge = myPoint(0, 80)
        self.downedge = myPoint(0, -40)
        self.xleft = myPoint(-20000, 0)
        self.xright = myPoint(20000, 0)
        self.yup = myPoint(0, 20000)
        self.ydown = myPoint(0, -20000)

    def scaleText(self, kx, ky, xm, ym):
        self.leftedge.zoom(kx, ky, xm, ym)
        self.rightedge.zoom(kx, ky, xm, ym)
        self.upedge.zoom(kx, ky, xm, ym)
        self.downedge.zoom(kx, ky, xm, ym)

    def drawPointCoordinate(self, x, y, mover, txt):
        textpoint = myPoint(x, y)
        if mover == 'up':
            textpoint.setCoordinates(x + 13, y + 6)
        elif mover == 'down':
            textpoint.setCoordinates(x + 13, y - 6)
        elif mover == 'left':
            textpoint.setCoordinates(x - 13, y - 6)
        else:
            textpoint.setCoordinates(x + 13, y - 6)
        canvasField.create_text(textpoint.getCoordinatesForCanvas(), text=txt, font="Verdana 9", fill='red')

    def draw(self):
        canvasField.create_line(self.xleft.getCoordinatesForCanvas(), self.xright.getCoordinatesForCanvas())
        canvasField.create_line(self.ydown.getCoordinatesForCanvas(), self.yup.getCoordinatesForCanvas())
        up = myPoint(0, 207)
        right = myPoint(5, 195)
        left = myPoint(-5, 195)
        canvasField.create_line(up.getCoordinatesForCanvas(), right.getCoordinatesForCanvas())
        canvasField.create_line(up.getCoordinatesForCanvas(), left.getCoordinatesForCanvas())
        up = myPoint(198, 5)
        right = myPoint(211, 0)
        down = myPoint(198, -5)
        canvasField.create_line(up.getCoordinatesForCanvas(), right.getCoordinatesForCanvas())
        canvasField.create_line(right.getCoordinatesForCanvas(), down.getCoordinatesForCanvas())
        textpoint = myPoint(198, 12)
        canvasField.create_text(textpoint.getCoordinatesForCanvas(), text="X", font="Verdana 12")
        textpoint = myPoint(12, 195)
        canvasField.create_text(textpoint.getCoordinatesForCanvas(), text="Y", font="Verdana 12")


    def drawSizes(self):
        a = self.zeropoint.getMSKCoordinates()
        self.drawPointCoordinate(a[0], a[1], 'right', '0, 0')
        a = self.upedge.getMSKCoordinates()
        self.drawPointCoordinate(a[0], a[1], 'up', '0, 80')

        a = self.downedge.getMSKCoordinates()
        self.drawPointCoordinate(a[0], a[1], 'down', '0, -40')

        a = self.leftedge.getMSKCoordinates()
        self.drawPointCoordinate(a[0], a[1], 'left', '-80, 0')

        a = self.rightedge.getMSKCoordinates()
        self.drawPointCoordinate(a[0], a[1], 'right', '80, 0')


class myWalls:
    def __init__(self):
        self.leftUp = myPoint(-80, 40)
        self.leftDown = myPoint(-80, -40)
        self.rightUp = myPoint(80, 40)
        self.rightDown = myPoint(80, -40)

    def move(self, dx, dy):
        self.leftUp.move(dx, dy)
        self.leftDown.move(dx, dy)
        self.rightUp.move(dx, dy)
        self.rightDown.move(dx, dy)

    def scale(self, kx, ky, xm, ym):
        self.leftUp.zoom(kx, ky, xm, ym)
        self.leftDown.zoom(kx, ky, xm, ym)
        self.rightUp.zoom(kx, ky, xm, ym)
        self.rightDown.zoom(kx, ky, xm, ym)

    def drawCarcas(self):
        self.leftDown.drawAsPoint()
        self.leftUp.drawAsPoint()
        self.rightDown.drawAsPoint()
        self.rightUp.drawAsPoint()

    def rotate(self, angle, xc, yc):
        self.leftUp.rotate(angle, xc, yc)
        self.leftDown.rotate(angle, xc, yc)
        self.rightUp.rotate(angle, xc, yc)
        self.rightDown.rotate(angle, xc, yc)

    def draw(self, color='black'):
        canvasField.create_line(self.leftUp.getCoordinatesForCanvas(), self.leftDown.getCoordinatesForCanvas(),
                                fill=color)
        canvasField.create_line(self.leftUp.getCoordinatesForCanvas(), self.rightUp.getCoordinatesForCanvas(),
                                fill=color)
        canvasField.create_line(self.leftDown.getCoordinatesForCanvas(), self.rightDown.getCoordinatesForCanvas(),
                                fill=color)
        canvasField.create_line(self.rightUp.getCoordinatesForCanvas(), self.rightDown.getCoordinatesForCanvas(),
                                fill=color)

    def getMinX(self):
        mas = []
        mas.append(self.leftUp.getX())
        mas.append(self.leftDown.getX())
        mas.append(self.rightDown.getX())
        mas.append(self.rightUp.getX())
        return min(mas)

    def getMinY(self):
        mas = []
        mas.append(self.leftUp.getY())
        mas.append(self.leftDown.getY())
        mas.append(self.rightDown.getY())
        mas.append(self.rightUp.getY())
        return min(mas)

    def getMaxX(self):
        mas = []
        mas.append(self.leftUp.getX())
        mas.append(self.leftDown.getX())
        mas.append(self.rightDown.getX())
        mas.append(self.rightUp.getX())
        return max(mas)

    def getMaxY(self):
        mas = []
        mas.append(self.leftUp.getY())
        mas.append(self.leftDown.getY())
        mas.append(self.rightDown.getY())
        mas.append(self.rightUp.getY())
        return max(mas)


class myRoof:
    def __init__(self):
        self.left = myPoint(-80, 40)
        self.right = myPoint(80, 40)
        self.up = myPoint(0, 80)

    def move(self, dx, dy):
        self.left.move(dx, dy)
        self.right.move(dx, dy)
        self.up.move(dx, dy)

    def scale(self, kx, ky, xm, ym):
        self.left.zoom(kx, ky, xm, ym)
        self.up.zoom(kx, ky, xm, ym)
        self.right.zoom(kx, ky, xm, ym)

    def rotate(self, angle, xc, yc):
        self.left.rotate(angle, xc, yc)
        self.up.rotate(angle, xc, yc)
        self.right.rotate(angle, xc, yc)

    def drawCarcas(self):
        self.left.drawAsPoint()
        self.up.drawAsPoint()
        self.right.drawAsPoint()

    def draw(self, color='black'):
        canvasField.create_line(self.left.getCoordinatesForCanvas(), self.right.getCoordinatesForCanvas(), fill=color)
        canvasField.create_line(self.left.getCoordinatesForCanvas(), self.up.getCoordinatesForCanvas(), fill=color)
        canvasField.create_line(self.right.getCoordinatesForCanvas(), self.up.getCoordinatesForCanvas(), fill=color)

    def getMinX(self):
        mas = []
        mas.append(self.left.getX())
        mas.append(self.right.getX())
        mas.append(self.up.getX())
        return min(mas)

    def getMinY(self):
        mas = []
        mas.append(self.left.getY())
        mas.append(self.right.getY())
        mas.append(self.up.getY())
        return min(mas)

    def getMaxX(self):
        mas = []
        mas.append(self.left.getX())
        mas.append(self.right.getX())
        mas.append(self.up.getX())
        return max(mas)

    def getMaxY(self):
        mas = []
        mas.append(self.left.getY())
        mas.append(self.right.getY())
        mas.append(self.up.getY())
        return max(mas)


class myUpperWindow:
    def __init__(self):
        self.mas = []
        self.rad = 10
        self.step = int(180 // (self.rad * pi))
        for i in range(0, 360, self.step):
            new = myPoint(-0 + self.rad * cos(i * pi / 180), 55 + self.rad * sin(i * pi / 180))
            self.mas.append(new)
        ######################

        self.center = myPoint(0, 55)
        self.radiusx = 10
        self.radiusy = 10
        self.up = myPoint(0, 65)
        self.down = myPoint(0, 45)
        self.left = myPoint(-10, 55)
        self.right = myPoint(10, 55)
    def elps_init(self):
        self.mas = []
        self.rad = 10
        self.step = int(180 // (self.rad * pi))
        for i in range(0, 360, self.step):
            new = myPoint(-0 + self.rad * cos(i * pi / 180), 55 + self.rad * sin(i * pi / 180))
            self.mas.append(new)

    def elps_move(self, dx, dy):
        for i in range(0, len(self.mas)):
            self.mas[i].move(dx, dy)

    def move(self, dx, dy):
        self.center.move(dx, dy)
        self.up.move(dx, dy)
        self.down.move(dx, dy)
        self.left.move(dx, dy)
        self.right.move(dx, dy)

    def elps_scale(self, kx, ky, xm, ym):
        for i in range(0, len(self.mas)):
            self.mas[i].zoom(kx, ky, xm, ym)

    def scale(self, kx, ky, xm, ym):
        self.center.zoom(kx, ky, xm, ym)
        self.radiusx *= kx
        self.radiusy *= ky
        self.up.zoom(kx, ky, xm, ym)
        self.down.zoom(kx, ky, xm, ym)
        self.left.zoom(kx, ky, xm, ym)
        self.right.zoom(kx, ky, xm, ym)

    def elps_rotate(self, angle, xc, yc):
        for i in range(0, len(self.mas)):
            self.mas[i].rotate(angle, xc, yc)

    def rotate(self, angle, xc, yc):
        self.center.rotate(angle, xc, yc)
        self.up.rotate(angle, xc, yc)
        self.down.rotate(angle, xc, yc)
        self.left.rotate(angle, xc, yc)
        self.right.rotate(angle, xc, yc)

    def draw_as_ellipse(self):
        for i in range(1, len(self.mas)):
            first = self.mas[i].getCoordinatesForCanvas()
            second = self.mas[i - 1].getCoordinatesForCanvas()
            canvasField.create_line(first, second)
        first = self.mas[0].getCoordinatesForCanvas()
        second = self.mas[len(self.mas) - 1].getCoordinatesForCanvas()
        canvasField.create_line(first, second)
        centx, centy = self.center.getCoordinatesForCanvas()
        canvasField.create_line(self.left.getCoordinatesForCanvas(), self.right.getCoordinatesForCanvas())
        canvasField.create_line(self.up.getCoordinatesForCanvas(), self.down.getCoordinatesForCanvas())

class myRightWindow:
    def __init__(self):
        self.leftUp = myPoint(30, 30)
        self.leftDown = myPoint(30, -20)
        self.rightUp = myPoint(60, 30)
        self.rightDown = myPoint(60, -20)
        self.upmid = myPoint(45, 30)
        self.downmid = myPoint(45, -20)
        self.leftmid = myPoint(30, 5)
        self.rightmid = myPoint(60, 5)

    def move(self, dx, dy):
        self.leftUp.move(dx, dy)
        self.leftDown.move(dx, dy)
        self.rightUp.move(dx, dy)
        self.rightDown.move(dx, dy)
        self.upmid.move(dx, dy)
        self.downmid.move(dx, dy)
        self.leftmid.move(dx, dy)
        self.rightmid.move(dx, dy)

    def scale(self, kx, ky, xm, ym):
        self.leftUp.zoom(kx, ky, xm, ym)
        self.leftDown.zoom(kx, ky, xm, ym)
        self.rightUp.zoom(kx, ky, xm, ym)
        self.rightDown.zoom(kx, ky, xm, ym)
        self.upmid.zoom(kx, ky, xm, ym)
        self.downmid.zoom(kx, ky, xm, ym)
        self.leftmid.zoom(kx, ky, xm, ym)
        self.rightmid.zoom(kx, ky, xm, ym)

    def rotate(self, angle, xc, yc):
        self.leftUp.rotate(angle, xc, yc)
        self.leftDown.rotate(angle, xc, yc)
        self.rightUp.rotate(angle, xc, yc)
        self.rightDown.rotate(angle, xc, yc)
        self.upmid.rotate(angle, xc, yc)
        self.downmid.rotate(angle, xc, yc)
        self.leftmid.rotate(angle, xc, yc)
        self.rightmid.rotate(angle, xc, yc)

    def draw(self, color='black'):
        canvasField.create_line(self.leftUp.getCoordinatesForCanvas(), self.leftDown.getCoordinatesForCanvas(),
                                fill=color)
        canvasField.create_line(self.leftUp.getCoordinatesForCanvas(), self.rightUp.getCoordinatesForCanvas(),
                                fill=color)
        canvasField.create_line(self.leftDown.getCoordinatesForCanvas(), self.rightDown.getCoordinatesForCanvas(),
                                fill=color)
        canvasField.create_line(self.rightUp.getCoordinatesForCanvas(), self.rightDown.getCoordinatesForCanvas(),
                                fill=color)
        canvasField.create_line(self.leftmid.getCoordinatesForCanvas(), self.upmid.getCoordinatesForCanvas(),
                                fill=color)
        canvasField.create_line(self.upmid.getCoordinatesForCanvas(), self.rightmid.getCoordinatesForCanvas(),
                                fill=color)
        canvasField.create_line(self.rightmid.getCoordinatesForCanvas(), self.downmid.getCoordinatesForCanvas(),
                                fill=color)
        canvasField.create_line(self.downmid.getCoordinatesForCanvas(), self.leftmid.getCoordinatesForCanvas(),
                                fill=color)


class myLeftWindow:
    def __init__(self):
        self.leftUp = myPoint(-55, 30)
        self.leftDown = myPoint(-55, -20)
        self.rightUp = myPoint(-25, 30)
        self.rightDown = myPoint(-25, -20)
        self.upmid = myPoint(-40, 30)
        self.downmid = myPoint(-40, -20)
        self.leftmid = myPoint(-55, 5)
        self.rightmid = myPoint(-25, 5)
        self.midmid = myPoint(-40, 5)

    def move(self, dx, dy):
        self.leftUp.move(dx, dy)
        self.leftDown.move(dx, dy)
        self.rightUp.move(dx, dy)
        self.rightDown.move(dx, dy)
        self.upmid.move(dx, dy)
        self.downmid.move(dx, dy)
        self.leftmid.move(dx, dy)
        self.rightmid.move(dx, dy)
        self.midmid.move(dx, dy)

    def scale(self, kx, ky, xm, ym):
        self.leftUp.zoom(kx, ky, xm, ym)
        self.leftDown.zoom(kx, ky, xm, ym)
        self.rightUp.zoom(kx, ky, xm, ym)
        self.rightDown.zoom(kx, ky, xm, ym)
        self.upmid.zoom(kx, ky, xm, ym)
        self.downmid.zoom(kx, ky, xm, ym)
        self.leftmid.zoom(kx, ky, xm, ym)
        self.rightmid.zoom(kx, ky, xm, ym)
        self.midmid.zoom(kx, ky, xm, ym)

    def rotate(self, angle, xc, yc):
        self.leftUp.rotate(angle, xc, yc)
        self.leftDown.rotate(angle, xc, yc)
        self.rightUp.rotate(angle, xc, yc)
        self.rightDown.rotate(angle, xc, yc)
        self.upmid.rotate(angle, xc, yc)
        self.downmid.rotate(angle, xc, yc)
        self.leftmid.rotate(angle, xc, yc)
        self.rightmid.rotate(angle, xc, yc)
        self.midmid.rotate(angle, xc, yc)

    def draw(self, color='black'):
        canvasField.create_line(self.leftUp.getCoordinatesForCanvas(), self.leftDown.getCoordinatesForCanvas(),
                                fill=color)
        canvasField.create_line(self.leftUp.getCoordinatesForCanvas(), self.rightUp.getCoordinatesForCanvas(),
                                fill=color)
        canvasField.create_line(self.leftDown.getCoordinatesForCanvas(), self.rightDown.getCoordinatesForCanvas(),
                                fill=color)
        canvasField.create_line(self.rightUp.getCoordinatesForCanvas(), self.rightDown.getCoordinatesForCanvas(),
                                fill=color)
        canvasField.create_line(self.leftmid.getCoordinatesForCanvas(), self.rightmid.getCoordinatesForCanvas(),
                                fill=color)
        canvasField.create_line(self.downmid.getCoordinatesForCanvas(), self.midmid.getCoordinatesForCanvas(),
                                fill=color)

class myEllipse:
    def __init__(self):
        self.mas = []
        self.xlen = 15
        self.ylen = 5
        self.step = int(180 // (self.xlen * pi))
        for i in range(0, 180, self.step):
            new = myPoint(-40 + self.xlen * cos(i * pi / 180), 30 + self.ylen * sin(i * pi / 180))
            self.mas.append(new)
    def move(self, dx, dy):
        for i in self.mas:
            i.move(dx, dy)
    def scale(self, kx, ky, xm, ym):
        for i in self.mas:
            i.zoom(kx, ky, xm, ym)
    def rotate(self, angle, xc, yc):
        for i in self.mas:
            i.rotate(angle, xc, yc)
    def draw(self):
        for i in range(1, len(self.mas) ):
            first = self.mas[i].getCoordinatesForCanvas()
            second = self.mas[i - 1].getCoordinatesForCanvas()
            canvasField.create_line(first, second)

class myObject:
    def __init__(self):
        self.wall = myWalls()
        self.roof = myRoof()
        self.upperWindow = myUpperWindow()
        self.rightWindow = myRightWindow()
        self.leftWindow = myLeftWindow()
        self.elips = myEllipse()
    def move(self, dx, dy):
        self.wall.move(dx, dy)
        self.roof.move(dx, dy)
        self.upperWindow.move(dx, dy)
        self.rightWindow.move(dx, dy)
        self.leftWindow.move(dx, dy)
        self.elips.move(dx, dy)
        self.upperWindow.elps_move(dx, dy)
    def zoom(self, kx, ky, xm, ym):
        self.wall.scale(kx, ky, xm, ym)
        self.roof.scale(kx, ky, xm, ym)
        self.upperWindow.scale(kx, ky, xm, ym)
        self.rightWindow.scale(kx, ky, xm, ym)
        self.leftWindow.scale(kx, ky, xm, ym)
        self.elips.scale(kx, ky, xm, ym)
        self.upperWindow.elps_scale(kx, ky, xm, ym)
    def rotate(self, angle, xc, yc):
        self.wall.rotate(angle, xc, yc)
        self.roof.rotate(angle, xc, yc)
        self.upperWindow.rotate(angle, xc, yc)
        self.rightWindow.rotate(angle, xc, yc)
        self.leftWindow.rotate(angle, xc, yc)
        self.elips.rotate(angle, xc, yc)
        self.upperWindow.elps_rotate(angle, xc, yc)
    def draw(self):
        self.wall.draw()
        self.roof.draw()
        #self.upperWindow.draw()
        self.rightWindow.draw()
        self.leftWindow.draw()
        self.elips.draw()
        self.upperWindow.draw_as_ellipse()
    def getCenter(self):
        xmax = []
        xmax.append(self.wall.getMaxX())
        xmax.append(self.roof.getMaxX())
        xmin = []
        xmin.append(self.wall.getMinX())
        xmin.append(self.roof.getMinX())
        ymax = []
        ymax.append(self.wall.getMaxY())
        ymax.append(self.roof.getMaxY())
        ymin = []
        ymin.append(self.wall.getMinY())
        ymin.append(self.roof.getMinY())
        xmax = max(xmax)
        xmin = min(xmin)
        ymax = max(ymax)
        ymin = min(ymin)
        xc = (xmax + xmin) // 2
        yc = (ymax + ymin) // 2
        return xc, yc

mySuperObject = myObject()
saveobject = myObject()

def resetDefault():
    clearCanvas()
    mySuperObject.__init__()
    mySuperObject.draw()
    axis.__init__()
    axis.draw()
    if flagCoordinatesShown:
        axis.drawSizes()


def drawCrd():
    clearCanvas()
    mySuperObject.draw()
    axis.draw()
    axis.drawSizes()


def clearCrd():
    clearCanvas()
    mySuperObject.draw()
    axis.draw()

def backstep():
    global saveobject, mySuperObject
    mySuperObject = deepcopy(saveobject)
    clearCanvas()
    mySuperObject.draw()
    axis.draw()
    if flagCoordinatesShown:
        axis.drawSizes()


def insertCenter():
    xc, yc = mySuperObject.getCenter()
    txtFieldRotateCenterX.delete(0, 'end')
    txtFieldRotateCenterY.delete(0, 'end')
    txtFieldRotateCenterX.insert(0, xc)
    txtFieldRotateCenterY.insert(0, yc)

    txtFieldZoomCenterX.delete(0, 'end')
    txtFieldZoomCenterY.delete(0, 'end')
    txtFieldZoomCenterX.insert(0, xc)
    txtFieldZoomCenterY.insert(0, yc)

def move():
    try:
        global saveobject, mySuperObject
        saveobject = deepcopy(mySuperObject)
        dx = float(txtFieldDx.get())
        dy = float(txtFieldDy.get())
        mySuperObject.move(dx, dy)
        clearCanvas()
        mySuperObject.draw()
        axis.draw()
        if flagCoordinatesShown:
            axis.drawSizes()
    except Exception:
        tk.messagebox.showinfo("Ошибка", "Проверьте корректность ввода данных")


def zoom():
    try:
        global saveobject, mySuperObject
        saveobject = deepcopy(mySuperObject)
        kx = float(txtFieldZoomX.get())
        ky = float(txtFieldZoomY.get())
        xm = float(txtFieldZoomCenterX.get())
        ym = float(txtFieldZoomCenterY.get())
        mySuperObject.zoom(kx, ky, xm, ym)
        axis.scaleText(kx, ky, xm, ym)
        clearCanvas()
        mySuperObject.draw()
        axis.draw()
        if flagCoordinatesShown:
            axis.drawSizes()
    except Exception:
        tk.messagebox.showinfo("Ошибка", "Проверьте корректность ввода данных")


def rotate():
    try:
        global saveobject, mySuperObject
        saveobject = deepcopy(mySuperObject)
        angle = float(txtFieldOfAngle.get())
        xc = float(txtFieldRotateCenterX.get())
        yc = float(txtFieldRotateCenterY.get())
        mySuperObject.rotate(angle, xc, yc)
        clearCanvas()
        mySuperObject.draw()
        axis.draw()
        if flagCoordinatesShown:
            axis.drawSizes()
    except Exception:
        tk.messagebox.showinfo("Ошибка", "Проверьте корректность ввода данных")


# class myObject:
#     def __init__(self):


def normalToTkInter(x, y):
    return (x + 330, -y + 345)


def masOut():
    print("MASOUT")
    for i in list:
        print(i)


def hideShow():
    global flagCoordinatesShown
    if flagCoordinatesShown:
        flagCoordinatesShown = False
        clearCrd()
    else:
        flagCoordinatesShown = True
        drawCrd()


#################################################################################
#################################################################################
################################### main ########################################
#################################################################################
#################################################################################

axis = myAxis()

root = tk.Tk()
root.geometry("700x700+700+700")

XCUR = XSAFE
YCUR = YSAFE
############################# Zoom ###################################
x, y = normalToTkInter(XCUR, YCUR - 150)
tk.Button(text="Масштабировать", command=zoom).place(x=x, y=y, width=150, height=30)

x, y = normalToTkInter(XCUR, YCUR + 3)
tk.Label(text="Коэффицент kx:", font="Veranda 10").place(x=x, y=y)

txtFieldZoomX = tk.Entry()
x, y = normalToTkInter(XCUR + 90, YCUR + 5)
txtFieldZoomX.place(x=x, y=y, width=60)

x, y = normalToTkInter(XCUR, YCUR - 40)
tk.Label(text="Коэффицент ky:", font="Veranda 10").place(x=x, y=y)

txtFieldZoomY = tk.Entry()
x, y = normalToTkInter(XCUR + 90, YCUR - 36)
txtFieldZoomY.place(x=x, y=y, width=60)

x, y = normalToTkInter(XCUR, YCUR - 76)
tk.Label(text="Центр x:", font="Veranda 10").place(x=x, y=y)

txtFieldZoomCenterX = tk.Entry()
x, y = normalToTkInter(XCUR + 90, YCUR - 76)
txtFieldZoomCenterX.place(x=x, y=y, width=60)

x, y = normalToTkInter(XCUR, YCUR - 116)
tk.Label(text="Центр y:", font="Veranda 10").place(x=x, y=y)

txtFieldZoomCenterY = tk.Entry()
x, y = normalToTkInter(XCUR + 90, YCUR - 116)
txtFieldZoomCenterY.place(x=x, y=y, width=60)
######################################################################
YCUR -= 220
############################# Move ###################################
x, y = normalToTkInter(XCUR, YCUR - 68)
tk.Button(text="Сместить", command=move).place(x=x, y=y, width=150, height=30)

x, y = normalToTkInter(XCUR, YCUR + 3)
tk.Label(text="dx:", font="Veranda 10").place(x=x, y=y)

txtFieldDx = tk.Entry()
x, y = normalToTkInter(XCUR + 90, YCUR + 5)
txtFieldDx.place(x=x, y=y, width=60)

x, y = normalToTkInter(XCUR, YCUR - 40)
tk.Label(text="dy:", font="Veranda 10").place(x=x, y=y)

txtFieldDy = tk.Entry()
x, y = normalToTkInter(XCUR + 90, YCUR - 36)
txtFieldDy.place(x=x, y=y, width=60)
######################################################################
YCUR -= 120

############################# Zoom ###################################
x, y = normalToTkInter(XCUR, YCUR - 150)
tk.Button(text="Повернуть", command=rotate).place(x=x, y=y, width=150, height=30)

x, y = normalToTkInter(XCUR, YCUR - 40)
tk.Label(text="Угол:", font="Veranda 10").place(x=x, y=y)

txtFieldOfAngle = tk.Entry()
x, y = normalToTkInter(XCUR + 90, YCUR - 36)
txtFieldOfAngle.place(x=x, y=y, width=60)

x, y = normalToTkInter(XCUR, YCUR - 76)
tk.Label(text="Центр x:", font="Veranda 10").place(x=x, y=y)

txtFieldRotateCenterX = tk.Entry()
x, y = normalToTkInter(XCUR + 90, YCUR - 76)
txtFieldRotateCenterX.place(x=x, y=y, width=60)

x, y = normalToTkInter(XCUR, YCUR - 116)
tk.Label(text="Центр y:", font="Veranda 10").place(x=x, y=y)

txtFieldRotateCenterY = tk.Entry()
x, y = normalToTkInter(XCUR + 90, YCUR - 116)
txtFieldRotateCenterY.place(x=x, y=y, width=60)
#####################################################################
#############################Canvas###################################
canvasField = tk.Canvas(root, width=415, height=415, bg='white')
x, y = normalToTkInter(-50, 345)
canvasField.place(x=x, y=y)

#############################Canvas###################################

x, y = normalToTkInter(XCUR, YCUR - 160)
tk.Button(text="Вернуть\nначальный рисунок", command=resetDefault).place(x=x, y=y + 30, width=150, height=40)

tk.Button(text="Отменить\nпоследнее действие", command=backstep).place(x=x+150, y=y + 30, width=150, height=40)

tk.Button(text="Показать/скрыть\nкоординаты", command=hideShow).place(x=x, y=y + 90, width=150, height=40)

tk.Button(text="Получить координаты\nцентра фигуры", command=insertCenter).place(x=x, y=y + 140, width=150, height=40)

resetDefault()

a = myUpperWindow()
a.elps_init()
a.draw_as_ellipse()


root.mainloop()
