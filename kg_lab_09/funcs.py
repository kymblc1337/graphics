from point import *
from copy import deepcopy


def lineDrawer(xs, ys, xf, yf, canvas, color):
    canvas.create_line(xs, ys, xf, yf, fill=color)
    canvas.update()


def lineDrawer(start: Point, finish: Point, canvas, color):
    canvas.create_line(start.x, start.y, finish.x, finish.y, fill=color)
    canvas.update()


def vct(v1, v2):
    x1 = v1[0].x - v1[1].x
    y1 = v1[0].y - v1[1].y

    x2 = v2[0].x - v2[1].x
    y2 = v2[0].y - v2[1].y

    return x1 * y2 - x2 * y1


def visible(point, pointa, pointb, n):
    v = vct([point, pointa], [pointb, pointa])
    if n * v < 0:
        return True
    else:
        return False


def convex(polygone):
    flag = 1
    cp = polygone[0]  # iая вершина
    ci = polygone[1]  # i+1 вершина
    cn = polygone[2]  # i+2 вершина и все остальные

    # векторное произведение двух векторов
    x1 = ci.x - cp.x
    y1 = ci.y - cp.y

    x2 = cn.x - ci.x
    y2 = cn.y - ci.y

    # определяем знак ординаты
    r = x1 * y2 - x2 * y1
    prev = 0 if r == 0 else 1 if r > 0 else -1
    # prev = sign(r)

    for i in range(2, len(polygone) - 1):
        if not flag:
            break
        cp = polygone[i - 1]
        ci = polygone[i]
        cn = polygone[i + 1]

        # векторное произведение двух векторов
        x1 = ci.x - cp.x
        y1 = ci.y - cp.y

        x2 = cn.x - ci.x
        y2 = cn.y - ci.y

        r = x1 * y2 - x2 * y1
        curr = 0 if r == 0 else 1 if r > 0 else -1

        # если знак предыдущей координаты не совпадает, то возможно многоугольник невыпуклый
        if curr != prev:
            flag = 0
        prev = curr

    # не забываем проверить последнюю с первой вершины
    cp = polygone[len(polygone) - 2]
    ci = polygone[len(polygone) - 1]
    cn = polygone[0]

    # векторное произведение двух векторов
    x1 = ci.x - cp.x
    y1 = ci.y - cp.y

    x2 = cn.x - ci.x
    y2 = cn.y - ci.y

    r = x1 * y2 - x2 * y1
    curr = 0 if r == 0 else 1 if r > 0 else -1
    if curr != prev:
        flag = 0

    return flag * curr


def sutherlandHodgman(cutter, figure, norm):
    # дублируем начальную вершину отсекателя в конец
    cutter.append(cutter[0])
    tmp = figure

    s = None
    f = None
    # цикл по вершинам отсекателя
    for i in range(len(cutter) - 1):
        new = []  # новый массив вершин
        for j in range(len(tmp)):  # цикл по вершинам многоугольника
            if j == 0:
                f = tmp[j]
            else:
                t = getIntersection([s, tmp[j]], [cutter[i], cutter[i + 1]], norm)
                if t:
                    new.append(t)

            s = tmp[j]
            if visible(s, cutter[i], cutter[i + 1], norm):
                new.append(s)

        if len(new) != 0:
            t = getIntersection([s, f], [cutter[i], cutter[i + 1]], norm)
            if t:
                new.append(t)

        tmp = new

    if len(tmp) == 0:
        return False
    else:
        return tmp


def getIntersection(l1, l2, norm):
    vis1 = visible(l1[0], l2[0], l2[1], norm)
    vis2 = visible(l1[1], l2[0], l2[1], norm)
    if (vis1 and not vis2) or (not vis1 and vis2):
        # ищем пересечение

        p1 = l1[0]
        p2 = l1[1]

        q1 = l2[0]
        q2 = l2[1]

        delta = (p2.x - p1.x) * (q1.y - q2.y) - (q1.x - q2.x) * (p2.y - p1.y)
        delta_t = (q1.x - p1.x) * (q1.y - q2.y) - (q1.x - q2.x) * (q1.y - p1.y)

        if abs(delta) <= 1e-6:
            return p2

        t = delta_t / delta

        result = Point((l1[0].x + (l1[1].x - l1[0].x) * t), (l1[0].y + (l1[1].y - l1[0].y) * t))
        return result
    else:
        return False
