def pointsMidhtBeTriangle(x1, y1, x2, y2, x3, y3):
    try :
        if (x1 == x2) and (x2 == x3) and ((y1 == y2) or (y2 == y3)):
            return False
        if (y1 == y2) and (y2 == y3) and ((x1 == x2) or (x2 == x3)):
            return False
        if (x2 == x1):
            x1, x2, x3 = x2, x3, x1
        if (y2 == y1):
            y1, y2, y3 = y2, y3, y1
        if ((x3 - x1) / (x2 - x1) == (y3 - y1) / (y2 - y1)):
            return False
        else:
            return True
    except ZeroDivisionError:
        return False

def xyIsInsideABC(x, y, xa, ya, xb, yb, xc, yc):
    a = (xa - x) * (yb - ya) - (xb - xa) * (ya - y);
    b = (xb - x) * (yc - yb) - (xc - xb) * (yb - y);
    c = (xc - x) * (ya - yc) - (xa - xc) * (yc - y);
    if (a < 0) and (b < 0) and (c < 0):
        return True
    if (a > 0) and (b > 0) and (c > 0):
        return True
    else:
        return False

def getCoefficientsOfLineOfTwoPoints(xa, ya, xb, yb):
    a = yb - ya
    b = xa - xb
    c = -(yb - ya) * xa - (xa - xb) * ya
    return a, b, c

def getPointOfIntersections(a1, b1, c1, a2, b2, c2):
    try :
        if a1 == 0:
            #a1x + b1y + c1 = 0
            #a2x + b2y + c2 = 0
            y = -c1 / b1
            x = (-b2 * y - c2) / a2
        elif a2 == 0:
            y = -c2 / b2
            x = (-b1 * y - c1) / a1
        elif b1 == 0:
            x = -c1 / a1
            y = (-a2 * x - c2) / b2
        elif b2 == 0:
            x = -c2 / a2
            y = (-a1 * x - c1) / b1
        else :
            y = ((a2 / a1) * c1 - c2) / (b2 - b1 * (a2 / a1))
            x = (-b1 * y - c1) / a1
        return x, y
    except Exception:
        print("Error occured in getPointOfIntersections")
        print(a1, b1, c1)
        print(a2, b2, c2)
        return None, None




def getPointCThatDividesABLike(x1, y1, x2, y2, a, b):
    l = a / b
    x = (x1 + l * x2) / (1 + l)
    y = (y1 + l * y2) / (1 + l)
    return x, y

def getBisectorCoefficientsOfAngleABC(xa, ya, xb, yb, xc, yc):
    abVector = ((xb - xa), (yb - ya))
    acVector = ((xc - xa), (yc - ya))
    #bcVector = ((xc - xb), (yc - yb))
    #getBisectorCoefficientsOfAngleABC(2, 1, 1, -2, -1, 0)
    ablen = (abVector[0] ** 2 + abVector[1] ** 2)**(1/2)
    aclen = (acVector[0] ** 2 + acVector[1] ** 2)**(1/2)
    #bclen = (bcVector[0] ** 2 + bcVector[1] ** 2)**(1/2)
    a = [i / ablen for i in abVector]
    b = [i / aclen for i in acVector]
    print(a)
    print(b)
    ak = [a[i] + b[i] for i in range(2)]
    print(ak)

def getABlen(xa, ya, xb, yb):
    return ((xb - xa) ** 2 + (yb - ya) ** 2)**(1/2)