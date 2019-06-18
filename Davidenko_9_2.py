"""Используя любой алгоритм сортировки, расположить числа в списке в порядке убывания модулей."""
import random


def sortAbs(lst):
    print("Исходный список: ", lst)
    for i in range(len(lst) - 1):
        for j in range(len(lst) - i - 1):
            lst[j], lst[j + 1] = (lst[j + 1], lst[j]) if abs(lst[j]) < abs(lst[j + 1]) else (lst[j], lst[j + 1])
        print("i = ", i, " list = ", lst)


n = int(input("Введите длину списка: "))
if n < 0:
    print("Ошибка: длина не может быть меньше 0")
else:
    random.seed()
    list1 = [random.randint(-10, 10) for i in range(n)]
    sortAbs(list1)
    print("Результат сортровки обменом: ", list1)
