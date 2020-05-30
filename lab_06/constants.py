WINDOWSIZE = 600
CANVASSIZE = 350

STRWINDOWSIZE = str(WINDOWSIZE) + 'x' + str(WINDOWSIZE) + '+' + str(WINDOWSIZE) + '+' + str(WINDOWSIZE)

def normalToTkInter(x, y):
    return (x + WINDOWSIZE//2.5, -y + WINDOWSIZE//2)

def getCanvasCoordinates(x, y):
    x += CANVASSIZE//2
    y = -y + CANVASSIZE//2
    return x, y