"""Определить, есть ли в последовательности простые числа."""
import math


def isPrime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def containsPrime(vector):
    for elem in vector:
        if isPrime(elem):
            return True
    return False


n = int(input("Введите длину списка: "))
if n < 0:
    print("Ошибка: длина не может быть меньше 0")
else:
    lst = [int(input()) for i in range(n)]
    if containsPrime(lst):
        print("Последовательность содержит простые числа")
    else:
        print("Последовательность НЕ содержит простые числа")
