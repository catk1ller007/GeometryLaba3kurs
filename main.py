import time
from forFile import *
from Algorithms import *
from DrawAlgo import drawAlgo
from Test import *
from Timer import timer

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


timer(points)

# Запись алгоритмов
writeFile(output_file, outJarvis, outGraham, outGrahamAndr, outQuickHull)

# Рисовка точек и выпуклой оболочки
drawAlgo(points, outJarvis, "Джарвис")
#drawAlgo(points, outGraham, "Грэхем")
#drawAlgo(points, outGrahamAndr, "Грэхем-Эндрю")
#drawAlgo(points, outQuickHull, "Быстрая оболочка")
