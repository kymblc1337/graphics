import tkinter as tk
from point import *
from math import sqrt, pi, cos, sin



def libDrawCircle(xc, yc, r, canvas, color):
    canvas.create_oval(xc - r, yc - r, xc + r, yc + r, outline=color)


def canonicCircle(xc, yc, r, canvas, color):
    dx = round(r / sqrt(2))
    r = r ** 2
    for x in range(0, dx + 1):
        y = round(sqrt(r - x ** 2))
        #drawPixel(xc + x, yc + y, canvas, color)
        draw8Points(xc, yc, x, y, canvas, color)


def parametricCircle(xc, yc, r, canvas, color):
    t = 0
    s = 1 / r
    while t < (pi/4):
        x = round(r * cos(t))
        y = round(r * sin(t))
        draw8Points(xc, yc, x, y, canvas, color)
        t += s

def bresCircle(xc, yc, r, canvas, color):
    x = 0
    y = r
    d = 2 * (1 - r)
    while y >= sqrt(2) * r // 2:
        #drawPixel(xc + x, yc - y, canvas, color)
        draw8Points(xc, yc, x, y, canvas, color)
        if d < 0:
            d1 = 2 * d + 2 * y - 1
            if d1 < 0:
                x = x + 1
                d = d + 2 * x + 1
            else:
                x += 1
                y -= 1
                d = d + 2 * (x - y + 1)
        elif d == 0:
            x += 1
            y -= 1
            d = d + 2 * (x - y + 1)

        elif d > 0:
            d2 = 2 * d - 2 * x - 1
            if d2 < 0:
                x += 1
                y -= 1
                d = d + 2 * (x - y + 1)
            else:
                y -= 1
                d = d - 2 * y + 1


def middlePointCircle(xc, yc, r, canvas, color):
    x = 0
    y = r
    p = 5 / 4 - r
    while x <= y:
        #drawPixel(xc + x, yc + y, canvas, color)
        draw8Points(xc, yc, x, y, canvas, color)
        x += 1
        if p < 0:
            p += 2 * x + 1
        else:
            p += 2 * x - 2 * y + 5
            y -= 1
