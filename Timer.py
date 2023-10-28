from Algorithms import *
import time
def timer(points):

    # Таймер засекающий время работы алгоритмов
    # Засекаем время
    startTime1 = time.time()
    outJarvis = JarvisAlgo(points)
    endTime1 = time.time()
    timeJarvis = endTime1 - startTime1

    startTime2 = time.time()
    outGraham = GrahamHull(points)
    endTime2 = time.time()
    timeGraham = endTime2 - startTime2

    startTime3 = time.time()
    outGrahamAndr = GrahamAnd(points)
    endTime3 = time.time()
    timeGrahamAndr = endTime3 - startTime3

    startTime4 = time.time()
    outQuickHull = QuickHull(points)
    endTime4 = time.time()
    timeQuickHull = endTime4 - startTime4

    print(f"Время выполнения: \n"
          f"Джарвис = {timeJarvis}\n"
          f"Грэхем = {timeGraham}\n"
          f"Грэхем-Эндрю = {timeGrahamAndr}\n"
          f"Быстрая оболочка = {timeQuickHull}")
