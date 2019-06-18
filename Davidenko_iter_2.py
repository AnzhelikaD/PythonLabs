"""С помощью функции map, увеличьте на 1 все значения в списке."""
import random


def incListElems(lst):
    return list(map(lambda x: x + 1, lst))


n = int(input("Введите длину списка: "))
if n < 0:
    print("Ошибка: длина не может быть меньше 0")
else:
    random.seed()
    list1 = [random.randint(-10, 10) for i in range(n)]
    print("Исходный список: ", list1)
    print(incListElems(list1))
