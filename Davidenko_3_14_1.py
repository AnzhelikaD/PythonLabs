"""Даны целые числа a , b , c . Найти значение выражения
min(a, b, c) / ln a """

from math import *

print("Введите 3 целых числа")
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

if a <= 0:
    print("Ошибка: ln a")
else:
    denominator = log(a)
    if denominator == 0:
        print("Ошибка: Знаменатель равен 0")
    else:
        minAB = a if a < b else b
        numerator = minAB if minAB < c else c
        print("Результат: ", numerator / denominator)
        print("Проверка: ", min(a, b, c) / log(a))
