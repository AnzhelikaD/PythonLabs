"""Используя алгоритм «решето Эратосфена», найти все простые числа из
промежутка [2 ; n ] ."""


def sieveEratosthenes(n):
    setNumbers = {i for i in range(2, n + 1)}
    setPrimes = set()
    try:
        while len(setNumbers) > 0:
            Next = setNumbers.pop()
            setPrimes.add(Next)
            for i in range(Next, n + 1):
                if i % Next == 0:
                    setNumbers.discard(i)
        print(setPrimes)
    except Exception:
        print("Error")


N = int(input("Введите n: "))
sieveEratosthenes(N)
