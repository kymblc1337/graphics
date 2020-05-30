from point import Point
from math import floor
from constants import *



def fillRGBColor(canvas, color, bg_color, intensity):
    grad = []
    (r1, g1, b1) = canvas.winfo_rgb(color)  # разложение цвета линни на составляющие ргб
    (r2, g2, b2) = canvas.winfo_rgb(bg_color)  # разложение цвета фона на составляющие ргб
    r_ratio = float(r2 - r1) / intensity  # получение шага интенсивности
    g_ratio = float(g2 - g1) / intensity
    b_ratio = float(b2 - b1) / intensity
    for i in range(intensity):
        nr = int(r1 + (r_ratio * i))  # заполнение массива разными оттенками
        ng = int(g1 + (g_ratio * i))
        nb = int(b1 + (b_ratio * i))
        grad.append("#%4.4x%4.4x%4.4x" % (nr, ng, nb))
    grad.reverse()
    return grad


def bresenhamFloat(a, b, canvas, color):
    if (a.x == b.x) and (a.y == b.y):
        a.drawAsPixel(canvas, color)
    else:
        dx = b.x - a.x
        dy = b.y - a.y
        sx = -1 if dx < 0 else 1 if dx > 1 else 0
        sy = -1 if dy < 0 else 1 if dy > 1 else 0
        dx = abs(dx)
        dy = abs(dy)

        fl = 0
        if dy > dx:
            dx, dy = dy, dx
            fl = 1  # шагаем по y

        m = dy / dx
        error = m - 0.5

        x = a.x
        y = a.y
        i = 1

        while i <= dx:
            Point(int(x), int(y)).drawAsPixel(canvas, color)
            if error >= 0:
                if fl == 1:
                    x += sx
                else:
                    y += sy
                error -= 1
            if error < 0:
                if fl == 1:
                    y += sy
                else:
                    x += sx
                error += m
            i += 1


def cdaDrawer(a, b, canvas, color):
    if (a.x == b.x) and (a.y == b.y):
        a.drawAsPixel(canvas, color)
    else:
        dx = abs(b.x - a.x)
        dy = abs(b.y - a.y)

        if dx > dy:
            steep = dx
        else:
            steep = dy
        sx = (b.x - a.x) / steep
        sy = (b.y - a.y) / steep

        x = a.x
        y = a.y
        for i in range(int(steep + 1)):
            Point(x, y).drawAsPixel(canvas, color)
            x += sx
            y += sy


def basicDrawer(a, b, canvas, color):
    canvas.create_line(a.x, a.y, b.x, b.y, fill=color)


def bresenhamInt(a, b, canvas, color):
    if (a.x == b.x) and (a.y == b.y):
        a.drawAsPixel(canvas, color)
    else:
        dx = b.x - a.x
        dy = b.y - a.y
        sx = -1 if dx < 0 else 1 if dx > 1 else 0
        sy = -1 if dy < 0 else 1 if dy > 1 else 0
        dx = abs(dx)
        dy = abs(dy)

        fl = 0
        if dy > dx:
            dx, dy = dy, dx
            fl = 1  # шагаем по y

        error = 2 * dy - dx

        x = a.x
        y = a.y
        i = 1

        while i <= dx:
            Point(int(x), int(y)).drawAsPixel(canvas, color)
            if error >= 0:
                if fl == 1:
                    x += sx
                else:
                    y += sy
                error -= 2 * dx
            if error < 0:
                if fl == 1:
                    y += sy
                else:
                    x += sx
                error += 2 * dy
            i += 1


def bresenhamSmooth(a, b, canvas, color):
    if (a.x == b.x) and (a.y == b.y):
        a.drawAsPixel(canvas, color)
    else:
        Intens = 100
        dx = b.x - a.x
        dy = b.y - a.y
        sx = -1 if dx < 0 else 1 if dx > 1 else 0
        sy = -1 if dy < 0 else 1 if dy > 1 else 0
        dx = abs(dx)
        dy = abs(dy)

        fl = 0
        if dy > dx:
            dx, dy = dy, dx
            fl = 1  # шагаем по y

        m = (dy / dx) * Intens
        error = Intens / 2
        w = Intens - m

        x = a.x
        y = a.y
        i = 1

        fillingColor = fillRGBColor(canvas, color, 'white', Intens)

        while i <= dx:
            # Point(int(x), int(y)).drawAsPixel(canvas, color)
            # Point(x, y).drawAsPixel(canvas, fillingColor[round(error) - 1])
            # Point(int(x), int(y)).drawAsPixel(canvas, fillingColor[round(error) - 1])
            if error < w:
                if fl == 0:
                    x += sx
                else:
                    y += sy
                error += m
            elif error >= w:
                y += sy
                x += sx
                error -= w
            a = Point(x, y)
            canvas.create_line(a.x, a.y, a.x + 1, a.y + 1, fill=fillingColor[round(error) - 1])
            i += 1


def drawRGBPixel(canvas, x, y, color):
    p = Point(x, y).getCanvasCoordinates()
    #canvas.create_line(p.x, p.y, p.x + 1, p.y + 1, fill=color)
    canvas.create_rectangle(p.x, p.y, p.x, p.y, fill = color, outline = color)



def Vu(a, b, canvas, color):
    x1 = a.x
    x2 = b.x
    y1 = a.y
    y2 = b.y
    I = 100
    fillColor = fillRGBColor(canvas, color, "white", I)
    if x1 == x2 and y1 == y2:
        canvas.create_line(x1, y1, x1 + 1, y1 + 1, fill=fillColor[100])
    else:
        fl = abs(y2 - y1) > abs(x2 - x1)

        if fl:
            x1, y1 = y1, x1
            x2, y2 = y2, x2
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1

        dx = x2 - x1
        dy = y2 - y1

        if dx == 0:
            m = 1
        else:
            m = dy / dx

        xfrom = round(x1)
        #yend = y1 + m * (xfrom - x1)
        #y= yend + m
        y = y1
        xto = int(x2 + 0.5)

        # main loop
        if fl:
            for x in range(xfrom, xto):
                canvas.create_line(int(y), x + 1, int(y) + 1, x + 2,
                                  fill=fillColor[int((I - 1) * (abs(1 - y + int(y))))])
                canvas.create_line(int(y) + 1, x + 1, int(y) + 2, x + 2,
                                  fill=fillColor[int((I - 1) * (abs(y - int(y))))])
                y += m
        else:
            for x in range(xfrom, xto):
                canvas.create_line(x + 1, int(y), x + 2, int(y) + 1,
                                   fill=fillColor[round((I - 1) * (abs(1 - y + floor(y))))])
                canvas.create_line(x + 1, int(y) + 1, x + 2, int(y) + 2,
                                   fill=fillColor[round((I - 1) * (abs(y - floor(y))))])
                y += m


