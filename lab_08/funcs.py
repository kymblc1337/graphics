from point import *

def lineDrawer(xs, ys, xf, yf, canvas, color):
    canvas.create_line(xs, ys, xf, yf, fill=color)
    canvas.update()

def lineDrawer(start: Point, finish: Point, canvas, color):
    canvas.create_line(start.x, start.y, finish.x, finish.y, fill=color)
    canvas.update()

def sign(x):
    if x == 0:
        return 0
    if x > 0:
        return 1
    return -1

def convex(polygone):
    flag = 1

    # начальные вершины
    vo = polygone[0]  # iая вершина
    vi = polygone[1]  # i+1 вершина
    vn = polygone[2]  # i+2 вершина и все остальные

    # векторное произведение двух векторов
    x1 = vi.x - vo.x
    y1 = vi.y - vo.y

    x2 = vn.x - vi.x
    y2 = vn.y - vi.y

    # определяем знак ординаты
    r = x1 * y2 - x2 * y1
    prev = 0 if r == 0 else 1 if r > 0 else -1
    #prev = sign(r)

    for i in range(2, len(polygone) - 1):
        if not flag:
            break
        vo = polygone[i - 1]
        vi = polygone[i]
        vn = polygone[i + 1]

        # векторное произведение двух векторов
        x1 = vi.x - vo.x
        y1 = vi.y - vo.y

        x2 = vn.x - vi.x
        y2 = vn.y - vi.y

        r = x1 * y2 - x2 * y1
        curr = sign(r)

        # если знак предыдущей координаты не совпадает, то возможно многоугольник невыпуклый
        if curr != prev:
            flag = 0
        prev = curr

    # не забываем проверить последнюю с первой вершины
    vo = polygone[len(polygone) - 2]
    vi = polygone[len(polygone) - 1]
    vn = polygone[0]

    # векторное произведение двух векторов
    x1 = vi.x - vo.x
    y1 = vi.y - vo.y

    x2 = vn.x - vi.x
    y2 = vn.y - vi.y

    r = x1 * y2 - x2 * y1
    curr = sign(r)
    if curr != prev:
        flag = 0

    return flag * curr

def cyrus_beck(line, edges, n, canvas):
    # инициализируем пределы значений параметра, предполагая, что весь отрезок полностью видимый
    # максимизируем t нижнее и t верхнее, исходя из того что 0 <= t <= 1
    tb = 0
    te = 1

    # вычисляем директрису(определяет направление/ориентацию отрезка) D= p1 - p2
    D = Point(x=line[1].x - line[0].x, y=line[1].y - line[0].y)

    # главный цикл по сторонам отсекателя
    for i in range(len(edges)):
        # вычисляем wi, D * ni, wi * n
        # весовой множитель удаленности гранничной точки от р1(берем граничную точку равной вершине)
        W = Point(x=line[0].x - edges[i].x, y=line[0].y - edges[i].y)

        # определяем нормаль
        if i == len(edges) - 1:
            N = Point(x=-n * (edges[0].y - edges[i].y), y=n * (edges[0].x - edges[i].x))
        else:
            N = Point(x=-n * (edges[i + 1].y - edges[i].y), y=n * (edges[i + 1].x - edges[i].x))
        # определяем скалярные произведения
        Dscalar = D.x * N.x + D.y * N.y
        Wscalar = W.x * N.x + W.y * N.y

        if Dscalar == 0:
            # если отрезок параллелен ребру отсекателю
            if Wscalar < 0:
                # виден ли?
                return
        else:
            # отрезок невырожден, определяем t
            t = - Wscalar / Dscalar
            # поиск верхнего и нижнего предела t

            if Dscalar > 0:
                # поиск нижнего предела
                # верно ли, что t <= 1
                if t > 1:
                    return
                else:
                    tb = max(tb, t)
            elif Dscalar < 0:
                # поиск верхнего предела
                # верно ли, что t >= 0
                if t < 0:
                    return
                else:
                    te = min(te, t)

        # проверка фактической видимости отрезка
    if tb <= te:
        lineDrawer(Point(line[0].x + (line[1].x - line[0].x) * te,
                   line[0].y + (line[1].y - line[0].y) * te), Point(
                   line[0].x + (line[1].x - line[0].x) * tb,
                   line[0].y + (line[1].y - line[0].y) * tb), canvas, "blue")
        '''scene.addLine(line[0].x + (line[1].x - line[0].x) * te,
                      line[0].y + (line[1].y - line[0].y) * te,
                      line[0].x + (line[1].x - line[0].x) * tb,
                      line[0].y + (line[1].y - line[0].y) * tb, p)'''