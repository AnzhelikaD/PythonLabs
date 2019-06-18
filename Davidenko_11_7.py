"""Используя алгоритм «решето Эратосфена», найти и напечатать в порядке
убывания все простые числа из промежутка [ m; n ]"""
import math


def isPrime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def sieveEratosthenes(m, n):
    setNumbers = {i for i in range(2, n + 1)}
    setPrimes = set()
    try:
        while len(setNumbers) > 0:
            Next = setNumbers.pop()
            if Next >= m:
                setPrimes.add(Next)
            for i in range(Next, n + 1):
                if i % Next == 0:
                    setNumbers.discard(i)
        return setPrimes
    except Exception:
        print("Error")


M = int(input("Введите m: "))
N = int(input("Введите n: "))
print(sieveEratosthenes(M, N))
