from functionForAlgo import *

# Алгоритм Грэхема
def GrahamHull(arrPoints: list):

    if len(arrPoints) < 3:
        return arrPoints

    # Выбираем минимальную точку, которая будет входить в выпуклую оболочку
    startPoint = min(arrPoints, key=lambda p: (p[0], p[1]))

    # Сортируем точки по полярному углу и если полярный угол одинаковый, то сортируем по длине
    sorted_points = sorted(arrPoints, key=lambda p: (angle(startPoint, p), distance(startPoint, p)))

    # Добавляем первые два элемента в нашу выпуклую оболочку
    convuxHull = [startPoint, sorted_points[0]]

    for i in range(1, len(sorted_points)):
        # Проходим циклом, пока три точки образуют не левый поворот или три точки лежат на прямой, убираем из стека последнюю точку
        while len(convuxHull) > 1 and ((orientation(convuxHull[-2], convuxHull[-1], sorted_points[i]) <= 0)):
            convuxHull.pop()
        # Иначе добавляем её в выпуклую оболочку
        convuxHull.append(sorted_points[i])

    return convuxHull


# Алгоритм Грэхема - Эндрю
def GrahamAnd(arrPoints: list):

    if len(arrPoints) < 3:
        return arrPoints

    # Соортируем наши точки по координатам в порядке возрастания
    sorted_points = sorted(arrPoints, key=lambda point: (point[0], point[1]))

    # Нашли минимальную точку, которая точно будет входить в выпуклую оболочку
    startPoint = sorted_points[0]

    # Делим нашу выпуклую оболочку на две части
    upperPart = []
    lowerPart = []

    # Кладем минимальные элемент в наш массив
    upperPart.append(startPoint)
    lowerPart.append(startPoint)

    # Добавляем в массив верхний части точки, которые не образуют правый поворот
    for i in range(1, len(sorted_points)):
        # Пока у нас верхней части массива >= двум элементов
        # И образуют левый поворот или они коллинеарны мы вынимаем из стека последний элемент
        # Иначе добавляем точку в верхнюю оболочку
        while len(upperPart) >= 2 and orientation(upperPart[-2], upperPart[-1], sorted_points[i]) >= 0:
            upperPart.pop()
        upperPart.append(sorted_points[i])

    # Добавляем в массив нижней части точки, которые не образуют левый поворот
    for i in range(1, len(sorted_points)):
        # Пока у нас нижней части массива >= двум элементов
        # И образуют правый поворот или они коллинеарны мы вынимаем из стека последний элемент
        # Иначе добавляем точку в верхнюю оболочку
        while len(lowerPart) >= 2 and orientation(lowerPart[-2], lowerPart[-1], sorted_points[i]) <= 0:
            lowerPart.pop()
        lowerPart.append(sorted_points[i])

    # Наша выпуклая оболочка, сначала добавляем в нее Верхнюю часть, дальше добавляем нижнюю часть, и без первого и последнего элемента, тк они есть в upperPart
    convex_hull = []
    convex_hull.extend(lowerPart)
    convex_hull.extend(upperPart[-2:0:-1])

    return convex_hull


# Алгоритм Джарвиса
def JarvisAlgo(arrPoints: list):

    if len(arrPoints) < 3:
        return arrPoints

    # Находим начальную точку
    startPoint = min(arrPoints, key=lambda p: (p[0], p[1]))

    # Создаем массив выпуклой оболочки и добавляем туда первый элемент
    convexHull = []
    convexHull.append(startPoint)

    # Говорим, что предыдущая точка равна нашей стартовой
    prevPoint = startPoint

    while True:
        # Наша точка кандидат на попадание в выпуклую оболочку
        currPoint = 0

        for point in arrPoints:
            # Если точка равна предыдущей, пропускаем её
            # if point == prevPoint:
            #     continue

            # На первом шаге мы присвоим точку к кандидату и перейдем на следующую итерацию
            if currPoint == 0:
                currPoint = point
                continue

            # Если прямые лежат на одной прямой, то выбираем самую дальнюю
            if (orientation(prevPoint, currPoint, point) == 0 and (distance(prevPoint, currPoint) < distance(prevPoint, point))):
                currPoint = point

            # Если образуется поворот вправо(по часовой стрелке)
            elif orientation(prevPoint, currPoint, point) < 0:
                currPoint = point

        # Если мы прошли точки и вернулись к стартовой, то выходим из цикла
        if currPoint == startPoint:
            break

        # Добавляем точку кандидат в выпуклую оболочку
        convexHull.append(currPoint)
        prevPoint = currPoint

    return convexHull


def quickAlgorithm(arrPoints, leftPoint, rightPoint, side):
    newArrPoints = []
    result = []

    if side == 1:
        # Проходим по каждой точке нашего массива и добавляем её в верхнюю часть оболочки
        for point in arrPoints:
            if sidePoint(leftPoint, rightPoint, point) == 1:
                newArrPoints.append(point)
        if len(newArrPoints) > 0:
            # Вычисляем максимальную площать треугольника, которая образовалось
            # Благодаря трем точкам
            topPoint = maxSquare(newArrPoints, leftPoint, rightPoint)
            # Добавляем точку в наш массив и повторяем наш алгоритм для
            # Следующих треугольников
            result.append(topPoint)
            result.extend(quickAlgorithm(newArrPoints, leftPoint, topPoint, side))
            result.extend(quickAlgorithm(newArrPoints, topPoint, rightPoint, side))
    else:
        # Проходим по каждой точке нашего массива и добавляем её в верхнюю часть оболочки
        for point in arrPoints:
            if sidePoint(leftPoint, rightPoint, point) == 0:
                newArrPoints.append(point)
        # Если в массиве есть хотя-бы одна точка выполняем
        if len(newArrPoints) > 0:
            # Вычисляем максимальную площать треугольника, которая образовалось
            # Благодаря трем точкам
            downPoint = maxSquare(newArrPoints, rightPoint, leftPoint)
            # Добавляем точку в наш массив и повторяем наш алгоритм для
            # Следующих треугольников
            result.append(downPoint)
            result.extend(quickAlgorithm(newArrPoints, leftPoint, downPoint, side))
            result.extend(quickAlgorithm(newArrPoints, downPoint, rightPoint, side))

    return result

def QuickHull(arrPoints):

    if len(arrPoints) < 3:
        return arrPoints

    # Берем минимальную точку и максимальную
    minPoint = min(arrPoints, key=lambda p: (p[0], p[1]))
    maxPoint = max(arrPoints, key=lambda p: (p[0], p[1]))

    result = []
    result1 = []
    convuxHull = []

    convuxHull.append(minPoint)
    # Вызываем и добавляем точки из нижней части
    result.extend(quickAlgorithm(arrPoints, minPoint, maxPoint, -1))
    result.sort()
    convuxHull.extend(result)
    convuxHull.append(maxPoint)

    # Вызываем и добавляем точки из верхней части
    result1.extend(quickAlgorithm(arrPoints, minPoint, maxPoint, 1))
    result1.sort()
    result1.reverse()
    convuxHull.extend(result1)

    return convuxHull