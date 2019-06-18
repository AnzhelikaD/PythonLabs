"""Заполнить массив размеров (2 n + 1) × (2 n + 1) по правилу"""


def printDrawing(mrx):
    for i in range(len(mrx)):
        print("".join(mrx[i]))


def drawSquares(n):
    listIndexes = [n*i for i in range(3)]
    size = listIndexes[2] + 1
    matrix = [[" "] * size for i in range(size)]

    for i in range(size):
        if i in listIndexes:
            for j in range(size):
                matrix[i][j] = "*"
        else:
            for j in range(size):
                if j in listIndexes:
                    matrix[i][j] = "*"
    printDrawing(matrix)


def makeDiagonal(mrx):
    for i in range(len(mrx)):
        for j in range(len(mrx[i])):
            if i == j:
                mrx[i][j] = "*"


def makeCross(mrx):
    makeDiagonal(mrx)
    for i in range(len(mrx)):
        mrx[i].reverse()
    makeDiagonal(mrx)


def drawCross(n):
    size = 2*n + 1
    matrix = [[" "] * size for i in range(size)]
    makeCross(matrix)
    printDrawing(matrix)


def drawSnowflake(n):
    size = 2 * n + 1
    matrix = [[" "] * size for i in range(size)]
    makeCross(matrix)
    for i in range(size):
        if i == n:
            for j in range(size):
                matrix[i][j] = "*"
        else:
            for j in range(size):
                if j == n:
                    matrix[i][j] = "*"
    printDrawing(matrix)


drawSquares(3)
print()
drawCross(3)
print()
drawSnowflake(3)
