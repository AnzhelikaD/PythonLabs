"""Даны целые числа a , b , c . Найти значение выражения
max(a, b, c) / sign(a) """

print("Введите 3 целых числа")
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

if a == 0:
    print("Ошибка: Знаменатель равен 0")
else:
    maxAB = a if a > b else b
    numerator = maxAB if maxAB > c else c
    denominator = -1 if (a < 0) else 1
    print("Результат: ", numerator / denominator)
    print("Проверка: ", max(a, b, c) / denominator)
