import numpy as np


# Тест, который генирирет наши рандомные точки от 0 и до 100
def TestPoints(numberPoints):
    arrpoints = []
    for i in range(numberPoints):
        x = np.random.randint(-10000, 10000)
        y = np.random.randint(-10000, 10000)
        point = (x, y)
        arrpoints.append(point)

    return arrpoints

# Запись наших рандомных точек в файлик
def writeFile_randPoints(file_path, arrpoints):
    with open(file_path, 'w') as file:
        for p in arrpoints:
            file.write(f"{p}\n")
