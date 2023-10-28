# Читаем координаты точек из файла
def read_file(file_path):
    points = []
    with open(file_path, 'r') as file:
        for line in file:
            coordinates = line.split(' ')
            x = float(coordinates[0])
            y = float(coordinates[1])
            point = (x, y)
            points.append(point)

    return points


# Записывает координаты точек в файл
def writeFile(file_path, pointsJv, poitnsGr, pointsGA, pointsQH):
    with open(file_path, 'w') as file:
        file.write("Jarvis Algo\n")
        for p in pointsJv:
            file.write(f"{p} ")
        file.write("\n\nGraham Algo\n")
        for p in poitnsGr:
            file.write(f"{p} ")
        file.write("\n\nGraham-And Algo\n")
        for p in pointsGA:
            file.write(f"{p} ")
        file.write("\n\nQuickHull Algo\n")
        for p in pointsQH:
            file.write(f"{p} ")

