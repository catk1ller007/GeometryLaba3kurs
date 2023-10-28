import math

# Вычисляем полярный угол
def angle(p0, p1):
    x1, y1 = p1[0] - p0[0], p1[1] - p0[1]
    return math.atan2(y1, x1)

# Вычисляет дистанцию между двумя точками
def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    dx = x2 - x1
    dy = y2 - y1
    return dx ** 2 + dy ** 2


# > 0 CWW(Counter Clockwise) - это поворот влево или против часовой стрелки
# < 0 CW (Clockwise) - это поворот вправо или по часовой стрелке
# == 0 Коллинеарны
def orientation(p1, p2, p3):
    return p1[0] * (p2[1] - p3[1]) + p2[0] * (p3[1] - p1[1]) + p3[0] * (p1[1] - p2[1])


# Площать треугольника по трем точкам
def squareTriangle(p1, p2, p3):
    return 0.5 * (p1[0] * (p2[1] - p3[1]) + p2[0] * (p3[1] - p1[1]) + p3[0] * (p1[1] - p2[1]))

 # Функция, которая находит максимальную площадь треугольника по трем точкам
def maxSquare(arrpoints, min_point, max_point):
    maxSquarePoint = None
    maxSquare = 0
    for i in range(len(arrpoints)):
        curSquare = squareTriangle(min_point, max_point, arrpoints[i])
        if maxSquare < curSquare:
            maxSquare = curSquare
            maxSquarePoint = arrpoints[i]
    return maxSquarePoint

def sidePoint(l, r, p):
    x, y = p
    x1, y1 = l
    x2, y2 = r
    D = (y2 - y1) * (x - x1) - (y - y1) * (x2 - x1)
    if D < 0:
        return 1
    if D > 0:
        return 0