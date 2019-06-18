"""Удалить из целочисленного списка все элементы с минимальным значением
(предполагается, что имеется несколько таких элементов)."""


def deleteAllMin(vector):
    minElem = vector[0]
    for elem in vector:
        minElem = min(elem, minElem)
    while minElem in vector:
        vector.remove(minElem)


n = int(input("Введите длину списка: "))
if n < 1:
    print("Ошибка: длина не может быть меньше 1")
else:
    lst = [int(input()) for i in range(n)]
    deleteAllMin(lst)
    print(lst)