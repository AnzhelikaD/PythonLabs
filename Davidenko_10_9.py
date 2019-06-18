"""Дана целочисленная матрица A ( 3 × 3 ). Элементы каждой строки матрицы
поделить на максимальный элемент данной строки. На печать выдавать 1) исходную
матрицу; 2) вектор-столбец максимальных элементов каждой строки; 3) преобразованную матрицу."""
import random


def transformation(mrx):
    listMax = []
    for i in range(len(mrx)):
        maxElem = max(mrx[i])
        for j in range(len(mrx[i])):
            mrx[i][j] /= maxElem
        listMax.append(maxElem)
    return listMax


n = 3
random.seed()
matrix = [[random.randint(-10, 10) for i in range(n)] for j in range(n)]
print("Исходная матрица: ")
for i in range(n):
    print(matrix[i])
maxElems = transformation(matrix)
print("Максимальные элементы: ", maxElems)
print("Преобразованная матрица: ")
for i in range(n):
    print(matrix[i])
