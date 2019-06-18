"""Сортировать по возрастанию элементы списка с индексами от
i 1 до i 2 включительно. Метод сортировки: 1) выбором; 2) обменом; 3) включением."""
import random


def sortChoice(lst):
    print("Исходный список: ", lst)
    for i in range(len(lst)-1, 0, -1):
        maxElem = lst[i]
        idxMax = i
        for j in range(i):
            maxElem, idxMax = (lst[j], j) if lst[j] > maxElem else (maxElem, idxMax)
        if i != idxMax:
            lst[i], lst[idxMax] = lst[idxMax], lst[i]
        print("i = ", i, " list = ", lst)


def sortExchange(lst):
    print("Исходный список: ", lst)
    for i in range(len(lst)-1):
        for j in range(len(lst) - i - 1):
            lst[j], lst[j+1] = (lst[j+1], lst[j]) if lst[j] > lst[j+1] else (lst[j], lst[j+1])
        print("i = ", i, " list = ", lst)


def sortInclusion(lst):
    print("Исходный список: ", lst)
    for i in range(1, len(lst)):
        elem = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > elem:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = elem
        print("i = ", i, " list = ", lst)


n = int(input("Введите длину списка: "))
if n < 0:
    print("Ошибка: длина не может быть меньше 0")
else:
    random.seed()
    list1 = [random.randint(-10, 10) for i in range(n)]
    sortChoice(list1)
    print("Результат сортровки выбором: ", list1)

    list2 = [random.randint(-10, 10) for i in range(n)]
    sortExchange(list2)
    print("Результат сортровки обменом: ", list2)

    list3 = [random.randint(-10, 10) for i in range(n)]
    sortInclusion(list3)
    print("Результат сортровки включением: ", list3)
