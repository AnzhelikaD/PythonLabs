"""Написать программу для сложения двух полиномов разной степени. Коэф-
фициенты полиномов-слагаемых получать случайным образом."""
import random


def sumpolynomial(p1, p2):
    minlength = min(len(p1), len(p2))
    maxp = p1 if len(p1) > len(p2) else p2
    p = [p1[i] + p2[i] for i in range(minlength)]
    return p + maxp[minlength:]


n = int(input("Введите степень первого полинома: "))
m = int(input("Введите степень второого полинома: "))
if n < 0 or m < 0:
    print("Ошибка: Степень полинома меньше 0")
else:
    random.seed()
    p1 = [random.randint(0, 9) for i in range(n)]
    p2 = [random.randint(0, 9) for j in range(m)]
    print(p1)
    print(p2)
    print(sumpolynomial(p1, p2))
