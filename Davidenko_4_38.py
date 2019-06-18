"""Определить, является ли заданное число n совершенным."""

print("Введите натуральное число")
n = int(input("n = "))

if n < 1:
    print("Ошибка: n < 1")
else:
    divSum = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            divSum += i

    if divSum == n:
        print("%d - совершенное число" % n)
    else:
        print("%d - не совершенное число" % n)
