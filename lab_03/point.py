from constants import *

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    def setx(self, x):
        self.x = x
    def sety(self, y):
        self.y = y
    def getCanvasCoordinates(self):
        x = self.x + CANVASSIZE//2
        y = - self.y + CANVASSIZE//2
        return Point(x, y)
    def drawAsPixel(self, canvas, color):
        #a = self.getCanvasCoordinates()
        #canvas.create_rectangle(a.x, a.y, a.x + 1, a.y+1, fill=color, outline = color)
        canvas.create_line(self.x, self.y, self.x + 1, self.y + 1, fill=color)

