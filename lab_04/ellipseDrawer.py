from math import pi, sin, cos, sqrt
from point import *


def libDrawEllipse(xc, yc, a, b, canvas, color):
    canvas.create_oval(xc - a, yc - b, xc + a, yc + b, outline=color)


def canonicEllipse(xc, yc, a, b, canvas, color):
    a2 = a ** 2
    b2 = b ** 2
    aDivB = a / b
    bDivA = b / a
    dx = round(a2 / sqrt(a2 + b2))
    for x in range(0, dx + 1):
        y = round(sqrt(a2 - x ** 2) * bDivA)
        draw4Points(xc, yc, x, y, canvas, color)

    dy = round(b2 / sqrt(a2 + b2))
    for y in range(0, dy + 1):
        x = round(sqrt(b2 - y ** 2) * aDivB)
        draw4Points(xc, yc, x, y, canvas, color)


def parametricEllipse(xc, yc, a, b, canvas, color):
    t = 0
    s = 1 / max(a, b)
    while t < (pi / 2):
        x = round(a * cos(t))
        y = round(b * sin(t))
        draw4Points(xc, yc, x, y, canvas, color)
        t += s


def bresEllispe(xc, yc, a, b, canvas, color):
    x = 0
    y = b
    aInPower2 = a * a
    bInPower2 = b * b
    twoAInPower2 = 2 * aInPower2
    twoBInPower2 = 2 * bInPower2
    d = aInPower2 + bInPower2 - 2 * aInPower2 * y
    while y >= 0:
        draw4Points(xc, yc, x, y, canvas, color)
        if d < 0:
            d1 = 2 * d + twoAInPower2 * y - aInPower2
            x += 1
            if d1 <= 0:
                d = d + twoBInPower2 * x + bInPower2
            else:
                y -= 1
                d = d + twoBInPower2 * x - twoAInPower2 * y + aInPower2 + bInPower2
        elif d > 0:
            d2 = 2 * d - twoBInPower2 * x - bInPower2
            y -= 1
            if d2 > 0:
                d = d - y * twoAInPower2 + aInPower2
            else:
                x += 1
                d = d + x * twoBInPower2 - y * twoAInPower2 + aInPower2 + bInPower2
        elif d == 0:
            x += 1
            y -= 1
            d = d + x * twoBInPower2 - y * twoAInPower2 + aInPower2 + bInPower2


def middlePointEllispe(xc, yc, a, b, canvas, color):
    x = 0
    y = b
    aInPower2 = a * a
    bInPower2 = b * b
    twoAInPower2 = 2 * aInPower2
    twoBInPower2 = 2 * bInPower2
    p = bInPower2 - aInPower2 * b + 0.25 * aInPower2
    while bInPower2 * x < aInPower2 * y:
        draw4Points(xc, yc, x, y, canvas, color)
        x += 1
        if p < 0:
            p += twoBInPower2 * x + bInPower2
        else:
            y -= 1
            p += twoBInPower2 * x - twoAInPower2 * y + bInPower2
    p = bInPower2 * (x + 0.5) * (x + 0.5) + aInPower2 * (y - 1) * (y - 1) - aInPower2 * bInPower2
    while y >= 0:
        draw4Points(xc, yc, x, y, canvas, color)
        y -= 1
        if p > 0:
            p -= twoAInPower2 * y + aInPower2
        else:
            x += 1
            p += twoBInPower2 * x - twoAInPower2 * y + aInPower2
