def drawPixel(x, y, canvas, color):
    if color == "white":
        canvas.create_line(x-1, y, x + 2, y, fill=color)
    else:
        canvas.create_line(x, y, x + 1, y, fill=color)  # fill=color,


def draw4Points(xc, yc, x, y, canvas, color):
    drawPixel(xc + x, yc + y, canvas, color)
    drawPixel(xc + x, yc - y, canvas, color)
    drawPixel(xc - x, yc + y, canvas, color)
    drawPixel(xc - x, yc - y, canvas, color)


def draw8Points(xc, yc, x, y, canvas, color):
    draw4Points(xc, yc, x, y, canvas, color)
    draw4Points(xc, yc, y, x, canvas, color)
