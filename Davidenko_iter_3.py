"""С помощью функций map и filter, выберите из списка все положительные числа
и возведите их в куб."""
import random


def allPositive3(lst):
    poslst = list(filter(lambda x: x > 0, lst))
    return list(map(lambda x: x**3, poslst))


n = int(input("Введите длину списка: "))
if n < 0:
    print("Ошибка: длина не может быть меньше 0")
else:
    random.seed()
    list1 = [random.randint(-10, 10) for i in range(n)]
    print("Исходный список: ", list1)
    print(allPositive3(list1))
