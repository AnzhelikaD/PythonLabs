"""Элементы последовательности — натуральные числа. Определить, верно ли,
что последовательность содержит хотя бы одно чётное число."""


def containsEven(lst):
    for elem in lst:
        if elem % 2 == 0:
            return True
    return False


n = int(input("Введите длину последовательности: "))
if n < 0:
    print("Ошибка: длина не может быть меньше 0")
else:
    vector = [int(input()) for i in range(n)]
    if containsEven(vector):
        print("Последовательность содержит четные числа")
    else:
        print("Последовательность НЕ содержит четные числа")
