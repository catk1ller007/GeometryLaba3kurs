import time
from forFile import *
from Algorithms import *
from DrawAlgo import drawAlgo
from Test import *
from Timer import writeFile_time

input_file = "input.txt"
output_file = "output.txt"

# Чтение точек из файла
#points = read_file(input_file)
points = TestPoints(10000)

#----------------- Алгоритмы ----------------------#
outJarvis = JarvisAlgo(points)
outGraham = GrahamHull(points)
outGrahamAndr = GrahamAnd(points)
outQuickHull = QuickHull(points)


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



writeFile_time("timeJarvis" , len(points), timeJarvis)
writeFile_time("timeGraham" , len(points), timeGraham)
writeFile_time("timeGrahamAND" , len(points), timeGrahamAndr)
writeFile_time("timeQuick" , len(points), timeQuickHull)





# Запись алгоритмов
writeFile(output_file, outJarvis, outGraham, outGrahamAndr, outQuickHull)

# Рисовка точек и выпуклой оболочки
drawAlgo(points, outJarvis, "Джарвис")
#drawAlgo(points, outGraham, "Грэхем")
#drawAlgo(points, outGrahamAndr, "Грэхем-Эндрю")
#drawAlgo(points, outQuickHull, "Быстрая оболочка")
