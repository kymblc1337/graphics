from PIL import Image, ImageTk

class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def __eq__(self, other):
        return self.r == other.r and self.g == other.g and self.b == other.b


whiteColor = Color(255, 255, 255)
redColor = Color(255, 0, 0)
blackColor = Color(1, 1, 1)
greenColor = Color(0, 255, 0)
blueColor = Color(0, 0, 255)



def isBackGround(r, g, b):
    return (r == g == b) and (r == 255)


def RGBtoString(r: int, g: int, b: int):
    if r == 255 and g == 0 and b == 0:
        return "red"
    elif r == 0 and g == 255 and b == 0:
        return "green"
    elif r == 0 and g == 0 and b == 255:
        return "blue"
    elif r == 255 and g == 255 and b == 255:
        return "white"
    elif r == 1 and g == 1 and b == 1:
        return "black"


def stringToRgb(color: str):
    if color == "red":
        r = 255
        g = 0
        b = 0
    elif color == "green":
        r = 0
        g = 255
        b = 0
    elif color == "blue":
        r = 0
        g = 0
        b = 255
    elif color == "white":
        r = 255
        g = 255
        b = 255
    else:
        r = 1
        g = 1
        b = 1
    return r, g, b


def getPixelColor(img, x, y):
    coordinate = x, y
    r, g, b = img.getpixel(coordinate)
    clr = Color(r, g, b)
    return clr


def changePixelColor(img, x, y, canvas, color: Color):
    r, g, b = getPixelColor(img, x, y)
    if isBackGround(r, g, b):
        drawPixel(x, y, canvas, img, color)
    elif r == color.r and b == color.b and g == color.g:
        clearPixel(x, y, canvas, img)
    else:
        pass

def clearPixel(x, y, canvas, img):
    x, y = int(x), int(y)
    img.putpixel((x, y), (255, 255, 255))
    colorizer = "#%02x%02x%02x" % (255, 255, 255)
    canvas.create_rectangle(x, y, x, y, width=0, fill=colorizer, outline=colorizer)

def drawPixel(x, y, canvas, img, color: Color):
    x, y = int(x), int(y)
    img.putpixel((x, y), (color.r, color.g, color.b))
    colorizer = "#%02x%02x%02x" % (color.r, color.g, color.b)
    canvas.create_rectangle(x, y, x, y, width=0, fill=colorizer, outline=colorizer)


def getXIntersection(xs, ys, xf, yf, level):
    if level < min(ys, yf) or level > max(ys, yf) or ys == yf:
        return None
    if yf < ys:
        xs, ys, xf, yf = xf, yf, xs, ys
    dx = (xf - xs) / (yf - ys)
    return xs + dx * (level - ys)



