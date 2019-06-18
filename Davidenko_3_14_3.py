"""Даны целые числа a , b , c . Найти значение выражения
max(a, b, c) / min (a, b ,c) """

print("Введите 3 целых числа")
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

minAB = a if a < b else b
denominator = minAB if minAB < c else c

if denominator == 0:
    print("Ошибка: Знаменатель равен 0")
else:
    maxAB = a if a > b else b
    numerator = maxAB if maxAB > c else c
    print("Результат: ", numerator / denominator)
    print("Проверка: ", max(a, b, c) / min(a, b, c))
0